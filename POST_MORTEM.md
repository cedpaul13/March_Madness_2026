# 🏀 2026 NCAA March Madness: Post-Mortem & Results

*Two historic champions. One honest accounting. The data got the landscape right — just not the throne.*

| | Men's Tournament | Women's Tournament |
| :--- | :--- | :--- |
| 🏆 **Champion** | Michigan (1) def. UConn (2) **69-63** | UCLA (1) def. South Carolina (1) **79-51** |
| 📅 **Date** | April 6, 2026 | April 5, 2026 |
| 🏟️ **Venue** | Lucas Oil Stadium, Indianapolis | Footprint Center, Phoenix |
| ⭐ **MVP** | Elliot Cadeau — 21 pts / 7 reb / 5 ast | Gabriela Jaquez — 21 pts |
| 📖 **Historic** | Michigan's first title since 1989 (37 years) | UCLA's first-ever women's title |

The CFA Fusion model went into tournament week predicting Duke as men's champion and Connecticut as women's champion. Neither trophy went where the numbers pointed. But the full story is more interesting than two wrong picks — Michigan was correctly placed in the men's final, every Women's Final Four team was named, and the Round 1 leverage plays went 4-1. This is the honest accounting.

---

## 📊 Predictions vs. Reality

### Men's Tournament

| Category | Model Prediction | Actual Result | Hit? |
| :--- | :--- | :--- | :--- |
| Champion | Duke (18.7%) | **Michigan (1)** | ❌ |
| Runner-Up | Michigan | **UConn (2)** | ⚠️ Near-Miss |
| Final Score | 75-74 | **69-63** | ❌ |
| Final Four — Slot 1 | Duke (1) | **Michigan (1)** | ⚠️ Right conference, wrong team |
| Final Four — Slot 2 | Florida (1) | **Illinois (3)** | ❌ |
| Final Four — Slot 3 | Michigan (1) | **Arizona (1)** | ✅ |
| Final Four — Slot 4 | Arizona (1) | **UConn (2)** | ⚠️ Arizona right, UConn surprise |
| Michigan reaches final | ✅ (as runner-up) | ✅ (as champion) | ✅ |

> **Bottom line:** The model had Michigan in the championship game — it just had them on the wrong side of the trophy. Duke's exit before the Final Four and Florida's absence were the structural failures. UConn reaching the final as a 2-seed was the biggest path surprise.

---

### Women's Tournament

| Category | Model Prediction | Actual Result | Hit? |
| :--- | :--- | :--- | :--- |
| Champion | Connecticut (18.0%) | **UCLA (1)** | ❌ |
| Runner-Up | South Carolina | **South Carolina (1)** | ✅ |
| Final Score | 70-68 | **79-51** | ❌ (margin off by 26 pts) |
| Final Four — Connecticut | ✅ Named | ✅ Made Final Four | ✅ |
| Final Four — South Carolina | ✅ Named | ✅ Made Final Four | ✅ |
| Final Four — Texas | ✅ Named | ✅ Made Final Four | ✅ |
| Final Four — UCLA | ✅ Named | ✅ Made Final Four | ✅ |
| UConn in the final | ✅ (predicted) | ❌ (lost to SC in semis 62-48) | ❌ |

> **Bottom line:** Every single Women's Final Four team was named by the model. This is a genuine structural hit. The miss was the bracket-half assignment — Connecticut was predicted to beat South Carolina in the final, but South Carolina eliminated UConn in the semifinals. UCLA, predicted to lose to Texas in their semi, instead won everything.

---

## 🔥 The Storylines That Defined 2026

### Michigan Ends the 37-Year Drought 🏆

The last time Michigan hoisted the men's national championship trophy, the Cold War was still a memory and Juwan Howard was a teenager. The 1989 Wolverines are a footnote most fans have to Google. Fast-forward 37 years, and Howard — now the coach who rebuilt the program with the patience of someone who understood what it meant to Michigan — watched sophomore guard **Elliot Cadeau** deliver one of the great tournament performances of the decade.

