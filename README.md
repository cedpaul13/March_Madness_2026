# March Madness 2026: Predictive Analytics & Bracket Strategy

I built CFA Fusion to fill out my 2026 NCAA brackets. This project compares those predictions with the tournament results.

**The full story, results and visuals live [here](https://cedpaul13.github.io/March_Madness_2026/).**

The site is available in English and French, with light and dark themes. Results
are summarized up front; expert comparisons, game stories, players and highlights
expand on demand.

The static site lives in [`docs/index.html`](./docs/index.html), with its product
design layer in [`docs/design.css`](./docs/design.css). Open the HTML directly to
preview it (no build required). To publish the site and logo to GitHub Pages, run
`./scripts/deploy_site.sh`.
The NCAA mark in the header is sourced from [NCAA.com](https://www.ncaa.com/favicon.svg).

### Site quality checks

Run the focused browser-fallback and deployment regression tests with Node.js
and Git (deployment tests use disposable local repositories, never GitHub):

```bash
node --test scripts/*.test.mjs
```

Before publishing, check both languages and themes at mobile, tablet and desktop
widths (including 700/701px and 760/768px breakpoints), 200% text sizing, keyboard
navigation, expanded tables, forced colors, reduced motion, printing collapsed
analyses, and navigation/charts with JavaScript disabled. Automated
accessibility checks do not replace manual contrast and screen-reader testing.
Video playback requires an HTTP server and third-party availability; direct-file
previews open YouTube links.

Keep the HTML and CSS under source control alongside the application code.
The deployment script
publishes them to `gh-pages` and rejects concurrent updates.

Results at a glance:

* One men's semifinal predicted correctly, including the matchup and winner
* All four women's Final Four teams named in advance
* A 4-1 record on five first-round picks
* Neither eventual champion was my pre-tournament pick

---

## Dig deeper

* [Post-mortem: the full technical accounting](./POST_MORTEM.md)
* [Methodology paper (PDF)](./article/CFA_article.pdf)
* [Men's official bracket (PDF)](./brackets/M_bracket.pdf) · [Women's official bracket (PDF)](./brackets/W_bracket.pdf)
* [Kaggle competition: March Machine Learning Mania 2026](https://www.kaggle.com/c/march-machine-learning-mania-2026)

---

## Run the pipeline

This repository holds the code behind the model (called CFA Fusion): data loading, feature engineering, XGBoost training, geospatial and momentum signals, and Monte Carlo bracket simulation.

**1. Create the environment**

```bash
conda env create -f environment.yml
conda activate march_madness_2026
```

**2. Configure the Kaggle API**

```bash
export KAGGLE_API_TOKEN=your_api_key
```

Add that line to `~/.zshrc` for it to persist across sessions.
