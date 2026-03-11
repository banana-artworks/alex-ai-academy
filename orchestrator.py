"""
A.L.E.X. Orchestrator - Multi-Agent Learning System
Coordinates AI agents (Researcher, Compiler, Critic) to generate lessons
"""

import os
import re
from datetime import datetime
from anthropic import Anthropic
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class AlexOrchestrator:
    """
    Multi-agent orchestrator for lesson generation
    
    Pipeline:
    1. Researcher: Gathers facts and context
    2. Compiler: Structures knowledge into lesson
    3. Critic: Optimizes for markdown and engagement
    """
    
    def __init__(self, student_level: int = 1, model: str = None):
        """
        Initialize orchestrator
        
        Args:
            student_level: 1-5 (1=Beginner, 5=Expert)
            model: Claude model to use (defaults to env var)
        """
        self.student_level = student_level
        self.model = model or os.getenv("ALEX_MODEL", "claude-sonnet-4-20250514")
        self.client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        
        if not os.getenv("ANTHROPIC_API_KEY"):
            raise ValueError("❌ ANTHROPIC_API_KEY not found in environment!")
        
        print(f"🚀 A.L.E.X. initialized | Level: {self.student_level} | Model: {self.model}")

    def ask_ai(self, prompt: str, system_role: str) -> str:
        """
        Call Claude API with structured prompt
        
        Args:
            prompt: User/task prompt
            system_role: System role/instruction
            
        Returns:
            AI response text or error message
        """
        try:
            message = self.client.messages.create(
                model=self.model,
                max_tokens=2000,
                system=system_role,
                messages=[{"role": "user", "content": prompt}]
            )
            return message.content[0].text
        except Exception as e:
            error_msg = f"❌ AI Agent Error: {str(e)}"
            print(error_msg)
            raise Exception(error_msg)

    def clean_filename(self, text: str) -> str:
        """Sanitize text for filename"""
        clean = re.sub(r'[\\/*?:"<>|]', "", text)
        return clean.replace(" ", "_")[:50]

    def run_learning_chain(self, topic: str) -> str:
        """
        Execute 3-agent chain to generate lesson
        
        Args:
            topic: Learning topic
            
        Returns:
            Markdown-formatted lesson content
            
        Raises:
            Exception: If any agent fails
        """
        if not topic or not topic.strip():
            raise ValueError("Topic cannot be empty!")
        
        topic = topic.strip()
        print(f"\n🔍 Starting learning chain for: '{topic}'")

        try:
            # Agent 1: Research
            print("  ⏳ [1/3] Researcher gathering facts...")
            research_data = self.ask_ai(
                f"Sammle 5-7 wichtige Fakten zu: {topic}", 
                "Du bist ein gründlicher Data-Analyst mit Fokus auf Genauigkeit."
            )

            # Agent 2: Compile
            print("  ⏳ [2/3] Compiler structuring knowledge...")
            compiled_lesson = self.ask_ai(
                f"Mache aus diesen Fakten eine gut strukturierte Lektion mit Überschriften:\n{research_data}", 
                "Du bist ein erfahrener Didaktik-Experte. Strukturiere klar mit H2/H3 Überschriften."
            )

            # Agent 3: Critic
            print("  ⏳ [3/3] Critic optimizing output...")
            final_markdown = self.ask_ai(
                f"Optimiere diesen Text für Markdown:\n- Nutze Emojis sinnvoll\n- Code-Blöcke wo relevant\n- Bullet Points\n\n{compiled_lesson}", 
                "Du bist ein strenger Chef-Redakteur mit hohen Standards."
            )

            # Save to local backup
            filename = f"{datetime.now().strftime('%Y-%m-%d')}_{self.clean_filename(topic)}.md"
            os.makedirs("lessons", exist_ok=True)
            filepath = os.path.join("lessons", filename)
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(final_markdown)
            
            print(f"  ✅ Lesson saved to: {filepath}")
            return final_markdown

        except Exception as e:
            print(f"❌ Learning chain failed: {e}")
            raise


def main():
    """CLI interface for testing"""
    try:
        alex = AlexOrchestrator(student_level=1)
        
        while True:
            print("\n" + "="*60)
            topic = input("What do you want to learn? (type 'exit' to quit)\n> ").strip()
            
            if topic.lower() == 'exit':
                print("Goodbye! 👋")
                break
            
            if not topic:
                print("⚠️  Please enter a valid topic")
                continue
            
            try:
                result = alex.run_learning_chain(topic)
                print(f"\n{'='*60}")
                print(result)
            except Exception as e:
                print(f"Error: {e}")
    
    except KeyboardInterrupt:
        print("\n\nInterrupted by user")


if __name__ == "__main__":
    main()
