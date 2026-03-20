# 🏀 March Madness 2026: Predictive Analytics & Bracket Strategy

A high-performance predictive pipeline for the **2026 NCAA Division I Men's and Women's Basketball Tournaments**. This project utilizes the **CFA Fusion** model (see [**CFA arXiv article**](./article/CFA_article.pdf)), integrating advanced efficiency metrics (AdjOE/AdjDE), momentum filters, and expert sentiment analysis to generate optimized tournament brackets.

## 🏆 Submitted Brackets & Projections

Access the finalized PDF brackets submitted for the 2026 competition:
* 📂 [**Men's Official Bracket**](./brackets/M_bracket.pdf)
* 📂 [**Women's Official Bracket**](./brackets/W_bracket.pdf)

---

### 🧊 Men's Tournament Projections

**Final Four Matchups**
| Round | Matchup | Predicted Winner |
| :--- | :--- | :--- |
| Final Four (R5WX) | (1) Duke vs. (1) Florida | **(1) Duke** |
| Final Four (R5YZ) | (1) Michigan vs. (1) Arizona | **(1) Michigan** |

**National Championship**
*📍 Lucas Oil Stadium | April 6, 2026*

| Team | Score | Vegas ML | Spread |
| :--- | :--- | :--- | :--- |
| **Duke** | **75** | **-103** | **-1.5** |
| Michigan | 74 | 103 | +1.5 |

* **Total (O/U):** 149.9
* **Predicted Champion:** **Duke**

---

### 🧊 Women's Tournament Projections

**Final Four Matchups**
| Round | Matchup | Predicted Winner |
| :--- | :--- | :--- |
| Final Four (R5WX) | (1) Connecticut vs. (1) South Carolina | **(1) Connecticut** |
| Final Four (R5YZ) | (1) Texas vs. (1) UCLA | **(1) Texas** |

**National Championship**
*📍 Lucas Oil Stadium | April 5, 2026*

| Team | Score | Vegas ML | Spread |
| :--- | :--- | :--- | :--- |
| **Connecticut** | **70** | **-105** | **-2.5** |
| South Carolina | 68 | 105 | +2.5 |

* **Total (O/U):** 138.8
* **Predicted Champion:** **Connecticut**

---

## 📊 Live Tracking & Resources

Stay updated with official scores and competition standings:

| Resource | Link |
| :--- | :--- |
| **NCAA Men's Scoreboard** | [Official NCAA Men's Scores](https://www.ncaa.com/scoreboard/basketball-men/d1) |
| **NCAA Women's Scoreboard** | [Official NCAA Women's Scores](https://www.ncaa.com/scoreboard/basketball-women/d1) |
| **Kaggle Mania 2026** | [March Machine Learning Mania 2 - 2026](https://www.kaggle.com/c/march-machine-learning-mania-2026) |
| **Advanced Metrics** | [BartTorvik 2026 Rankings](https://barttorvik.com/trank.php?year=2026) |

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
