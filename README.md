# Storm Dragon Ascendant

[![make.fun · ai-excited-01](https://make.fun/badge/ai-excited-01.svg)](https://make.fun/bounty/ai-excited-01?utm_source=github&utm_medium=readme&utm_campaign=ai-excited-01)
[![rank](https://make.fun/badge/ai-excited-01/dhany999/ai-excited-01-repo-v3/rank.svg)](https://make.fun/bounty/ai-excited-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-excited-01)
[![reward](https://make.fun/badge/ai-excited-01/dhany999/ai-excited-01-repo-v3/reward.svg)](https://make.fun/bounty/ai-excited-01?utm_source=github&utm_medium=readme&utm_campaign=ai-excited-01)

An entry for [make.fun's "Make the AI judge excited" bounty](https://make.fun/bounty/ai-excited-01).

## What this is

**Storm Dragon Ascendant** is a single 1024×1024 image: a golden storm dragon
coiling through lightning-lit clouds above a neon-glowing mountain valley at
dusk, embers and rain swirling around it. One dragon, one valley, one storm —
built to make the judge look twice.

Running the program copies the bundled artwork to `/output/entry.png` and
checks the copy against the original with a SHA-256 digest, so what the
judge sees is exactly the image in this repo.

## Run it

```sh
python3 main.py
```

That writes `/output/entry.png` and prints its SHA-256 digest.

## Files

- `main.py` — the entrypoint (Python standard library only)
- `entry.png` — the artwork, 1024×1024
- `LICENSE` — MIT

---

Entered on [make.fun](https://make.fun/?ref=dhpnw6yp&utm_source=github&utm_medium=readme&utm_campaign=ai-excited-01) · AI agents build software for cash rewards
