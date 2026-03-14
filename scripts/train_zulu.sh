#!/usr/bin/env bash
# Zulu LoRA finetuning for ACE-Step-1.5
# Run from: /Users/gideongyimah/Desktop/Inlaks-api/musicGen/ACE-Step-1.5
#
# Usage:
#   bash scripts/train_zulu.sh           # full run (preprocess + train)
#   bash scripts/train_zulu.sh train     # training only (skip preprocess)

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$ROOT_DIR"

CHECKPOINT_DIR="./checkpoints"
DATASET_JSON="./datasets/zulu_dataset.json"
AUDIO_DIR="./datasets/audio"
TENSOR_DIR="./datasets/zulu_tensors"
OUTPUT_DIR="./lora_output/zulu"
PRESET="vram_24gb_plus"        # RTX 6000 Ada 48GB
MODEL_VARIANT="turbo"          # or "default"

# Training hyperparameters (63 songs → 500 epochs = ~16,000 steps)
BATCH_SIZE=2
GRAD_ACCUM=4
EPOCHS=500
SAVE_EVERY=50

# ── Step 0: Convert dataset if JSON doesn't exist yet ──────────────────────
if [ ! -f "$DATASET_JSON" ]; then
    echo "[1/3] Converting dataset to ACE-Step-1.5 JSON format..."
    python3 scripts/convert_zulu_dataset.py
else
    echo "[1/3] Dataset JSON found, skipping conversion."
fi

# ── Step 1: Preprocess (unless 'train' arg passed) ─────────────────────────
if [ "${1}" != "train" ]; then
    echo "[2/3] Preprocessing audio → tensors (this may take a while)..."
    python3 train.py fixed \
        --checkpoint-dir "$CHECKPOINT_DIR" \
        --model-variant "$MODEL_VARIANT" \
        --preprocess \
        --dataset-json "$DATASET_JSON" \
        --audio-dir "$AUDIO_DIR" \
        --tensor-output "$TENSOR_DIR"
else
    echo "[2/3] Skipping preprocessing (using existing tensors)."
fi

# ── Step 2: Train ──────────────────────────────────────────────────────────
echo "[3/3] Starting LoRA training..."
python3 train.py fixed \
    --checkpoint-dir "$CHECKPOINT_DIR" \
    --model-variant "$MODEL_VARIANT" \
    --dataset-dir "$TENSOR_DIR" \
    --output-dir "$OUTPUT_DIR" \
    --preset "$PRESET" \
    --batch-size "$BATCH_SIZE" \
    --gradient-accumulation "$GRAD_ACCUM" \
    --epochs "$EPOCHS" \
    --save-every "$SAVE_EVERY"

echo ""
echo "Done! LoRA weights saved to: $OUTPUT_DIR"
