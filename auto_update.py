import os
import subprocess
import time

def update_repo():
    try:
        subprocess.run(["git", "fetch"], check=True)
        subprocess.run(["git", "reset", "--hard", "origin/main"], check=True)
        print("Repo erfolgreich aktualisiert.")
    except subprocess.CalledProcessError as e:
        print(f"Fehler beim Aktualisieren des Repos: {e}")

if __name__ == "__main__":
    while True:
        update_repo()
        print("Warte 10 Minuten...")
        time.sleep(600)  # Aktualisiere alle 10 Minuten
