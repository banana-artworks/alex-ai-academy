"""
A.L.E.X. Content Generator
Generiert alle Kurs-Lektionen in 4 Sprachen: Deutsch, Englisch, Chinesisch, Spanisch
"""

import os
import time
from datetime import datetime
from anthropic import Anthropic
from dotenv import load_dotenv
import database as db

# Konfiguration
load_dotenv()
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# ============ LERNPFAD STRUKTUR ============

CURRICULUM = {
    "MODUL 1: Anfänger (Was ist KI?)": [
        "Geschichte der Künstlichen Intelligenz - Von Turing bis heute",
        "Machine Learning vs. Deep Learning vs. Large Language Models - Unterschiede erklären",
        "Wie funktionieren Sprachmodelle? Transformer und Tokenization",
        "Claude vs. ChatGPT vs. Gemini - Vergleich der Top KI-Modelle",
        "Deine erste API-Anfrage mit Python",
        "API Keys und Sicherheit - Best Practices",
    ],
    "MODUL 2: Anfänger (Prompt Engineering Basics)": [
        "Was ist ein Prompt? Definition und Grundkonzepte",
        "Zero-Shot vs. Few-Shot Prompting - Praktische Unterschiede",
        "Chain-of-Thought Prompting - Schritt-für-Schritt Denken",
        "Die richtige Temperatur und Parameter wählen",
        "Häufige Fehler beim Prompting und wie man sie vermeidet",
        "Praktische Übung: Den perfekten Prompt schreiben",
    ],
    "MODUL 3: Anfänger (Praktische Tools)": [
        "ChatGPT / Claude Web-Interface - Wie man es richtig nutzt",
        "Browser-Extensions für KI - ChatGPT für Google und mehr",
        "Erste API Integration in Python - Ein einfaches Beispiel",
        "Anthropic Python SDK - Installation und Grundlagen",
        "Kosten und Rate Limits verstehen - Budget planen",
        "Projekt: Baue deinen ersten einfachen Chatbot",
    ],
    "MODUL 4: Fortgeschrittene (Advanced Prompting)": [
        "Jailbreaking verstehen - Wie KI-Constraints funktionieren",
        "Persona-basierte Prompts - Rollen effektiv nutzen",
        "Structured Output und JSON Mode - Strukturierte Antworten",
        "Multi-Turn Conversations - Kontexte managen",
        "Context Window Management - Effizienz maximieren",
        "Projekt: Baue ein Q&A System mit Memory",
    ],
    "MODUL 5: Fortgeschrittene (Production-Ready Code)": [
        "Error Handling und Retry Logic - Robuste Systeme",
        "Caching und Optimierung - Kosten senken",
        "Logging und Monitoring - Debug und Track",
        "Testing KI-Outputs - Validierung und Qualität",
        "Kosten-Tracking und Analytics",
        "Projekt: Baue ein produktives CLI-Tool",
    ],
    "MODUL 6: Fortgeschrittene (Integration & APIs)": [
        "FastAPI für KI-Backends - Professionelle Server",
        "Webhooks und Asynchrone Calls - Skalierung",
        "File Upload und Processing - Datei-Handling",
        "Vector Databases - Einführung in die Grundlagen",
        "RAG (Retrieval-Augmented Generation) - Externe Knowledge",
        "Projekt: Baue ein Dokumenten-QA System",
    ],
    "MODUL 7: Profi (Advanced Architectures)": [
        "Multi-Agent Systems - Wie A.L.E.X. funktioniert",
        "Tool Use und Function Calling - KI-Werkzeuge erweitern",
        "Vision Models und Image Analysis - Bilder verstehen",
        "Fine-Tuning vs. Prompt Tuning - Wann welcher Ansatz?",
        "LangChain und LlamaIndex - Popular Frameworks",
        "Projekt: Baue deinen eigenen Multi-Agent",
    ],
    "MODUL 8: Profi (Deployment & Scaling)": [
        "Docker und Containerization - Production-Ready",
        "Cloud Deployment - AWS, GCP, Azure Optionen",
        "Load Balancing und Auto-Scaling - Millionen User",
        "Security Best Practices - Deine KI schützen",
        "GDPR und Privacy Compliance - Rechtliche Basics",
        "Projekt: Setze einen Produktionsserver auf",
    ],
    "MODUL 9: Profi (Business & Ethics)": [
        "AI Safety und Alignment - Die Zukunft sicher gestalten",
        "Bias Detection und Mitigation - Faire KI",
        "Pricing Models und ROI - Geschäftsmodelle",
        "Ethical AI Guidelines - Verantwortungsvolle KI",
        "AI Regulation - EU AI Act und Global Standards",
        "Projekt: Compliance Audit für dein KI-System",
    ],
}

# ============ SPRACH-PROMPTS ============

