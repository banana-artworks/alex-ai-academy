import logging
import os
from datetime import datetime
from typing import List

import anthropic
from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

import database as db
from orchestrator import AlexOrchestrator

# ============ Anthropic Client für Titel-Übersetzung ============
anthropic_client = anthropic.Anthropic()

LANG_NAMES = {
    "de": "German",
    "en": "English",
    "zh": "Chinese (Simplified)",
    "es": "Spanish"
}

def translate_title(topic: str, lang: str) -> str:
    """Übersetzt den Thementitel in die Zielsprache via Claude."""
    if lang == "de":
        return topic  # Kein Übersetzen nötig
    try:
        target_lang = LANG_NAMES.get(lang, "English")
        message = anthropic_client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=100,
            messages=[{
                "role": "user",
                "content": f"Translate this course title to {target_lang}. Return ONLY the translated title, nothing else:\n\n{topic}"
            }]
        )
        translated = message.content[0].text.strip()
        logger.info(f"📝 Title translated: '{topic}' → '{translated}' ({lang})")
        return translated
    except Exception as e:
        logger.warning(f"Title translation failed, using original: {e}")
        return topic  # Fallback auf Original

# ============ Setup Logging ============
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ============ Initialize FastAPI ============
app = FastAPI(
    title="A.L.E.X. Academy API",
    version="2.1.1",
    description="Multilingual AI Learning Platform"
)

# ============ Initialize AI Orchestrator ============
try:
    alex = AlexOrchestrator()
    logger.info("✅ A.L.E.X. Orchestrator initialized successfully")
except Exception as e:
    logger.error(f"❌ Failed to initialize: {e}")
    alex = None

# ============ Middleware (CORS) ============
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============ Pydantic Models ============

class LessonRequest(BaseModel):
    topic: str = Field(..., min_length=2, max_length=200)
    language: str = Field(default="de", pattern="^(de|en|zh|es)$")

    class Config:
        json_schema_extra = {
            "example": {
                "topic": "Python Basics",
                "language": "de"
            }
        }

class LessonResponse(BaseModel):
    id: int
    title: str
    content: str
    status: str
    language: str
    original_topic: str
    created_at: datetime

    class Config:
        from_attributes = True

# ============ Dependencies ============

def get_db():
    session = db.SessionLocal()
    try:
        yield session
    finally:
        session.close()

# ============ ROUTES ============