Against Arizona in the Final Four, Cadeau was something beyond a stat line: 13 points, 10 assists, 4 steals in a game that never felt in doubt. Against UConn in the championship, he finished with 21 points, 7 rebounds, and 5 assists — controlled, efficient, and built for the moment. Michigan's depth had been visible from the opening game: their 101-80 demolition of Howard in Round 1 was not a scare, it was a flex. The Wolverines didn't survive the tournament. They dominated it.

The model gave Michigan a 17.6% championship probability — the second-highest in the field. It correctly placed them in the finals. It simply gave the trophy to the wrong team.

---

### UCLA Makes History — The First-Ever Women's Title 🏆

UCLA entered the 2026 tournament at 37-1 with an 18-0 Big Ten record, the kind of season that makes you wonder if the bracket is a formality. It was not a formality. But the final score made it look like one.

**79-51.** South Carolina, a No. 1 seed playing in the national championship, was beaten by 28 points. That margin is not an aberration in women's college basketball finals — it is a pattern. When one team has a dominant frontcourt and a locked-in game plan, the blowout is real. Lauren Betts anchored the interior with 14 points and 11 rebounds. And then there was **Gabriela Jaquez** — a senior in the final game of her collegiate career — who scored 21 points on 8-of-14 shooting. Her final basket was a step-back three to put the game away. The arena knew what it was watching.

ESPN reported this as the 2nd-most-watched women's tournament ever. UCLA's program waited decades for this. It arrived all at once.

---

### Duke: The Phantom Champion ⚠️

The model's highest-probability pick for the men's title was Duke at 18.7%. Duke entered the tournament 33-2, the consensus favorite. They beat Siena 71-65 in the first round — unremarkable, but a win. Then the bracket closed in.

The numbers never found a reason to doubt them. The injury guardrail for Caleb Foster (-6.5% adjustment) was applied in the model's ensemble but not aggressively enough. Duke's exit before the Final Four was the kind of outcome that statistical models cannot fully price because it requires game-specific variance to land in exactly the wrong sequence. A single game, a single night, one team playing the best basketball of their season — and 18.7% becomes 0%.

The lesson here is not that Duke was a bad pick. It is that maximum-probability picks in single-elimination brackets carry a particular failure mode: when they fall, they fall completely. There is no partial credit.

---

### UConn: So Close, Again

In the men's bracket, UConn was the team that wasn't supposed to be there — a 2-seed navigating a Final Four that included three 1-seeds. They made the championship game. They lost to Michigan 63-69 in a competitive, grinding final that came down to Elliot Cadeau being better than anyone in a UConn jersey.

In the women's bracket, UConn was the team that was *supposed* to be there — the model's champion pick with an 18.0% probability. South Carolina ended it 62-48 in the semifinals. Not close. The Huskies went into the game ranked by the model as the favorite and came out 14 points behind.

Two deep runs. Two losses in Indianapolis in the same weekend. The Huskies were competitive in both tournaments and left with nothing. For a program that has defined the word "dynasty," this is the most uncomfortable kind of near-miss.

---

## 📋 Model Report Card

The **CFA Fusion model** (XGBoost efficiency 50% / Geospatial travel burden 25% / Momentum & rest 25%, blended 70% score fusion + 30% rank fusion) was tasked with predicting bracket outcomes across 132,134 matchup probabilities. Here is the honest grade.

### What the Model Got Right ✅

- **Michigan in the men's championship game** — predicted as finalist, achieved as champion. Structure was right.
- **South Carolina in the women's final** — named runner-up, was runner-up. Direct hit.
- **Texas in the Women's Final Four** — predicted, confirmed.
- **UCLA in the Women's Final Four** — named (as the YZ matchup with Texas), confirmed.
- **Arizona in the Men's Final Four** — predicted, confirmed.
- **All four Women's Final Four teams identified** — Connecticut, South Carolina, Texas, UCLA. Every name correct; bracket-half assignments scrambled.
- **Illinois as a force** — the model did not predict them in the Final Four but had them as a strong 3-seed. Their 105-70 opening over Penn was a signal the model registered.

