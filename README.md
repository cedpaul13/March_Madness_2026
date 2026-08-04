# March Madness 2026: Predictive Analytics & Bracket Strategy

Every March, millions of people fill out a bracket. I built a model to fill out mine, then spent three weeks watching the tournament argue with it.

**The full story, results and visuals live [here](https://cedpaul13.github.io/March_Madness_2026/).**

The site is available in English and French.

Why it's worth the click:

* An exact Final Four semifinal call, matchup and winner, made before a single game tipped off
* All four women's Final Four teams named in advance
* A 4-1 record on Round 1 leverage plays
* Two champions the model never saw coming, and an honest account of why

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
