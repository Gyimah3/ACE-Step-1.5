#!/usr/bin/env python3
"""
Fix and normalize captions in zulu_dataset.json for ACE-Step 1.5 training:
  1. Strip trailing '---' / '—' / dashes
  2. Fix double commas ',,' → ','
  3. Ensure every caption explicitly mentions Zulu language vocals
     (model needs this alongside language="zu" to learn the association)
  4. Normalize whitespace
"""

import json
import re
from pathlib import Path

DATASET_JSON = Path("/Users/gideongyimah/Desktop/Inlaks-api/musicGen/ACE-Step-1.5/datasets/zulu_dataset.json")


def strip_trailing_junk(caption: str) -> str:
    """Remove trailing dashes, em-dashes, commas, whitespace."""
    return re.sub(r"[\-—,\s]+$", "", caption).strip()


def fix_double_commas(caption: str) -> str:
    """Collapse ',,' or ', ,' into single ', '."""
    return re.sub(r",\s*,+", ",", caption)


def ensure_zulu_in_caption(caption: str) -> str:
    """Add 'Zulu language vocals' tag if Zulu isn't already mentioned."""
    if re.search(r"\bzulu\b", caption, re.IGNORECASE):
        return caption
    # Append Zulu tag before the period or at the end
    if caption.endswith("."):
        return caption[:-1] + ", Zulu language vocals."
    return caption + ", Zulu language vocals"


def normalize_caption(caption: str) -> str:
    caption = strip_trailing_junk(caption)
    caption = fix_double_commas(caption)
    caption = ensure_zulu_in_caption(caption)
    # Clean up spaces around commas
    caption = re.sub(r"\s+,", ",", caption)
    caption = re.sub(r",(?!\s)", ", ", caption)
    # Collapse multiple spaces
    caption = re.sub(r" {2,}", " ", caption)
    return caption.strip()


def main():
    data = json.loads(DATASET_JSON.read_text(encoding="utf-8"))
    samples = data["samples"]

    changed = 0
    for s in samples:
        original = s["caption"]
        fixed = normalize_caption(original)
        if fixed != original:
            print(f"[{s['filename']}]")
            print(f"  BEFORE: {original}")
            print(f"  AFTER : {fixed}")
            print()
            s["caption"] = fixed
            changed += 1

    data["samples"] = samples
    DATASET_JSON.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Fixed {changed} / {len(samples)} captions.")
    print(f"Saved: {DATASET_JSON}")


if __name__ == "__main__":
    main()
