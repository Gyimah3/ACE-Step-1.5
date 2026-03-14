#!/usr/bin/env python3
"""
Merge BPM + key metadata from key_bpm CSV into zulu_dataset.json.
Also sets timesignature to "4" (4/4) for all songs as default.
"""

import csv
import json
from pathlib import Path

CSV_PATH  = Path("/Users/gideongyimah/Downloads/key_bpm (1).csv")
JSON_PATH = Path("/Users/gideongyimah/Desktop/Inlaks-api/musicGen/ACE-Step-1.5/datasets/zulu_dataset.json")


def load_csv(path: Path) -> dict:
    """Return {filename: {bpm, keyscale}} from CSV.

    Some song titles contain unquoted commas which breaks DictReader.
    Parse by splitting from the right: last 3 fields are always BPM, Key, Camelot.
    First field is always the filename.
    """
    result = {}
    with open(path, encoding="utf-8-sig") as f:
        lines = f.read().splitlines()

    for line in lines[1:]:   # skip header
        if not line.strip():
            continue
        parts = line.split(",")
        filename = parts[0].strip()
        # BPM, Key, Camelot are the last 3 — Key may contain no value
        camelot  = parts[-1].strip()
        key_raw  = parts[-2].strip()
        bpm_raw  = parts[-3].strip()
        if filename and bpm_raw.isdigit():
            result[filename] = {
                "bpm":      int(bpm_raw),
                "keyscale": key_raw,
            }
    return result


def main():
    csv_data  = load_csv(CSV_PATH)
    data      = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    samples   = data["samples"]

    updated = 0
    missing = []

    for s in samples:
        fname = s["filename"]
        if fname in csv_data:
            s["bpm"]           = csv_data[fname]["bpm"]
            s["keyscale"]      = csv_data[fname]["keyscale"]
            s["timesignature"] = "4"   # 4/4 default — not in CSV
            updated += 1
        else:
            missing.append(fname)

    data["samples"] = samples
    JSON_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"Updated {updated} / {len(samples)} samples with BPM + key.")
    if missing:
        print(f"No CSV entry found for: {missing}")
    else:
        print("All 63 samples have BPM + key.\n")

    # Summary
    print("Sample check:")
    for s in samples[:5]:
        print(f"  {s['filename']:40s}  BPM={s.get('bpm','?'):>3}  Key={s.get('keyscale','?')}")


if __name__ == "__main__":
    main()
