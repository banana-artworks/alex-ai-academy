from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

SQLALCHEMY_DATABASE_URL = "sqlite:///./alex_academy.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Lesson(Base):
    __tablename__ = "lessons"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)
    status = Column(String, default="published")
    language = Column(String, default="de", index=True)  # de, en, zh, es
    original_topic = Column(String, nullable=True)  # Originales Thema für Referenz
    created_at = Column(DateTime, default=datetime.datetime.utcnow, index=True)

# Datenbank initialisieren
Base.metadata.create_all(bind=engine)