LANGUAGE_PROMPTS = {
    "de": {
        "system": "Du bist ein erfahrener KI-Kurs-Autor und Experte für Künstliche Intelligenz. Schreibe eine hochwertige, strukturierte Lektion auf Deutsch.",
        "instruction": "Schreibe eine umfassende, professionelle Lektion zum Thema: '{topic}'\n\nStruktur:\n# {topic}\n\n## Einführung\n[Kurze, ansprechende Einführung]\n\n## Hauptinhalte\n[2-3 Hauptabschnitte mit Überschriften]\n\n## Praktische Beispiele\n[Konkrete Code-Beispiele oder Anwendungsfälle]\n\n## Wichtige Punkte\n[Zusammenfassung der Key Takeaways]\n\n## Nächste Schritte\n[Was man als nächstes lernen sollte]\n\nMache die Lektion interaktiv, praktisch und für Anfänger verständlich. Nutze Emojis für bessere Lesbarkeit."
    },
    "en": {
        "system": "You are an experienced AI course instructor and expert. Write a high-quality, structured lesson in English.",
        "instruction": "Write a comprehensive, professional lesson on the topic: '{topic}'\n\nStructure:\n# {topic}\n\n## Introduction\n[Brief, engaging introduction]\n\n## Key Concepts\n[2-3 main sections with subheadings]\n\n## Practical Examples\n[Concrete code examples or real-world applications]\n\n## Key Takeaways\n[Summary of important points]\n\n## Next Steps\n[What to learn next]\n\nMake the lesson interactive, practical, and beginner-friendly. Use emojis for better readability."
    },
    "zh": {
        "system": "你是一位经验丰富的人工智能课程讲师和专家。用中文撰写高质量、结构化的课程。",
        "instruction": "关于'{topic}'这个主题写一篇全面、专业的课程\n\n结构:\n# {topic}\n\n## 介绍\n[简短吸引人的介绍]\n\n## 核心概念\n[2-3个主要部分和子标题]\n\n## 实际例子\n[具体的代码示例或实际应用]\n\n## 重点总结\n[重要内容的总结]\n\n## 下一步\n[接下来应该学什么]\n\n使课程具有交互性、实用性和初学者友好。使用表情符号提高可读性。"
    },
    "es": {
        "system": "Eres un instructor de cursos de IA experimentado y experto. Escribe una lección de alta calidad y bien estructurada en español.",
        "instruction": "Escribe una lección integral y profesional sobre el tema: '{topic}'\n\nEstructura:\n# {topic}\n\n## Introducción\n[Introducción breve y atractiva]\n\n## Conceptos Clave\n[2-3 secciones principales con subtítulos]\n\n## Ejemplos Prácticos\n[Ejemplos de código concretos o aplicaciones del mundo real]\n\n## Puntos Clave\n[Resumen de puntos importantes]\n\n## Próximos Pasos\n[Qué aprender a continuación]\n\nHaz la lección interactiva, práctica y amigable para principiantes. Usa emojis para mejor legibilidad."
    }
}

# ============ GENERATOR ============

def generate_content():
    """Generiert alle Lektionen in allen Sprachen"""
    
    print("\n" + "="*60)
    print("🚀 A.L.E.X. CONTENT GENERATOR - Starting")
    print("="*60)
    
    session = db.SessionLocal()
    total_lessons = sum(len(topics) for topics in CURRICULUM.values())
    total_to_generate = total_lessons * 4  # 4 Sprachen
    counter = 0
    
    start_time = time.time()
    
    try:
        # Alle bestehenden Lektionen löschen (um sauberzustarten)
        print("\n🗑️  Lösche alte Lektionen...")
        session.query(db.Lesson).delete()
        session.commit()
        print("✅ Alte Lektionen gelöscht")
        
        # Durch alle Module und Themen gehen
        for module_name, topics in CURRICULUM.items():
            print(f"\n📚 Modul: {module_name}")
            print("-" * 60)
            
            for topic in topics:
                print(f"\n  📖 Topic: {topic}")
                
                # Für jede Sprache generieren
                for language_code in ["de", "en", "zh", "es"]:
                    counter += 1
                    lang_name = {"de": "🇩🇪 Deutsch", "en": "🇬🇧 English", "zh": "🇨🇳 中文", "es": "🇪🇸 Español"}[language_code]
                    
                    print(f"    {lang_name} ({counter}/{total_to_generate})", end=" ... ", flush=True)
                    
                    try:
                        # Generiere mit Claude
                        message = client.messages.create(
                            model="claude-sonnet-4-20250514",
                            max_tokens=2000,
                            system=LANGUAGE_PROMPTS[language_code]["system"],
                            messages=[{
                                "role": "user",
                                "content": LANGUAGE_PROMPTS[language_code]["instruction"].format(topic=topic)
                            }]
                        )
                        
                        content = message.content[0].text
                        
                        # Speichere in Datenbank
                        lesson = db.Lesson(
                            title=topic,
                            content=content,
                            status="published",
                            language=language_code,
                            original_topic=topic
                        )
                        session.add(lesson)
                        session.commit()
                        
                        print("✅")
                        
                        # Rate limiting (API-Limits respektieren)
                        time.sleep(1)
                        
                    except Exception as e:
                        print(f"❌ Error: {str(e)}")
                        session.rollback()
                        continue
        
        elapsed = time.time() - start_time
        print("\n" + "="*60)
        print(f"✨ FERTIG! {total_to_generate} Lektionen generiert")
        print(f"⏱️  Zeit: {elapsed:.1f} Sekunden")
        print(f"📊 Durchschnitt: {elapsed/total_to_generate:.1f}s pro Lektion")
        print("="*60 + "\n")
        
    except Exception as e:
        print(f"\n❌ FEHLER: {str(e)}")
        session.rollback()
    finally:
        session.close()

if __name__ == "__main__":
    print("\n🎓 A.L.E.X. Akademie - Content Generator\n")
    print("Dieser Prozess wird:")
    print("✓ 45+ Lektionen in 4 Sprachen generieren")
    print("✓ Alle in die Datenbank speichern")
    print("✓ ~30-45 Minuten dauern\n")
    
    confirm = input("Bereit zu starten? (ja/nein): ").lower().strip()
    if confirm in ["ja", "yes", "y", "j"]:
        generate_content()
    else:
        print("Abgebrochen.")
