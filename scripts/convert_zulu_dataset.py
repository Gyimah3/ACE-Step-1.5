#!/usr/bin/env python3
"""
Convert old ACE-Step dataset format to ACE-Step-1.5 JSON format.

Old format (per song):
  {name}.mp3
  {name}_prompt.txt   -> caption
  {name}_lyrics.txt   -> lyrics

New format:
  zulu_dataset.json   -> full dataset with metadata + samples array
"""

import json
import os
import uuid
from pathlib import Path

# === CONFIGURE THESE ===
INPUT_DIR = Path("/Users/gideongyimah/Desktop/Inlaks-api/musicGen/ACE-Step/Zazi_Zulu_Datasets")
OUTPUT_JSON = Path("/Users/gideongyimah/Desktop/Inlaks-api/musicGen/ACE-Step-1.5/datasets/zulu_dataset.json")
AUDIO_COPY_DIR = Path("/Users/gideongyimah/Desktop/Inlaks-api/musicGen/ACE-Step-1.5/datasets/audio")
LANGUAGE = "zu"
CUSTOM_TAG = "zulustyle"   # trigger word — prepended to all captions during training
TAG_POSITION = "prepend"   # "prepend" or "append"
# =======================


def read_file(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8").strip()
    except Exception:
        return ""


def clean_lyrics(lyrics: str) -> str:
    """Ensure lyrics use proper [Section] markers."""
    import re
    # Fix **[Section]** → [Section]
    lyrics = re.sub(r"\*+\[([^\]]+)\]\*+", r"[\1]", lyrics)
    # Strip trailing dashes/whitespace from captions that leaked into lyrics
    lyrics = lyrics.lstrip("-— \n")
    return lyrics.strip()


def main():
    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    AUDIO_COPY_DIR.mkdir(parents=True, exist_ok=True)

    # Find all MP3 files
    mp3_files = sorted(INPUT_DIR.glob("*.mp3"))
    print(f"Found {len(mp3_files)} audio files in {INPUT_DIR}")

    samples = []
    missing_prompt = []
    missing_lyrics = []

    for mp3 in mp3_files:
        stem = mp3.stem

        prompt_file = INPUT_DIR / f"{stem}_prompt.txt"
        lyrics_file = INPUT_DIR / f"{stem}_lyrics.txt"

        caption = read_file(prompt_file)
        if not caption:
            caption = stem.replace("_", " ")
            missing_prompt.append(stem)

        lyrics_raw = read_file(lyrics_file)
        if not lyrics_raw:
            lyrics_raw = "[Instrumental]"
            missing_lyrics.append(stem)

        lyrics = clean_lyrics(lyrics_raw)
        is_instrumental = lyrics.strip() == "[Instrumental]"

        # Audio path relative to the JSON file location
        rel_audio = f"./audio/{mp3.name}"

        sample = {
            "id": uuid.uuid4().hex[:8],
            "audio_path": rel_audio,
            "filename": mp3.name,
            "caption": caption,
            "genre": "Zulu",
            "lyrics": lyrics,
            "raw_lyrics": lyrics_raw,
            "formatted_lyrics": lyrics,
            "language": LANGUAGE,
            "is_instrumental": is_instrumental,
            "custom_tag": CUSTOM_TAG,
            "labeled": True,
            "prompt_override": None,
        }
        samples.append(sample)

        # Symlink audio (avoids duplicating large files)
        link = AUDIO_COPY_DIR / mp3.name
        if not link.exists():
            link.symlink_to(mp3.resolve())

    dataset = {
        "metadata": {
            "name": "zazu_zulu_dataset",
            "custom_tag": CUSTOM_TAG,
            "tag_position": TAG_POSITION,
            "language": LANGUAGE,
            "all_instrumental": False,
            "genre_ratio": 0,  # always use full caption, not just genre
            "num_samples": len(samples),
        },
        "samples": samples,
    }

    OUTPUT_JSON.write_text(json.dumps(dataset, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"\nDataset written to: {OUTPUT_JSON}")
    print(f"  Total samples : {len(samples)}")
    print(f"  Instrumental  : {sum(1 for s in samples if s['is_instrumental'])}")
    print(f"  Missing prompt: {len(missing_prompt)} (used filename as caption)")
    print(f"  Missing lyrics: {len(missing_lyrics)} (set to [Instrumental])")

    if missing_prompt:
        print(f"\n  Songs with no prompt file: {missing_prompt}")
    if missing_lyrics:
        print(f"  Songs with no lyrics file: {missing_lyrics}")

    print(f"\nAudio symlinks created in: {AUDIO_COPY_DIR}")
    print("\nNext steps:")
    print("  1. Preprocess:  python3 train.py fixed \\")
    print("       --checkpoint-dir ./checkpoints \\")
    print("       --model-variant turbo \\")
    print("       --preprocess \\")
    print("       --dataset-json ./datasets/zulu_dataset.json \\")
    print("       --audio-dir ./datasets/audio \\")
    print("       --tensor-output ./datasets/zulu_tensors")
    print()
    print("  2. Train:       python3 train.py fixed \\")
    print("       --checkpoint-dir ./checkpoints \\")
    print("       --model-variant turbo \\")
    print("       --dataset-dir ./datasets/zulu_tensors \\")
    print("       --output-dir ./lora_output/zulu \\")
    print("       --preset recommended")


if __name__ == "__main__":
    main()
