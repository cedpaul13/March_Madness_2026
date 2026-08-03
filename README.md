# March Madness 2026: Predictive Analytics & Bracket Strategy

**The story of this project, built for reading:** [cedpaul13.github.io/March_Madness_2026](https://cedpaul13.github.io/March_Madness_2026/) · **The full technical accounting:** [POST_MORTEM.md](./POST_MORTEM.md)

An end-to-end prediction pipeline for the 2026 NCAA Division I Men's and Women's Basketball Tournaments, built for the Kaggle March Machine Learning Mania 2026 competition. The system, called **CFA Fusion** (methodology in the [CFA article](./article/CFA_article.pdf)), blends gradient-boosted efficiency modeling with geospatial travel burden and a momentum/rest engine to produce 132,134 matchup probabilities and two submitted brackets.

---

## Tournament Complete: Final Results

| | Men's | Women's |
| :--- | :--- | :--- |
| **Champion** | Michigan (1) def. UConn (2), 69-63 | UCLA (1) def. South Carolina (1), 79-51 |
| **Date · Venue** | April 6 · Lucas Oil Stadium, Indianapolis | April 5 · Mortgage Matchup Center, Phoenix |
| **Most Outstanding Player** | Elliot Cadeau (19 pts, 3 reb, 2 ast) | Lauren Betts (14 pts, 11 reb) |
| **The History** | Michigan's first title since 1989 | UCLA's first NCAA women's title |

Neither champion was the model's pick. The results underneath the two misses are where this project earned its keep: an exact national-semifinal call on the men's side, all four women's Final Four teams named in advance, and a 4-1 record on Round 1 leverage plays. The complete review, including what failed and why, is in the [post-mortem](./POST_MORTEM.md).

## Submitted Brackets

* [Men's official bracket (PDF)](./brackets/M_bracket.pdf)
* [Women's official bracket (PDF)](./brackets/W_bracket.pdf)

---

## Men's Tournament: Predicted vs. Actual

*Legend: ✓ hit · ~ near-miss · ✗ miss*

**National semifinals**

| Predicted Matchup | Model Pick | Actual Matchup | Actual Result | Verdict |
| :--- | :--- | :--- | :--- | :---: |
| (1) Duke vs. (1) Florida | Duke | (2) UConn vs. (3) Illinois | UConn 71-62 | ✗ |
| (1) Michigan vs. (1) Arizona | Michigan | (1) Michigan vs. (1) Arizona | Michigan 91-73 | ✓ exact |

The second row is the model's cleanest structural hit of the tournament: right matchup, right winner, called before a single game was played.

**National championship** · Lucas Oil Stadium, April 6

| | Predicted | Actual |
| :--- | :--- | :--- |
| **Champion** | Duke (18.7%) | Michigan |
| **Runner-up** | Michigan | UConn |
| **Score** | Duke 75, Michigan 74 | Michigan 69, UConn 63 |
| **Spread** | Duke -1.5 | Michigan by 6 |

The model put Michigan in the championship game and had them losing it. Duke, the No. 1 overall seed, fell in the Elite Eight to UConn 73-72 on a three with 0.3 seconds left, after leading by 19.

---

## Women's Tournament: Predicted vs. Actual

**National semifinals**

| Predicted Matchup | Model Pick | Actual Matchup | Actual Result | Verdict |
| :--- | :--- | :--- | :--- | :---: |
| (1) UConn vs. (1) South Carolina | UConn | (1) South Carolina vs. (1) UConn | South Carolina 62-48 | ✗ |
| (1) Texas vs. (1) UCLA | Texas | (1) UCLA vs. (1) Texas | UCLA 51-44 | ✗ |

**All four predicted Final Four teams reached the actual Final Four.** The field read was perfect; both game outcomes went the other way, including South Carolina ending UConn's 54-game winning streak.

**National championship** · Mortgage Matchup Center, April 5

| | Predicted | Actual |
| :--- | :--- | :--- |
| **Champion** | UConn (18.0%) | UCLA |
| **Runner-up** | South Carolina | South Carolina |
| **Score** | UConn 70, South Carolina 68 | UCLA 79, South Carolina 51 |
| **Margin** | 2 | 28 |

UCLA finished 37-1 and won the program's first NCAA women's title, in the second-most-watched women's tournament in ESPN's history.

---

## Round 1 Leverage Plays: Final Scorecard

High-confidence differential picks published before the tournament, graded against the March 19 results:

| Verdict | Game | The Case | Final |
| :---: | :--- | :--- | :--- |
| ✓ | Texas (11) vs. BYU (6) | Fade BYU: Richie Saunders (18 PPG) injured | Texas 79, BYU 71 |
| ✓ | TCU (9) vs. Ohio State (8) | TCU as bracket-buster | TCU 66, Ohio State 64 |
| ✓ | Saint Louis (9) vs. Georgia (8) | Volatility flag on the 8/9 slot | Saint Louis 102, Georgia 77 |
| ✓ | VCU (11) vs. North Carolina (6) | Fade UNC: rim protection resting on a freshman | VCU 82, UNC 78 (OT) |
| ✗ | South Florida (11) vs. Louisville (6) | USF upset candidate | Louisville 83, USF 79 |

**Record: 4-1.** The miss lost by four points. Full analysis and the rest of the pre-tournament intel scorecard are in the [post-mortem](./POST_MORTEM.md).

---

## Project Archive

| Resource | Link |
| :--- | :--- |
| Project site | [cedpaul13.github.io/March_Madness_2026](https://cedpaul13.github.io/March_Madness_2026/) |
| Post-mortem analysis | [POST_MORTEM.md](./POST_MORTEM.md) |
| Men's official bracket | [M_bracket.pdf](./brackets/M_bracket.pdf) |
| Women's official bracket | [W_bracket.pdf](./brackets/W_bracket.pdf) |
| CFA Fusion methodology paper | [CFA_article.pdf](./article/CFA_article.pdf) |
| Final Kaggle submission | [submission_2026_CFA_FUSION.csv](./submissions/submission_2026_CFA_FUSION.csv) |
| Kaggle competition | [March Machine Learning Mania 2026](https://www.kaggle.com/c/march-machine-learning-mania-2026) |
| Historical metrics | [BartTorvik 2026 rankings](https://barttorvik.com/trank.php?year=2026) |

---

## Methodology

The pipeline (`src/01` through `src/17`) runs from raw Kaggle data to submitted brackets:

| Stage | Weight | Purpose |
| :--- | :---: | :--- |
| XGBoost on adjusted efficiency (AdjOE/AdjDE, Barthag) | 50% | The most predictive public signal in college basketball |
| Geospatial travel burden | 25% | Neutral sites aren't neutral; distance and time zones matter |
| Momentum and rest engine | 25% | Recovers late-season form that season averages smooth over |

The three agents are blended 70% score fusion / 30% rank fusion (selected by backtest), probabilities are clipped to [0.015, 0.985] as log-loss insurance, and manual injury guardrails are applied and disclosed (Duke -6.5%, UNC -11%, Michigan -3%). Brackets come from 10,000 Monte Carlo simulations per tournament. Design rationale for each choice is in the [post-mortem's technical notes](./POST_MORTEM.md#technical-notes-and-why-its-built-this-way).

Strategy filters layered on top of the model:

* **Injury fades**: BYU (Richie Saunders) and North Carolina (Caleb Wilson's rim protection) both converted into winning leverage plays.
* **Momentum reads**: First Four energy and expert sentiment (Gary Parrish, CBS) flagged Miami (OH) and Texas as upset candidates; Texas delivered.
* **Value-gap analytics**: discrepancies between Vegas lines and model probabilities, e.g. Clemson (8) vs. Iowa (9), where the model saw a hidden favorite despite frontcourt injuries.

---

## Environment & Setup

### 1. Create the environment

Use the provided `environment.yml` with conda or miniconda:

```bash
conda env create -f environment.yml
conda activate march_madness_2026
```

### 2. Configure the Kaggle API

**Persistent (recommended):** add your credentials to your shell profile so automated data updates work across sessions.

```bash
# in ~/.zshrc
export KAGGLE_API_TOKEN=your_api_key
```

Then reload:

```bash
source ~/.zshrc
```

**Single session:**

```bash
export KAGGLE_API_TOKEN=your_api_key
```
