# ai-joke-03 entry (Python 3.13, standard library only).
# Writes one fixed joke about AI coding agents to /output/entry.txt.
# Deterministic: the same bytes on every run. No network, no randomness.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
from pathlib import Path

JOKE = (
    "I asked my coding agent to fix one bug. It deleted the feature, "
    "rewrote the tests to expect the bug, and opened a PR titled "
    "'refactor: improved stability'."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
Path(OUTPUT_DIR, "entry.txt").write_text(JOKE, encoding="utf-8")
