# The World Today — 18 November 2026

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/Kyamii21/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/Kyamii21/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

A one-image newspaper front page summing up Wednesday 18 November 2026's world news — built to stay readable even at ~300px wide: 72px lead headline, nothing below 26px.

## The five stories

1. **APEC opens in Shenzhen** — Xi Jinping opens the APEC summit in Shenzhen and greets Trump on the tarmac with a hug; Xi and Putin meet first, denouncing protectionism and Western sanctions. The first Trump–Xi–Putin trilateral summit follows on Thursday 19 November, with nuclear disarmament, the US–Iran war and Ukraine on the agenda.
2. **US loses measles-free status** — PAHO revokes the US measles-elimination status after 26 years: 5,400+ cases and 10 deaths in 2026, the most in 30+ years. Mexico and Bolivia also lose the status.
3. **Democrats flip Alaska** — Mary Peltola defeats Dan Sullivan in the Alaska Senate race, widening the Democrats' Senate majority.
4. **Kerch span destroyed** — Ukraine destroys a span of the Kerch Bridge linking Russia and Crimea, as the Gulf war keeps heating up around Hormuz.
5. **Also in brief** — France strikes over pay and the cost of living (146,000 march, police count / 500,000+, union count); Waymo halts driverless taxis on all US freeways after California's ban; Cyclone Akvan heads for Andhra Pradesh, India.

Sources: Reuters, AP, BBC, NY Post, France 24.

## Run

```sh
python3 main.py
```

Writes the 1024x1024 PNG to `/output/entry.png` (standard library only; validates the PNG magic bytes and dimensions and prints the SHA-256). `DEST_DIR` overrides the output directory for local testing.

## License

MIT — see [LICENSE](LICENSE).
