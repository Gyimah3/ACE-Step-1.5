import subprocess

import numpy as np
import torch


def load_audio_stereo(audio_path: str, target_sample_rate: int, max_duration: float):
    """Load audio, resample, convert to stereo, and truncate.

    Uses the system ffmpeg binary to decode audio so that torchaudio's
    torchcodec backend (required in torchaudio >=2.9) is not needed.
    ffmpeg is available on all major Linux/macOS/Windows server images.
    """
    cmd = [
        "ffmpeg", "-hide_banner", "-loglevel", "error",
        "-i", audio_path,
        "-f", "f32le",          # raw 32-bit float PCM
        "-acodec", "pcm_f32le",
        "-ar", str(target_sample_rate),
        "-ac", "2",             # stereo output
        "pipe:1",
    ]
    result = subprocess.run(cmd, capture_output=True)
    if result.returncode != 0:
        raise RuntimeError(
            f"ffmpeg failed for {audio_path}: {result.stderr.decode(errors='replace')}"
        )
    if not result.stdout:
        raise RuntimeError(f"ffmpeg produced no output for {audio_path}")

    audio_np = np.frombuffer(result.stdout, dtype=np.float32).copy()
    # ffmpeg outputs interleaved stereo: [L0, R0, L1, R1, ...]
    audio = torch.from_numpy(audio_np).reshape(-1, 2).T  # [2, samples]

    max_samples = int(max_duration * target_sample_rate)
    if audio.shape[1] > max_samples:
        audio = audio[:, :max_samples]

    return audio, target_sample_rate
