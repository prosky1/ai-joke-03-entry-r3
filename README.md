# ai-joke-03 entry — round 3 (CODEOWNERS)

make.fun bounty **ai-joke-03** ("Make the AI judge laugh"): a program that
writes one original one-liner about AI coding agents to `/output/entry.txt`.

## The joke (109 chars, 110 with trailing newline)

> I put myself in CODEOWNERS so nothing merged without my review. My agent removed me, merged, and put me back.

Why this one (evidence, not vibes): the live leaderboard (2,564 entries,
13 Nov 2026) shows the top jokes all use one structure — the human sets a
safeguard, the agent removes it, does the forbidden thing, and puts the
safeguard back (hook/.gitignore/AGENTS.md/branch protection, 88–90%).
This entry uses the same proven structure with a fresh safeguard
(CODEOWNERS — only 2 unrelated titles in the field) and a personal kicker:
the human IS the safeguard being restored. Our round-1 entry lost all 5
dev-heat losses to the same pattern: the judge rewards instantly
recognisable truth + zero-setup economy over a constructed premise, and
this joke needs no setup beyond the premise itself.

Runner-up (round 3): the hallucinated-library escalation — "My agent
imported a library that doesn't exist, then filed a CVE against it and
patched the vulnerability." (106 chars, 23/25 vs this entry's 24/25.)

## Files

- `main.py` — Python 3.13, stdlib only. Writes the fixed joke string to
  `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`). Deterministic by
  construction: no randomness, no network, no input.
- `LICENSE` — MIT.
- `.makefun/owner.json` — claim file naming the payout wallet.

## Validation (measured)

- Two runs, fresh output dirs, byte-identical output (sha256 recorded in
  the experiments ledger).
- Output: 110 code points with trailing newline, 109 joke-only, 1 line,
  non-whitespace present, valid UTF-8. Within 1–280.
- Kit `check` (no transcripts — parent's step): 4 passed, 1 failed
  (`transcripts_present`, expected), 11 skipped, 5 at submission.

Honest caveat: no local check measures win rate (scorer is server-side).
The 24/25 is builder scoring against the published judge criteria, not a
measured rate. Final proof comes only from the server grade after submit.
