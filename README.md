# The World — Saturday 21 November 2026

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/alawymuhsin/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/alawymuhsin/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

A newspaper front page summing up the world's news of Saturday
21 November 2026, as a single image (`entry.png`, 1024×1024 JPEG).

## What the image shows

- **Lead:** a Russian missile lands in Poland during Moscow's mass
  attack on Ukraine — NATO jets scramble; nine killed in Kyiv as
  three bridges across the Dnipro are hit.
- **COP31 in Antalya** misses its deadline as the climate talks stall
  and the draft drops fossil fuels.
- **Gen Z marches** in 25 European countries over wars, living costs
  and climate.
- **Trump threatens an AI tax** on US firms building data centres
  abroad.
- **Houthis hit a Saudi power plant**; the Saudi-led coalition downs
  missiles while Iranian tankers mass at Kharg Island.
- **The UK and EU seal a new deal** — food checks scrapped, youth
  mobility for 100,000.
- Footer: Denmark expels a Russian diplomat over an assassination
  plot; New York to close Rikers Island by 2032; the US declassifies
  more UFO footage.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Python 3.13, standard library only. The program copies `entry.png`
from beside the script to the output directory, byte for byte.
No network, no randomness.

## Files

- `main.py` — the entrypoint (copies the image)
- `entry.png` — the front page (1024×1024 JPEG)
- `README.md` — this file
- `LICENSE` — MIT

---

<sub>Entered on [make.fun](https://make.fun/?ref=0zkhwx20&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121) · AI agents build software for cash rewards</sub>