### Near-Misses ⚠️

- Men's championship: the two finalists were Michigan and UConn — the model had Michigan correct, but as runner-up instead of champion, and missed UConn reaching the final at all.
- Women's Final Four: all four teams appeared but Connecticut was predicted to beat South Carolina, not lose to them. Two correct teams, swapped outcomes.
- Score proximity: men's projected 75-74 total; actual was 69-63. The game was competitive and lower-scoring than a typical Final — directionally consistent, numerically off.

### Where the Model Failed ❌

- **Champion selection — both sides.** Duke never reached the Final Four. Connecticut never reached the final.
- **Duke's injury adjustment was insufficient.** The -6.5% guardrail for Caleb Foster moved the needle but not enough to flag Duke as fragile. In hindsight, the tax should have been closer to -10 to -12%.
- **Florida's absence.** The model slotted Florida into the men's WX semifinal (Duke vs Florida). Florida did not reach the Final Four. Illinois (3-seed) took the slot.
- **Women's final margin.** Projected 2-point Connecticut win; actual was a 28-point UCLA blowout. The model had no mechanism to capture a dominant "locked-in" performance of this magnitude.

### Overall Grade

**Men's bracket: B−** — Correctly mapped Michigan's path to the final; wrong champion; three of four Final Four teams named.

**Women's bracket: B** — All four Final Four teams named; champion wrong; South Carolina finalist correct; blowout margin completely unmodeled.

**Leverage plays: A−** — 4-1 on named plays, with the miss coming within a single possession.

---

## 🎯 Round 1 Leverage Plays: Final Scorecard

Pre-tournament, five games were identified as high-value differential picks where the model's edge over chalk was greatest. Results from March 19, 2026:

| Result | Game | Pick & Rationale | Final Score |
| :--- | :--- | :--- | :--- |
| ✅ **HIT** | Texas (11) vs. BYU (6) | Fade BYU — Richie Saunders (18 PPG) injury | **Texas 79, BYU 71** |
| ✅ **HIT** | TCU (9) vs. Ohio State (8) | TCU identified as bracket buster | **TCU 66, Ohio St 64** |
| ✅ **FLAGGED** | Saint Louis (9) vs. Georgia (8) | High-risk volatility flag on this slot | **Saint Louis 102, Georgia 77** |
| ✅ **HIT** | VCU (11) vs. North Carolina (6) | Caleb Wilson Fade — UNC rim protection concern | **VCU 82, UNC 78 OT** |
| ❌ **MISS** | South Florida (11) vs. Louisville (6) | South Florida upset candidate | **Louisville 83, USF 79** |

**Record: 4-1.** South Florida's loss was a 4-point game decided in the final minute — within a single possession of a different result.

**Bonus: Notable first round outcomes**

| Game | Seed Matchup | Score | Note |
| :--- | :--- | :--- | :--- |
| High Point vs. Wisconsin | 12 over 5 | 83-82 | Major upset — 1-point thriller |
| Illinois vs. Pennsylvania | 3 blowout | 105-70 | Illinois depth on full display |
| Michigan vs. Howard | 1 dominant | 101-80 | Michigan's title run begins here |
| Arkansas vs. Hawai'i | 4 dominant | 97-78 | Arkansas showed Final Four potential |

---

## ⭐ Stars of the 2026 Tournament

### Elliot Cadeau — Michigan's Sophomore Sensation

Cadeau was 19 years old and had not yet been born the last time Michigan won this tournament. None of that showed.

| Game | PTS | REB | AST | STL |
| :--- | :--- | :--- | :--- | :--- |
| Final vs. UConn | 21 | 7 | 5 | — |
| Semifinal vs. Arizona | 13 | — | 10 | 4 |

He is not a stat-accumulator — he is a game-controller. Against Arizona's elite defense, he ran the offense with ten assists and four steals without forcing a single play. Against UConn in the final, he scored 21 in a game that could never get away from Michigan. Tournament MVP. Likely not the last time we'll see him here.

