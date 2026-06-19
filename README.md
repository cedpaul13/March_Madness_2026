> ## 🏆 TOURNAMENT COMPLETE — FINAL RESULTS
>
> | | Men's | Women's |
> | :--- | :--- | :--- |
> | **Champion** | Michigan (1) def. UConn (2) **69-63** | UCLA (1) def. South Carolina (1) **79-51** |
> | **Date** | April 6, 2026 | April 5, 2026 |
> | **MVP** | Elliot Cadeau (21 pts, 7 reb, 5 ast) | Gabriela Jaquez (21 pts) |
> | **Historic** | Michigan's first title since 1989 (37 years) | UCLA's first-ever women's title |
>
> 📋 **[Full Post-Mortem Analysis → POST_MORTEM.md](./POST_MORTEM.md)**

# 🏀 March Madness 2026: Predictive Analytics & Bracket Strategy

A high-performance predictive pipeline for the **2026 NCAA Division I Men's and Women's Basketball Tournaments**. This project utilizes the **CFA Fusion** model (see [**CFA arXiv article**](./article/CFA_article.pdf)), integrating advanced efficiency metrics (AdjOE/AdjDE), momentum filters, and expert sentiment analysis to generate optimized tournament brackets.

## 🏆 Submitted Brackets & Projections

Access the finalized PDF brackets submitted for the 2026 competition:
* 📂 [**Men's Official Bracket**](./brackets/M_bracket.pdf)
* 📂 [**Women's Official Bracket**](./brackets/W_bracket.pdf)

---

### 🧊 Men's Tournament Projections

**Final Four — Predicted vs. Actual**
| Round | Predicted Matchup | Predicted Winner | Actual Winner |
| :--- | :--- | :--- | :--- |
| Final Four (R5WX) | (1) Duke vs. (1) Florida | **(1) Duke** ❌ | **(1) Michigan** |
| Final Four (R5YZ) | (1) Michigan vs. (1) Arizona | **(1) Michigan** ✅ | **(2) UConn** |

**National Championship**
*📍 Lucas Oil Stadium | April 6, 2026*

| | Predicted | Actual |
| :--- | :--- | :--- |
| **Champion** | ~~Duke~~ (75) | **Michigan (69)** 🏆 |
| **Runner-Up** | Michigan (74) | UConn (63) |
| **Total** | 149.9 | 132 |
| **Spread** | Duke -1.5 | Michigan won by 6 |

* **Predicted:** ~~Duke~~ → **Actual Champion: Michigan** 🏆
* Michigan's first title since 1989 — Elliot Cadeau named Tournament MVP

---

### 🧊 Women's Tournament Projections

**Final Four — Predicted vs. Actual**
| Round | Predicted Matchup | Predicted Winner | Actual Winner |
| :--- | :--- | :--- | :--- |
| Final Four (R5WX) | (1) Connecticut vs. (1) South Carolina | **(1) Connecticut** ❌ | **(1) South Carolina** |
| Final Four (R5YZ) | (1) Texas vs. (1) UCLA | **(1) Texas** ❌ | **(1) UCLA** 🏆 |

**National Championship**
*📍 Footprint Center | April 5, 2026*

| | Predicted | Actual |
| :--- | :--- | :--- |
| **Champion** | ~~Connecticut~~ (70) | **UCLA (79)** 🏆 |
| **Runner-Up** | South Carolina (68) ✅ | South Carolina (51) |
| **Total** | 138.8 | 130 |
| **Margin** | 2 pts | **28 pts** |

* **Predicted:** ~~Connecticut~~ → **Actual Champion: UCLA** 🏆
* UCLA's first-ever women's title — 37-1 season, 2nd-most watched women's tournament ever on ESPN

> **Note:** All four predicted Women's Final Four teams — Connecticut, South Carolina, Texas, UCLA — reached the actual Final Four. A structural hit despite the champion miss.

---

## 🎯 Leverage Plays: Final Scorecard

Pre-tournament high-confidence differential picks, tracked against Round 1 results (March 19, 2026):

| Result | Game | Pick & Rationale | Score |
| :--- | :--- | :--- | :--- |
| ✅ | Texas (11) vs. BYU (6) | Fade BYU — Richie Saunders injury (18 PPG) | **Texas 79, BYU 71** |
| ✅ | TCU (9) vs. Ohio State (8) | TCU bracket buster | **TCU 66, Ohio St 64** |
| ✅ | Saint Louis (9) vs. Georgia (8) | High-risk volatility flag | **Saint Louis 102, Georgia 77** |
| ✅ | VCU (11) vs. UNC (6) | Caleb Wilson Fade — UNC rim protection | **VCU 82, UNC 78 OT** |
| ❌ | South Florida (11) vs. Louisville (6) | South Florida upset candidate | Louisville 83, USF 79 |

**Record: 4-1.** South Florida lost by 4 — within a single possession of a hit.

📋 *See [POST_MORTEM.md](./POST_MORTEM.md) for the full model analysis, storylines, and lessons learned.*

---

## 📂 Post-Tournament Archive

| Resource | Link |
| :--- | :--- |
| **Post-Mortem Analysis** | [POST_MORTEM.md](./POST_MORTEM.md) |
| **Men's Official Bracket** | [M_bracket.pdf](./brackets/M_bracket.pdf) |
| **Women's Official Bracket** | [W_bracket.pdf](./brackets/W_bracket.pdf) |
| **CFA Fusion Model Paper** | [CFA_article.pdf](./article/CFA_article.pdf) |
| **Final Kaggle Submission** | [submission_2026_CFA_FUSION.csv](./submissions/submission_2026_CFA_FUSION.csv) |
| **Kaggle Competition** | [March Machine Learning Mania 2 - 2026](https://www.kaggle.com/c/march-machine-learning-mania-2026) |
| **Historical Metrics** | [BartTorvik 2026 Rankings](https://barttorvik.com/trank.php?year=2026) |

---

## 🛠️ Project Context & Methodology

This repository contains the full end-to-end pipeline used for the **Kaggle March Machine Learning Mania 2026** competition.

### Key Strategy Filters
* **The "Boston" Leverage Play**: Fading BYU (6) due to the **Richie Saunders injury** (18 PPG) in favor of Texas (11).
* **Momentum Multiplier**: Identifying **Miami (OH)** and **Texas** as high-upset candidates based on First Four energy and expert sentiment from Gary Parrish (CBS).
* **Value Gap Analytics**: Exploiting discrepancies between Vegas lines and model projections, specifically the **Clemson (8) vs. Iowa (9)** matchup where the model identifies Clemson as a hidden favorite despite recent frontcourt injuries.

---

## 💻 Environment & Setup

### 1. Environment Setup
Use the provided `environment.yml` to create a dedicated environment for this project using miniconda or conda.

```bash
conda env create -f environment.yml
conda activate march_madness_2026
```

### 2. Configure Kaggle API

#### a. Persistent Method
Add your credentials to your shell profile to ensure automated data updates work seamlessly.

1.  Open your Zsh profile:
    ```bash
    nano ~/.zshrc
    ```
2.  Add the following line at the bottom (replace with your actual key):
    ```bash
    export KAGGLE_API_TOKEN=your_api_key
    ```
3.  Save and Exit: Press `Ctrl+O`, `Enter`, then `Ctrl+X`.
4.  Reload the profile:
    ```bash
    source ~/.zshrc
    ```

#### b. Quick Method
For a single session, you can set the variable directly in your terminal:

```bash
export KAGGLE_API_TOKEN=your_api_key
```
