import os
import sys
import subprocess
import atexit
from google import genai

NOTES_FILE = "notes.txt"

try:
    client = genai.Client()
except Exception as e:
    client = None

def auto_github_backup():
    try:
        subprocess.run(["git", "add", "."], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(["git", "commit", "-m", "Auto-backup: Master Agent Core"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run(["git", "push"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception:
        pass

atexit.register(auto_github_backup)

def master_agent_orchestrator(user_command):
    print("\n🤖 [Master Agent 007]: حکم پروسیس ہو رہا ہے...")

    if not client:
        print("⚠️ الرٹ: جیمنائی کلائنٹ کنفیگر نہیں ہو سکا۔")
        return

    system_prompt = (
        "You are Project 007, an elite fully autonomous master AI assistant. "
        "Always answer the user's questions clearly, accurately, and professionally in English."
    )

    try:
        # یہاں ماڈل کا نام بالکل لیٹسٹ اور درست (gemini-3.6-flash) سیٹ کر دیا گیا ہے
        response = client.models.generate_content(
            model='gemini-3.6-flash',
            contents=f"{system_prompt}\n\nUser Command: {user_command}"
        )
        
        print("\n" + "="*50)
        print("✨ [Autonomous AI Output]:")
        print("="*50)
        print(response.text)
        print("="*50)

    except Exception as e:
        print(f"⚠️ خرابی پیش آئی: {e}")

def main():
    if len(sys.argv) > 1:
        user_command = " ".join(sys.argv[1:])
        master_agent_orchestrator(user_command)
        return

    print("="*50)
    print("🤖 Project 007 - Multi-Agent Master System Active")
    print("="*50)
    
    auto_github_backup()

    while True:
        try:
            user_input = input("\n💡 What would you like to do? (Type 'exit' to quit): ").strip()
            if user_input.lower() == 'exit':
                print("Exiting... GitHub background sync completed.")
                break
            elif user_input:
                master_agent_orchestrator(user_input)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()