@app.get("/", response_class=HTMLResponse)
async def root():
    """Dient als Einstiegspunkt für die index.html"""
    try:
        with open("index.html", "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        logger.error(f"Error serving index.html: {e}")
        return "<h1>Error: index.html not found</h1>"

@app.get("/api/health")
def health_check():
    """Status-Check für die Status-Lampe im Frontend"""
    return {
        "status": "ok",
        "service": "A.L.E.X. Academy API",
        "version": "2.1.1",
        "ai_ready": alex is not None
    }

@app.get("/api/lessons", response_model=List[LessonResponse])
def get_all_lessons(
    limit: int = Query(50, ge=1, le=500),
    language: str = Query("de", pattern="^(de|en|zh|es)$"),
    db_session: Session = Depends(get_db)
):
    """Lade Lektionen gefiltert nach Sprache"""
    try:
        lessons = (
            db_session.query(db.Lesson)
            .filter(db.Lesson.language == language)
            .order_by(db.Lesson.created_at.desc())
            .limit(limit)
            .all()
        )
        logger.info(f"Retrieved {len(lessons)} lessons in {language}")
        return lessons
    except Exception as e:
        logger.error(f"Error fetching lessons: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch lessons")

@app.get("/api/lessons/{lesson_id}", response_model=LessonResponse)
def get_lesson(lesson_id: int, db_session: Session = Depends(get_db)):
    """Einzelne Lektion laden"""
    try:
        lesson = db_session.query(db.Lesson).filter(db.Lesson.id == lesson_id).first()
        if not lesson:
            raise HTTPException(status_code=404, detail="Lesson not found")
        return lesson
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error fetching lesson: {e}")
        raise HTTPException(status_code=500, detail="Failed to fetch lesson")

@app.post("/api/generate-lesson", response_model=LessonResponse)
def generate_lesson(
    request: LessonRequest,
    db_session: Session = Depends(get_db)
):
    """KI-Generierung einer Lektion"""
    if not alex:
        raise HTTPException(status_code=503, detail="AI engine not initialized")

    topic = request.topic.strip()
    lang = request.language

    try:
        logger.info(f"🚀 Generating {lang} lesson for: {topic}")

        # Titel in Zielsprache übersetzen (DE bleibt unverändert)
        translated_title = translate_title(topic, lang)

        # Sprache wird an den Orchestrator übergeben (Fallback falls kein lang-Parameter)
        try:
            result_text = alex.run_learning_chain(topic, lang)
        except TypeError:
            # Falls der Orchestrator nur einen Parameter akzeptiert
            logger.warning("Orchestrator does not accept 'lang' parameter, falling back to topic-only call")
            result_text = alex.run_learning_chain(topic)

        new_lesson = db.Lesson(
            title=translated_title,   # ✅ Übersetzter Titel
            content=result_text,
            status="published",
            language=lang,
            original_topic=topic      # Original-Thema bleibt erhalten
        )
        db_session.add(new_lesson)
        db_session.commit()
        db_session.refresh(new_lesson)

        logger.info(f"✅ Lesson created with ID: {new_lesson.id}")
        return new_lesson

    except Exception as e:
        logger.error(f"Error generating lesson: {e}")
        db_session.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/api/lessons/{lesson_id}")
def delete_lesson(lesson_id: int, db_session: Session = Depends(get_db)):
    """Löschen einer Lektion"""
    try:
        lesson = db_session.query(db.Lesson).filter(db.Lesson.id == lesson_id).first()
        if not lesson:
            raise HTTPException(status_code=404, detail="Lesson not found")

        db_session.delete(lesson)
        db_session.commit()
        logger.info(f"🗑️ Lesson {lesson_id} deleted")

        return {"message": f"Lesson {lesson_id} deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error deleting lesson: {e}")
        db_session.rollback()
        raise HTTPException(status_code=500, detail="Failed to delete lesson")

@app.get("/api/stats")
def get_stats(db_session: Session = Depends(get_db)):
    """Plattform-Statistiken laden"""
    try:
        total = db_session.query(db.Lesson).count()

        stats = {
            "total_lessons": total,
            "by_language": {
                "de": db_session.query(db.Lesson).filter(db.Lesson.language == "de").count(),
                "en": db_session.query(db.Lesson).filter(db.Lesson.language == "en").count(),
                "zh": db_session.query(db.Lesson).filter(db.Lesson.language == "zh").count(),
                "es": db_session.query(db.Lesson).filter(db.Lesson.language == "es").count(),
            }
        }
        return stats
    except Exception as e:
        logger.error(f"Error getting stats: {e}")
        raise HTTPException(status_code=500, detail="Failed to get stats")

@app.post("/api/translate-all")
def translate_all_lessons(
    language: str = Query(..., pattern="^(en|zh|es)$"),
    db_session: Session = Depends(get_db)
):
    """
    Übersetzt alle deutschen Lektionen in die Zielsprache.
    Überspringt Lektionen die bereits übersetzt wurden (via original_topic).
    """
    if language == "de":
        raise HTTPException(status_code=400, detail="Target language cannot be 'de'")

    target_lang = LANG_NAMES.get(language, "English")

    # Alle DE-Lektionen laden
    de_lessons = db_session.query(db.Lesson).filter(db.Lesson.language == "de").all()
    if not de_lessons:
        return {"translated": 0, "skipped": 0, "message": "No German lessons found"}

    # Bereits übersetzte original_topics sammeln
    existing_topics = set(
        row.original_topic for row in
        db_session.query(db.Lesson.original_topic).filter(db.Lesson.language == language).all()
    )

    translated_count = 0
    skipped_count = 0

    for lesson in de_lessons:
        # Überspringen falls bereits übersetzt
        if lesson.original_topic in existing_topics:
            skipped_count += 1
            continue

        try:
            # Titel + Inhalt in einem API-Call übersetzen
            message = anthropic_client.messages.create(
                model="claude-haiku-4-5-20251001",
                max_tokens=4096,
                messages=[{
                    "role": "user",
                    "content": (
                        f"Translate the following lesson title and content to {target_lang}.\n"
                        f"Return ONLY this exact format (no extra text):\n"
                        f"TITLE: <translated title>\n"
                        f"CONTENT:\n<translated content>\n\n"
                        f"---\n"
                        f"TITLE: {lesson.title}\n"
                        f"CONTENT:\n{lesson.content}"
                    )
                }]
            )

            response_text = message.content[0].text.strip()

            # Titel und Inhalt aus der Antwort extrahieren
            if "TITLE:" in response_text and "CONTENT:" in response_text:
                title_part = response_text.split("CONTENT:")[0].replace("TITLE:", "").strip()
                content_part = response_text.split("CONTENT:", 1)[1].strip()
            else:
                title_part = lesson.title  # Fallback
                content_part = response_text

            new_lesson = db.Lesson(
                title=title_part,
                content=content_part,
                status="published",
                language=language,
                original_topic=lesson.original_topic
            )
            db_session.add(new_lesson)
            db_session.commit()
            translated_count += 1
            logger.info(f"✅ Translated [{translated_count}]: '{lesson.title}' → '{title_part}'")

        except Exception as e:
            logger.error(f"❌ Failed to translate '{lesson.title}': {e}")
            db_session.rollback()
            continue

    logger.info(f"🌍 Translation complete: {translated_count} translated, {skipped_count} skipped")
    return {
        "translated": translated_count,
        "skipped": skipped_count,
        "language": language,
        "message": f"Done! {translated_count} lessons translated to {target_lang}."
    }


if __name__ == "__main__":
    import uvicorn
    logger.info("Starting A.L.E.X. Academy API...")
    uvicorn.run(app, host="127.0.0.1", port=8000)