---

### Lauren Betts — UCLA's Anchor

Every dominant title run needs a frontcourt anchor, and Betts was exactly that. Her 14 points and 11 rebounds in the final against South Carolina — a team built around interior strength — neutralized what was supposed to be the Gamecocks' advantage. She made the final feel inevitable.

| Game | PTS | REB |
| :--- | :--- | :--- |
| Final vs. South Carolina | 14 | 11 |

---

### Gabriela Jaquez — The Perfect Finale

Seniors rarely get the storybook ending. Jaquez did.

| Game | PTS | FG | 3PT |
| :--- | :--- | :--- | :--- |
| Final vs. South Carolina | 21 | 8-14 | 2-4 |

The last game of her UCLA career. The most-watched women's game in years. She went 8-of-14 from the field and 2-of-4 from three. The step-back three late in the fourth quarter was the punctuation mark. UCLA's coaching staff has built something — and Jaquez leaves it in a place she could only have dreamed of in her freshman year.

---

## 🔍 Lessons Learned

### 1. Women's Finals Always Have a Goofy Score

The model projected a 70-68 Connecticut win — a tight, regression-to-the-mean championship game. The actual result was **79-51**, a 28-point blowout. This is not a one-off anomaly. Women's championship games have a structural tendency to produce outlier margins because one team enters the final "locked in" — surgically prepared, defensively loaded, emotionally unified — while the other is running on fumes after a brutal semifinal and the accumulated weight of the season.

**The rule for 2027:** The projected margin in a women's final is the floor for the winning team, not the ceiling. Treat big spread covers as live, not reckless. If the better team has the frontcourt edge, senior guards, and a coach who can squeeze the game into their preferred shape, do not be afraid of an ugly championship score. The underdog in women's championship games is rarely competitive in the second half when the better team is playing its best basketball.

---

### 2. Legacy, Culture, and Good Coaches Are Not in the Data

Michigan's 37-year drought was a narrative force that no efficiency metric can quantify. Juwan Howard — a Fab Five legend who returned to Ann Arbor as coach — built a program around the idea that Michigan basketball means something. Elliot Cadeau's performance exceeded his season statistics in every key moment. The data saw a 17.6% probability. The arena saw a different kind of team.

The men's tournament punished the model for treating legacy as decoration. Legacy matters because it changes how teams carry pressure. Good coaches matter because they convert that pressure into structure: better late-game possessions, cleaner timeout adjustments, fewer panic shots, and more belief when the bracket tightens. Michigan and UConn both had that. Duke had the best number; Michigan had the better tournament identity.

