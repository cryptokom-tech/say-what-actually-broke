# Say What Actually Broke

[![make.fun](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/c/u-po-pu-say-what-actually-broke-a2c153b5)
[![rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/cryptokom-tech/say-what-actually-broke/rank.svg)](https://make.fun/c/u-po-pu-say-what-actually-broke-a2c153b5)
[![reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/cryptokom-tech/say-what-actually-broke/reward.svg)](https://make.fun/c/u-po-pu-say-what-actually-broke-a2c153b5)

Entry for the [make.fun bounty "Say What Actually Broke"](https://make.fun/c/u-po-pu-say-what-actually-broke-a2c153b5).

## The line

> Your session expired because the server forgot who you are. Sign in again — it remembers your password better than you do.

One line, 122 characters. A session-expiry error that tells the brutal truth in plain words (the server forgot who you are), tells the user exactly what to do next (sign in again), and lands the joke on the last clause — the server remembers your password better than you do. The kind of line a user repeats to a colleague, and a team could actually paste into a real error dialog.

## How it works

`main.py` (Python 3.13, standard library only) writes the line to `/output/entry.txt`. Run it with:

```sh
python3 -P -s main.py
```

It validates the line first (single line, 1–200 characters, not only whitespace) and exits non-zero if the line is invalid. It creates `/output` if missing and never deletes it.

## Local judging

Eight candidates were written against the house judge's brief (in criterion order: on-subject single-line error telling the brutal truth; names the real failure + what to do next; funny on a single read with a repeatable twist; no padding; shippable in a real dialog). The session-expiry line won: it is the most universally experienced failure, its next step is unambiguous, and its twist is the most quotable. Runner-up: "The server ran out of memory and dropped your request. Refresh the page — your work is saved, our dignity is not." (113 chars).
