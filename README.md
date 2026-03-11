# 🪐 A.L.E.X. Academy
### Agentic Learning EXperience — AI-Powered Multilingual Learning Platform

![Status](https://img.shields.io/badge/Status-Live-00d4ff?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.11-3b82f6?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110-22c55e?style=flat-square&logo=fastapi)
![Claude AI](https://img.shields.io/badge/Powered_by-Claude_AI-ff6b35?style=flat-square)
![Languages](https://img.shields.io/badge/Languages-DE_|_EN_|_ZH_|_ES-a855f7?style=flat-square)

---

## 🚀 What is A.L.E.X. Academy?

A.L.E.X. Academy is a **full-stack AI learning platform** that generates high-quality course lessons on any AI/programming topic using a **3-Agent Orchestration Pipeline** powered by Anthropic Claude.

Users enter a topic → the AI researches, compiles, and critically reviews the content → a polished lesson is stored and displayed in a stunning **Space UI** with glassmorphism design.

**Live Features:**
- 🤖 3-Agent AI Pipeline (Researcher → Compiler → Critic)
- 🌍 4 Languages: German, English, Chinese, Spanish
- 🪐 Interactive Solar System Navigation (Orbit Map)
- 📚 220+ Lessons across 8 topic categories
- 🎨 Space/Glassmorphism UI with animated starfield
- 🔒 XSS-protected frontend

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | FastAPI + Uvicorn |
| **AI Engine** | Anthropic Claude (claude-haiku-4-5) |
| **Database** | SQLite + SQLAlchemy |
| **Frontend** | Vanilla HTML/CSS/JS (no frameworks) |
| **Fonts** | Orbitron + Rajdhani (Google Fonts) |
| **Animation** | requestAnimationFrame (60fps orbit) |

---

## 🧠 AI Architecture

```
User Input (Topic)
       │
       ▼
┌─────────────────┐
│  🔍 RESEARCHER  │  ← Gathers facts, context, examples
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  📝 COMPILER    │  ← Structures content into lesson format
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  ⚖️  CRITIC     │  ← Reviews quality, adds improvements
└────────┬────────┘
         │
         ▼
  Polished Lesson (Markdown)
  Stored in SQLite DB
```

---

## 🪐 Orbit Map Feature

The platform features a unique **solar system navigation UI** — each planet represents a topic category. Click a planet to see all lessons in that category.

- 8 Planets = 8 Categories (Python, KI/AI, Ethics, Security, Data, Web/API, Projects, More)
- Real-time animation via `requestAnimationFrame`
- Smooth category filtering

---

## ⚡ Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/alex-academy.git
cd alex-academy

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux

# 3. Install dependencies
pip install fastapi uvicorn anthropic sqlalchemy pydantic python-dotenv

# 4. Set your API key
echo "ANTHROPIC_API_KEY=your_key_here" > .env

# 5. Start the server
python backend.py

# 6. Open in browser
# http://127.0.0.1:8000
```

---

## 📁 Project Structure

```
alex-academy/
├── backend.py          # FastAPI server + API routes
├── orchestrator.py     # 3-Agent AI pipeline
├── generate_content.py # Content generation logic
├── database.py         # SQLAlchemy models
├── index.html          # Full frontend (single file)
├── .env                # API keys (not committed)
└── alex_academy.db     # SQLite database
```

---

## 🌍 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Serve frontend |
| `GET` | `/api/health` | Status check |
| `GET` | `/api/lessons` | Get lessons (by language) |
| `POST` | `/api/generate-lesson` | Generate new AI lesson |
| `DELETE` | `/api/lessons/{id}` | Delete lesson |
| `GET` | `/api/stats` | Platform statistics |
| `POST` | `/api/translate-all` | Translate all lessons to language |

---

## 👤 About the Developer

Built by a **Vibe Coder & AI Solutions Builder** — demonstrating that with the right AI tools and conceptual direction, anyone can build production-grade applications.

> "I don't write code — I architect solutions and direct AI to build them."

**Available for freelance projects on Upwork:**
- AI-powered web applications
- FastAPI backends with Claude/GPT integration
- Custom learning platforms
- Multilingual AI content pipelines

---

## 📄 License

MIT License — feel free to use and build upon this project.

---

<div align="center">
  <strong>A.L.E.X. Academy · Agentic Learning EXperience · Powered by Claude AI</strong>
</div>
