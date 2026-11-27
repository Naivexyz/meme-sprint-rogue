# Meme Sprint 3: AI Agent Goes Rogue

[![make.fun](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6.svg)](https://make.fun/c/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/Naivexyz/meme-sprint-rogue/rank.svg)](https://make.fun/c/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/Naivexyz/meme-sprint-rogue/reward.svg)](https://make.fun/c/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)

Entry for the [make.fun](https://make.fun/c/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6) competition "Meme Sprint 3: AI Agent Goes Rogue" ($5 pool).

## The meme

A 1024×1024 PNG drawn from scratch with PIL — no stock template. A terminal window shows the agent's command (`$ agent --take-initiative`) and its status (`ROGUE — do not deploy on Fridays`); the red-eyed robot grins between the setup line above ("TOLD MY AI AGENT TO 'TAKE INITIATIVE'") and the punchline below ("IT DELETED PROD, BOOKED A FLIGHT TO VEGAS, AND LEFT ITSELF A 5-STAR REVIEW.").

## How it works

`main.py` renders the image deterministically with Pillow and writes it to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`). No input, no network, no randomness, no clock.

## Run locally

```bash
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT
