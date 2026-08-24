import sys
import os

def save_note(note):
    # HID / User Approval Logic
    approval = input("[HID APPROVAL] Do you want to save this record? (y/n): ").strip().lower()
    if approval == 'y':
        with open("notes.txt", "a") as f:
            f.write(note + "\n")
        print("[AUTO-SAVE]: Record saved successfully to notes.txt!")
    else:
        print("[CANCELLED]: Action aborted by user.")

def main():
    print("========================================")
    print("      PROJECT 007: SECURITY CHECK       ")
    print("========================================")
    
    code = input("Enter Access Code: ")
    if code != "007":
        print("[ACCESS DENIED]: Invalid Code.")
        sys.exit()

    print("\n[ACCESS GRANTED]: Welcome Agent Ashfaq Ahmad.")
    print("========================================")
    print("   PROJECT 007: AI SYSTEM INITIALIZED   ")
    print("========================================")

    while True:
        cmd = input("\nProject007> ").strip().lower()
        if cmd == "exit":
            print("Shutting down Project 007... Goodbye!")
            break
        elif cmd == "status":
            print("[STATUS]: System is online, HID Auto-Save enabled.")
        elif cmd == "add":
            note = input("Enter new data/note: ")
            save_note(note)
        elif cmd == "help":
            print("Available commands: status, add, exit")
        else:
            print(f"[ERROR]: Unknown command '{cmd}'. Type 'help' for options.")

if __name__ == "__main__":
    main()