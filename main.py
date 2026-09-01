import os
import sys
import platform
import subprocess
import psutil
import time
from datetime import datetime

# Windows terminal UTF-8 support
if sys.platform == "win32":
    import codecs
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.buffer)

class UltimateProject007Agent:
    def __init__(self):
        self.os_name = platform.system()
        self.workspace = "project_007_vault"
        os.makedirs(self.workspace, exist_ok=True)
        print("007-SYSTEM: Ultimate Agent Initialized Successfully.")

    def execute_command_with_self_healing(self, command: str, max_retries: int = 2) -> dict:
        """Self-healing loop for automatic error correction."""
        attempt = 0
        while attempt < max_retries:
            try:
                result = subprocess.run(
                    command,
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                    encoding="utf-8",
                    timeout=20
                )
                if result.returncode == 0:
                    return {"status": "success", "output": result.stdout.strip()}
                else:
                    attempt += 1
                    time.sleep(1)
            except Exception as e:
                return {"status": "error", "message": str(e)}
        return {"status": "failed", "message": "Command execution failed after retries."}

    def get_system_health(self) -> dict:
        """Live system hardware monitoring."""
        health = {
            "cpu": psutil.cpu_percent(interval=1),
            "ram": psutil.virtual_memory().percent,
            "disk": psutil.disk_usage('/').percent
        }
        print(f"System Health -> CPU: {health['cpu']}% | RAM: {health['ram']}% | Disk: {health['disk']}%")
        return health

    def save_note(self, filename: str, content: str):
        """Save text notes/data inside the vault directory."""
        if not filename.endswith(".txt"):
            filename += ".txt"
        filepath = os.path.join(self.workspace, filename)
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Note saved successfully: {filepath}")
        except Exception as e:
            print(f"Error saving note: {e}")

    def read_note(self, filename: str):
        """Read text notes from the vault directory."""
        if not filename.endswith(".txt"):
            filename += ".txt"
        filepath = os.path.join(self.workspace, filename)
        if os.path.exists(filepath):
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()
                print(f"--- Content of {filename} ---\n{content}\n-----------------------------")
            except Exception as e:
                print(f"Error reading note: {e}")
        else:
            print(f"Note not found: {filename}")

    def list_notes(self):
        """List all saved notes in the vault."""
        notes = os.listdir(self.workspace)
        if notes:
            print("Saved Notes in Vault:")
            for note in notes:
                print(f" - {note}")
        else:
            print("Vault is currently empty.")

    def start_console_loop(self):
        """Master console loop to take and execute live commands and manage notes."""
        print("\n--- Project 007 Ultimate Console Mode Active ---")
        print("Commands:")
        print("  - health               : Check CPU, RAM, and Disk status")
        print("  - save <name> <text>   : Save a text note to vault")
        print("  - read <name>          : Read a text note from vault")
        print("  - notes                : List all saved notes")
        print("  - exit                 : Quit the agent")
        print("  - [Any OS Command]     : Run command via self-healing execution\n")
        
        while True:
            try:
                command = input("007-COMMAND > ").strip()
                if not command:
                    continue
                
                parts = command.split(" ", 2)
                action = parts[0].lower()

                if action in ["exit", "quit", "band karo"]:
                    print("Shutting down Project 007. Goodbye!")
                    break
                elif action in ["health", "report"]:
                    self.get_system_health()
                elif action == "notes":
                    self.list_notes()
                elif action == "save" and len(parts) >= 3:
                    self.save_note(parts[1], parts[2])
                elif action == "save" and len(parts) < 3:
                    print("Usage error: Type 'save <filename> <content>'")
                elif action == "read" and len(parts) >= 2:
                    self.read_note(parts[1])
                elif action == "read" and len(parts) < 2:
                    print("Usage error: Type 'read <filename>'")
                else:
                    print(f"Executing: {command}")
                    res = self.execute_command_with_self_healing(command)
                    if res.get("status") == "success":
                        print(f"Output:\n{res.get('output')}")
                    else:
                        print(f"Message: {res.get('message')}")
            except KeyboardInterrupt:
                break

if __name__ == "__main__":
    agent = UltimateProject007Agent()
    agent.start_console_loop()