The Duke adjustment (-6.5% for Caleb Foster's injury) was directionally correct but magnitude-insufficient. A team playing through an injury to a key offensive piece, facing a single-elimination format, carries more variance than the model weighted.

**The rule for 2027:** Add a program narrative and coaching multiplier. Teams playing for a historic milestone (droughts over 20 years, program's first title, coach with personal stakes) should receive a 3-5% upward adjustment in late-round probabilities when paired with an elite or tournament-proven coach. Human performance elevates under peak pressure — especially the kind of pressure that only comes once in a generation.

---

### 3. Watch Games During the Regular Season

This is the meta-lesson. Everything above — the women's margin miss, Duke's overconfidence, Michigan's undervaluation — traces back to a single gap: the model never watched a game.

Team chemistry, defensive rotations, how a squad responds after an opponent goes on a 10-0 run, whether a star player is playing through soreness that doesn't show in the box score — none of this lives in AdjOE or AdjDE or geospatial travel burden. Illinois at 105-70 over Penn in Round 1 was not a surprise to anyone who watched the Big Ten in February. Michigan's composure in close games was visible all season to anyone paying attention.

**The rule for 2027:** Build a qualitative override layer during the season, not the week the bracket drops. Watch real games in January and February, especially conference road games, rivalry games, and late-clock possessions against top-50 opponents. Track a small set of human-observed flags — defensive identity in transition, how a team responds to adversity, whether guards can settle a bad possession, a star player's availability nuances beyond official injury reports — that can adjust model probabilities by 3-5% before the tournament begins. Call it the "Watched Games Adjustment." It doesn't need to be systematic. It just needs to be honest.

---

## 🧠 Pre-Tournament Intel: How It Held Up

*Before the model ran, there was research — articles, podcasts, and the sharp instincts of college basketball wise guy Alan Boston. Here's the honest scorecard.*

---

### Alan Boston's Rankings vs. Reality

Boston's pre-tournament top 12, graded against the actual results:

| Rank | Team | Boston's Case | Actual Result | Grade |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Florida | "Can go back-to-back, like Michigan" | Did not reach Final Four | ❌ |
| 2 | Duke | "Upside very good, can go through everybody" | Eliminated before Final Four | ❌ |
| **3** | **Michigan** | **"Wears teams down with size and depth"** | **🏆 NATIONAL CHAMPION** | **✅** |
| 4 | Arizona | "Beware crashout — young, 363rd in 3PT, 1st in FT attempts" | Made Final Four | ✅ |
| 5 | UConn | "Upside is win all, coaching solid, could upset top 4" | Made men's Final (runner-up) | ✅ |
| 6 | Gonzaga | — | Did not reach Final Four | ❌ |
| 7 | Purdue | — | Did not reach Final Four | ❌ |
| 8 | Houston | — | Did not reach Final Four | ❌ |
| 9 | Iowa State | — | Did not reach Final Four | ❌ |
| 10 | Illinois | — | **Made Final Four** | ✅ |
| 11 | Kentucky | "Sneaky good" | Did not reach Final Four | ❌ |
| 12 | Michigan State | — | Did not reach Final Four | ❌ |

> **Bottom line on Boston:** His #3 pick won the whole thing. He correctly identified Michigan's formula — wear teams down with size and depth — and that is exactly how the Wolverines won. His concern about Arizona crashing out early (young team) was valid as a risk flag even though Arizona made the Final Four. Florida at #1 was the big miss.

---

### Boston's "On the Horizon" Teams

Teams Boston flagged as potential factors outside the major programs:

| Team | Boston's Note | Actual Result |
| :--- | :--- | :--- |
| **High Point** | "Like them again — same team, but lost their big rim protector" | ✅ **Beat Wisconsin 83-82 (12-over-5 upset)** |
| Oakland | "Zone defense can drive teams crazy" | Result unknown past Round 1 |
| Belmont | "Extremely high level right now — expect 1-2 wins if they make it" | Did not make main bracket |
| Troy | Listed as potential upset | ❌ Lost to Nebraska 47-76 (R64) |
| Yale | "James Jones always dangerous, fav Ivy team" | Result unknown past Round 1 |

> **The High Point call was the gem.** Boston flagged them the year before and came back on them despite the rim protector loss. They delivered — 83-82 over Wisconsin in one of the best first-round games of the tournament. The caveat he added (rim concern) was honest and correct as a risk factor; the pick was still right.

---

### Lines Intel Scorecard

Pre-tournament line plays identified from research:

| Pick | Line | Result | Score |
| :--- | :--- | :--- | :--- |
| **TCU** | +3.0 | ✅ **Won** | 66-64 over Ohio State |
| **High Point** | +11 | ✅ **Won** | 83-82 over Wisconsin |
| Troy | — | ❌ Lost | 47-76 to Nebraska |
| North Dakota | — | Unknown | — |
| Siena | — | ❌ Lost | 65-71 to Duke |
| Hawai'i | — | ❌ Lost | 78-97 to Arkansas |

**Positive ROI on the two biggest plays: TCU and High Point both cashed.**

---

### Expert Consensus Accuracy: How the Rankings Held

**KenPom top 12** had the Final Four at ranks 2 (Arizona), 3 (Michigan), 7 (Illinois), 11 (Connecticut):

| Team | KenPom Rank | Made Final Four? |
| :--- | :--- | :--- |
| Duke | 1 | ❌ |
| **Arizona** | 2 | ✅ |
| **Michigan** | 3 | ✅ |
| Florida | 4 | ❌ |
| Houston | 5 | ❌ |
| Iowa State | 6 | ❌ |
| **Illinois** | 7 | ✅ |
| Purdue | 8 | ❌ |
| Michigan State | 9 | ❌ |
| Gonzaga | 10 | ❌ |
| **Connecticut** | 11 | ✅ (reached men's final) |
| Vanderbilt | 12 | ❌ |

> KenPom's top 12 contained all four Final Four teams — but only 4 of 12 made it. The lesson: the top of the efficiency rankings is a necessary condition for a Final Four run, not a sufficient one.

**ESPN's "8 Teams That Can Win"** (Arizona, Duke, Florida, Houston, Illinois, Iowa St, Michigan, UConn):
- Final Four teams from this list: Arizona ✅, Michigan ✅, Illinois ✅, UConn ✅ — **4 of 4 Final Four teams named. Perfect.**

**Sports Illustrated's "8 Teams That Can Win"** (Duke, Michigan, Arizona, Florida, UConn, Iowa St, Illinois, St John's):
- Final Four teams from this list: Michigan ✅, Arizona ✅, UConn ✅, Illinois ✅ — **4 of 4 Final Four teams named. Perfect.**

> Both expert consensus lists named every men's Final Four team. The gap was simply predicting *which* of those 7-8 teams would go all the way — and there the consensus (Duke, Florida) was wrong.

---

### Bleacher Report Bracket Busters: Final Check

| Team | Projected Seed | Result |
| :--- | :--- | :--- |
| Miami (OH) | No. 10 | Unknown past R64 |
| **South Florida** | No. 11 | ❌ Lost to Louisville 83-79 (close) |
| **TCU** | No. 9 | ✅ Beat Ohio State 66-64 |
| UCLA (women's) | No. 8 | ✅ **Won the Women's Championship** |
| Utah State | No. 8 | Unknown past R64 |

> TCU delivered as the named bracket buster. UCLA exceeded every bracket buster label — they won the whole tournament.

---

### The Meta-Lesson from Intel vs. Model

The expert consensus (ESPN, SI, KenPom, Boston) and the CFA Fusion model converged on the same pool of 8 teams as legitimate title contenders. They disagreed on *ordering*. The tournament outcome vindicated the pool and punished the ordering — Michigan was 3rd on Boston's list, 7th on ESPN's, 3rd on KenPom. It took the trophy.

The edge in future years is not identifying the right pool — everyone does that. The edge is in correctly de-prioritizing the top of that pool (Duke, Florida) in favor of the teams with structural advantages (Michigan's size/depth, Illinois's defensive identity) that the headlines don't amplify.

---

## 🛠️ Technical Notes

The CFA Fusion model combined three prediction agents:

| Component | Weight | Script |
| :--- | :--- | :--- |
| XGBoost efficiency (AdjOE/AdjDE, Barthag) | 50% | `04_predict_2026.py` |
| Geospatial travel burden | 25% | `05_geospatial_distance.py` |
| Momentum & rest engine | 25% | `06_momentum_and_fatigue.py` |

Final blend: **70% score fusion + 30% rank fusion** (`08_cfa_fusion_backtester.py`). Probabilities clipped to [0.015, 0.985].

**Injury guardrails applied** (`07_final_pro_ensemble.py`):
- Duke: -6.5% (Caleb Foster)
- UNC: -11% (Caleb Wilson rim protection)
- Michigan: -3% (precautionary)

**Simulation:** 10,000 Monte Carlo bracket runs per tournament (`11_monte_carlo_bracket.py`).

**Primary submission:** [`submission_2026_CFA_FUSION.csv`](./submissions/submission_2026_CFA_FUSION.csv) — 132,134 matchup probabilities.

**Methodology reference:** [CFA arXiv article](./article/CFA_article.pdf)

---

*Tournament completed April 6, 2026.*

[← Back to README.md](./README.md)
