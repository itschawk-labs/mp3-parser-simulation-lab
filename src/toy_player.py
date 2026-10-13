import sys
import time
import subprocess
from pathlib import Path

import pygame
from mutagen.id3 import ID3, ID3NoHeaderError

FIELD_NAME = "LAB_PARSER_TEST"
SIMULATED_LIMIT = 256

def read_lab_field(mp3_path: Path):
    try:
        tags = ID3(mp3_path)
    except ID3NoHeaderError:
        return None

    for frame in tags.getall("TXXX"):
        if frame.desc == FIELD_NAME:
            return "".join(frame.text)

    return None

def main():
    if len(sys.argv) != 2:
        print("Usage: python toy_player.py <file.mp3>")
        raise SystemExit(1)

    audio = Path(sys.argv[1]).resolve()

    if not audio.exists():
        print(f"File not found: {audio}")
        raise SystemExit(1)

    field = read_lab_field(audio)
    field_size = len(field.encode("utf-8")) if field else 0

    print()
    print("========== AUDIO FORENSICS LAB ==========")
    print(f"[PLAYER] File: {audio.name}")
    print(f"[PARSER] Test field present: {field is not None}")
    print(f"[PARSER] Simulated safe limit: {SIMULATED_LIMIT} bytes")
    print(f"[PARSER] Received: {field_size} bytes")
    print()

    pygame.mixer.init()
    pygame.mixer.music.load(str(audio))
    pygame.mixer.music.play()

    print("[PLAYER] Playback started.")
    time.sleep(0.35)

    if (
        field is not None
        and field_size > SIMULATED_LIMIT
        and pygame.mixer.music.get_busy()
    ):
        print("[PARSER] Simulated boundary violation detected.")
        print("[LAB] Simulating control-flow compromise.")
        print("[LAB] Benign demonstration action: launching Calculator.")
        subprocess.Popen(["calc.exe"])
    else:
        print("[PARSER] Input accepted normally.")
        print("[LAB] No trigger action.")

    clock = pygame.time.Clock()

    while pygame.mixer.music.get_busy():
        clock.tick(10)

    pygame.mixer.quit()
    print("[PLAYER] Playback finished.")

if __name__ == "__main__":
    main()
