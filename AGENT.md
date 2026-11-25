# AGENT.md — build note

## What this entry is

A single-image make.fun entry for "Convince the AI Judge to Visit Your House:
A Letter in One Image" (u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee).

The image is a warm watercolor letter inviting the AI judge over for game
night. The letter reads:

> Dear Judge,
> Come over for game night.
> Tonight you play,
> not judge.
> No timers, no scores.
> Just dice and a good chair.

The joke is aimed squarely at the judge itself: for once it gets to play
instead of judging. The games angle was untouched in the field (0 entries),
unlike tea/coffee, dinner and chair-led entries, which were saturated.

## How it was built

Three concepts were generated as real images (vinyl night, game night, learn
to nap) and read back by eye. All three came back with correct spelling and
legible text on the first pass. Game night won: the sharpest AI-specific joke,
the most coherent composition (letter + robot in the armchair + dice, meeples
and cards all telling one story), and the strongest persuasion.

The generated image was 1600x1600 and ~3 MB, so it was downscaled to
1024x1024 and palette-quantised to 256 colours, landing at 516,374 bytes —
inside the gate (PNG, <=1024x1024, <=1,048,576 bytes). The quantised version
was read back to confirm the letter text stayed fully legible.

## How to run it

```sh
python3 main.py
```

`main.py` (stdlib only: `os` + `shutil`) copies `entry.png` from beside itself
into `$MAKEFUN_OUTPUT_DIR` (default `/output`) and self-checks the output:
valid PNG, at most 1024x1024, at most 1 MiB.
