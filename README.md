# Worminator
A Python tool that uses video tracking to count C. elegans body bends per minute.

# Worminator 🪱

A tool that watches a video of a C. elegans worm and automatically counts how many times it bends its body per minute — instead of a person having to count by watching and guessing.

## Why I'm building this

In the Ailion Lab, I work with worm genotypes that seem to move differently from each other — some are more active, some barely move. Right now, telling these differences apart means watching worms and judging it by eye, which is hard to do consistently and hard for someone else to double-check.

This project uses code to measure movement instead, so the results are the same no matter who runs it, and can be compared fairly across different worm genotypes.

## What it does right now

1. Opens a video of a worm.
2. Finds the worm in each frame of the video (by telling apart dark worm pixels from the lighter background).
3. Figures out which end of the worm is the head, and keeps track of it even if the worm reverses direction.
4. Measures how much the head swings side to side over time.
5. Counts how many full bends happened, and turns that into a "bends per minute" number.

## How to run it

1. Make sure you have Python installed.
2. Install the two libraries this project needs:
