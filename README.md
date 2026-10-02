# automated-body-bends-assay

A tool that watches a video of a *C. elegans* and automatically counts how many times it bends per minute — instead of a person counting by eye.

## Why

In the Ailion Lab, body bends assays are normally done by watching a worm and counting bends manually. This is subjective: different scientists count differently depending on what they consider a "full bend," and the same person can count differently between trials. This makes results hard to compare across people or across days.

This project replaces manual counting with a consistent, code-based measurement, so results don't depend on who's watching.

## What it does

1. Opens a video of a worm.
2. Separates the worm from the background in each frame.
3. Identifies the worm's head and tracks it frame to frame, even through reversals.
4. Measures how the head swings side to side over time.
5. Counts full bends and reports a bends-per-minute value.

## Setup

```bash
pip install opencv-python scipy
```

## Usage

1. Place your worm video in this folder.
2. Update the filename in `automated-body-bends-assay.py` to match your video.
3. Run:
   ```bash
   python automated-body-bends-assay.py
   ```
4. Output:
   ```
   Bends per minute: 24.3
   ```

## Status

Core pipeline works: detects the worm, tracks its head through reversals, and extracts a bend-rate signal. Tested on one video — automated count (24.5 bends) is close to, but not identical to, a manual by-eye count (~20 bends) over the same clip. Possible sources of the gap: subtle bends that are hard to catch by eye but visible in the extracted signal, or oversensitivity to small wiggles. Next: validate against more videos and more genotypes.

## Background

Built from undergraduate research in the Ailion Lab on *C. elegans* genotypes affecting dense-core vesicle biogenesis (*rab-2*) and neuropeptide processing (*egl-3*, *egl-21*) — genes that affect neuron signaling and may alter movement.
