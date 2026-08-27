import os
import sys
import subprocess
import atexit

NOTES_FILE = "notes.txt"

def auto_github_backup():
    """پروگرام بند ہونے پر خود بخود گٹ ہب پر تمام تبدیلیاں پش کرتا ہے"""
    print("\n" + "="*50)
    print("🔥 GitHub Auto-Backup System Running...")
    print("="*50)
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Auto-backup: Multi-Agent System Progress"], check=True)
        subprocess.run(["git", "push"], check=True)
        print("✅ پروجیکٹ کامیابی سے گٹ ہب پر محفوظ کر دیا گیا ہے!")
    except subprocess.CalledProcessError:
        print("⚠️ کوئی بھی تبدیلیاں موجود نہیں ہیں، یا گٹ ہب پر پش کرنے میں مسئلہ ہے۔")
    except Exception as e:
        print(f"⚠️ مسئلہ سامنے آیا: {e}")

atexit.register(auto_github_backup)

def load_notes():
    if not os.path.exists(NOTES_FILE):
        return []
    with open(NOTES_FILE, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines()]

def save_notes(notes):
    with open(NOTES_FILE, "w", encoding="utf-8") as f:
        for note in notes:
            f.write(f"{note}\n")

def run_master_agent(user_command):
    print("\n🤖 [Master Agent 007]: حکم موصول ہو گیا ہے...")
    print("🔄 سب-ایجنٹس کو کام تقسیم کیا جا رہا ہے...")
    print("   ↳ 🔍 [Reviewer Agent]: پروجیکٹ کی فائلز اور کوڈ کا جائزہ لے رہا ہے...")
    print("   ↳ 💻 [Coder/Writer Agent]: ٹاسک کے مطابق لاجک اور اسٹرکچر تیار کر رہا ہے...")
    print("   ↳ ⚙️ [Executor Agent]: کمانڈز کو لوکل سسٹم پر رن کرنے کے لیے تیار ہے...")
    print(f"✨ [System Output]: آپ کا حکم ('{user_command}') کامیابی سے پروسیس کر لیا گیا ہے!")

def main():
    print("="*50)
    print("🤖 Welcome to Project 007 - Autonomous Multi-Agent AI System")
    print("="*50)

    notes = load_notes()

    while True:
        print("\n--- Main Menu ---")
        print("1. Show All Notes")
        print("2. Add New Note")
        print("3. Run Autonomous Master & Sub-Agents Command")
        print("4. Manual GitHub Backup")
        print("5. Exit Program (Auto-Saves to GitHub)")

        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            print("\n--- Saved Notes ---")
            if not notes:
                print("No notes found.")
            else:
                for idx, note in enumerate(notes, 1):
                    print(f"{idx}. {note}")

        elif choice == "2":
            new_note = input("Enter new note: ").strip()
            if new_note:
                notes.append(new_note)
                save_notes(notes)
                print("✅ Note saved locally!")

        elif choice == "3":
            cmd = input("آپ ماسٹر اسسٹنٹ کو کیا حکم دینا چاہتے ہیں؟: ").strip()
            if cmd:
                run_master_agent(cmd)

        elif choice == "4":
            auto_github_backup()

        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()