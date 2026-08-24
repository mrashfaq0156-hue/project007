import os
import sys
import subprocess
import atexit

NOTES_FILE = "notes.txt"

def auto_github_backup():
    """پروگرام بند ہوتے ہی تمام فائلز کو خود بخود GitHub پر اپلوڈ کرنے والا فنکشن"""
    print("\n" + "="*50)
    print("🔄 GitHub Auto-Backup System Running...")
    print("="*50)
    try:
        # 1. نئی اور تبدیل شدہ فائلز کو سٹیج کریں
        subprocess.run(["git", "add", "."], check=True)
        
        # 2. سیو پوائنٹ (Commit) بنائیں
        subprocess.run(["git", "commit", "-m", "Auto-backup: Saved via Project 007 System"], check=True)
        
        # 3. GitHub پر پش کریں
        subprocess.run(["git", "push"], check=True)
        print("✅ پروجیکٹ خود بخود GitHub پر محفوظ کر دیا گیا ہے!")
    except subprocess.CalledProcessError:
        print("ℹ️ کوئی نئی تبدیلی موجود نہیں تھی یا بیک اپ پہلے ہی اپ ٹو ڈیٹ ہے۔")
    except Exception as e:
        print(f"⚠️ آٹو بیک اپ کے دوران مسئلہ آیا: {e}")

# پروگرام مکمل طور پر بند ہوتے ہی یہ فنکشن خود بخود چلے گا
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

def main():
    print("="*50)
    print("🤖 Welcome to Project 007 - AI & Command System")
    print("="*50)
    
    notes = load_notes()

    while True:
        print("\n--- Main Menu ---")
        print("1. Show All Notes")
        print("2. Add New Note")
        print("3. Manual GitHub Backup (Optional)")
        print("4. Exit Program (Auto-Saves to GitHub)")
        
        choice = input("Enter choice (1-4): ").strip()

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
            auto_github_backup()

        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()