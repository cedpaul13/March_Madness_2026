# The 2026 Post-Mortem: What the Model Saw, and What It Missed

*I spent a season building a machine to predict March Madness. Michigan and UCLA spent the same season building something better. This is the full accounting: what landed, what collapsed, and what changes before I run it back.*

---

## The Final Ledger

| | Men's Tournament | Women's Tournament |
| :--- | :--- | :--- |
| **Champion** | Michigan (1) def. UConn (2), **69-63** | UCLA (1) def. South Carolina (1), **79-51** |
| **Date · Venue** | April 6 · Lucas Oil Stadium, Indianapolis | April 5 · Mortgage Matchup Center, Phoenix |
| **Most Outstanding Player** | Elliot Cadeau: 19 pts, 3 reb, 2 ast, 2 stl | Lauren Betts: 14 pts, 11 reb |
| **The History** | Michigan's first title since 1989, a 37-year wait | UCLA's first NCAA women's basketball title |

The CFA Fusion model went into tournament week with Duke winning the men's bracket and Connecticut winning the women's. Neither trophy went where the numbers pointed. The honest ledger is still more interesting than two wrong picks. The model called the Michigan-Arizona national semifinal exactly, down to the matchup and the winner. It put Michigan in the championship game. It named all four women's Final Four teams before the tournament started, and it went 4-1 on its Round 1 leverage plays. It also handed both trophies to teams that never won them. A fair post-mortem has to sit with all of that at once.

---

## Predictions vs. Reality

*Legend: ✓ hit · ~ near-miss · ✗ miss*

### Men's Tournament

| Category | Model Prediction | Actual Result | Verdict |
| :--- | :--- | :--- | :---: |
| Champion | Duke (18.7%) | Michigan (1) | ✗ |
| Runner-up | Michigan | UConn (2) | ~ |
| National final | Duke 75, Michigan 74 | Michigan 69, UConn 63 | ~ |
| Semifinal 1 | Duke vs. Florida; Duke advances | UConn 71, Illinois 62 | ✗ |
| Semifinal 2 | Michigan vs. Arizona; Michigan advances | **Michigan 91, Arizona 73** | ✓ exact |
| Final Four field | Duke, Florida, Michigan, Arizona | Michigan, Arizona, UConn, Illinois | ~ 2 of 4 |
| Michigan reaches the final | Yes, as runner-up | Yes, as champion | ✓ |

**Bottom line:** one half of the bracket behaved. The model called the Michigan-Arizona semifinal down to the participants and the winner, and it had Michigan playing on the final Monday. The other half fell apart. Duke and Florida, both 1-seeds and both model favorites, never reached Indianapolis; their places went to a 2-seed and a 3-seed, and the 2-seed made the final. So the champion miss wasn't a wild guess gone wrong. The model built the right game and put the trophy on the wrong sideline.

### Women's Tournament

| Category | Model Prediction | Actual Result | Verdict |
| :--- | :--- | :--- | :---: |
| Champion | Connecticut (18.0%) | UCLA (1) | ✗ |
| Runner-up | South Carolina | South Carolina (1) | ✓ |
| National final | UConn 70, South Carolina 68 | UCLA 79, South Carolina 51 | ✗ |
| Final Four field | UConn, South Carolina, Texas, UCLA | All four | ✓ 4 of 4 |
| Semifinal outcomes | UConn over SC · Texas over UCLA | SC 62, UConn 48 · UCLA 51, Texas 44 | ✗ |

**Bottom line:** every women's Final Four team was named in advance. That part was a real structural read; the model looked at the field and correctly picked out the four best teams in the country. What it got wrong was everything that happened once they reached Phoenix. It had Connecticut beating South Carolina in the final, and South Carolina eliminated Connecticut before the final existed. It had UCLA losing their semifinal. UCLA won the whole thing by 28.

---

## The Storylines

### Michigan: Rebuilt from Scratch, Champion in One Year

The last time Michigan won the national championship, the Berlin Wall was still standing. April 1989: Steve Fisher coaching as an interim who never lost, Glen Rice on fire for six games, Rumeal Robinson at the line in overtime against Seton Hall. Thirty-seven years is long enough for a title to slide out of living memory and into program mythology.

What ended the drought wasn't patience. Dusty May arrived in Ann Arbor in 2024, having already taken 9-seed Florida Atlantic to a Final Four, and he built his 2025-26 roster almost entirely out of the transfer portal: Elliot Cadeau from North Carolina, Yaxel Lendeborg from UAB, Aday Mara from UCLA, Morez Johnson Jr. from Illinois. A starting core in its first season wearing the jersey. The sport's old logic says teams like that lack the connective tissue to survive March. Michigan went 29-2 through the regular season, won the Big Ten, and spent the next three weeks making the old logic look sentimental.

The run itself was brutal. A 101-80 dismissal of Howard University in Round 1. Ninety or more points in five consecutive tournament games, which no team had ever done. In the national semifinal Michigan beat Arizona 91-73 and led by as many as 30; Mara scored a career-high 26, and freshman Trey McKenney hit four threes. When the final against UConn turned into a rockfight instead, Michigan won it at the free-throw line, 25-of-28, and closed out a 69-63 grinder.

Then the ending nobody scripts: within weeks, the Dallas Mavericks hired May to replace Jason Kidd, a Hall of Fame point guard, as their head coach. An NBA franchise watched that season and decided the coach was the answer to their own problems. Hard to think of a stronger outside audit of what Michigan just pulled off.

The model gave Michigan a 17.6% championship probability, second-highest in the field, and put them in the final. It read the team correctly and the moment wrong. More on that in the lessons.

### UCLA: A 28-Point Coronation

UCLA came into March with one loss all year and an 18-0 record in the Big Ten, the kind of résumé that makes a bracket feel like paperwork. It wasn't; their semifinal against Texas was a 51-44 defensive grind that could have gone either way for long stretches. The final was a different sport.

**79-51.** South Carolina, a 1-seed and the program that has set the standard in the women's game for a decade, trailed from the opening minutes and never led. Lauren Betts controlled the paint with 14 points and 11 rebounds against a team built on interior force. Gianna Kneepkens hit three threes for 15. Gabriela Jaquez, a senior playing the last game of her college career, scored 21 on 8-of-14 and buried the step-back three that turned the fourth quarter into a party.

It was the program's first NCAA women's basketball title; UCLA's 1978 crown came in the AIAW era, before the NCAA sponsored the women's game. The country showed up for it, too: 9.9 million average viewers for the final, a 10.7 million peak, and the second-most-watched women's tournament in ESPN's history. UCLA finished the season 37-1.

The model had UCLA in the Final Four and dismissed them there. That miss has a lesson attached as well.

### Duke: The Phantom Champion

The model's men's champion was Duke at 18.7%, the highest probability in the field, attached to the No. 1 overall seed. The pick did not die quietly. It died up nineteen points.

Duke's tournament had been uneasy from the start. Their first-round game against Siena was a 71-65 escape in which "survives" was the operative verb in every headline. Then, in the Elite Eight, Duke led UConn by 19 and was closing in on the Final Four the model had penciled in for them. UConn took the lead apart possession by possession, and with 0.3 seconds left Braylon Mullins hit the three that ended it, 73-72.

One possession from validating the pick, and zero credit for the proximity. Single-elimination formats are merciless in exactly this way: an 18.7% champion doesn't fail gradually, it fails all at once, the moment its win probability inside one game touches zero. The model's injury guardrail for Caleb Foster (a -6.5% adjustment) was right about Duke's fragility and wrong about its size.

### UConn: The Cruelest Weekend in Program History

No school owned more of this tournament's oxygen and left with less.

The men weren't supposed to be there. A 2-seed in a bracket the model had assigned to Duke, they pulled off the Mullins miracle in the Elite Eight, ground past Illinois 71-62 in the semifinal, and walked into the title game having beaten the No. 1 overall seed on the way. Alex Karaban gave them 17 points and 11 rebounds in the final, and Tarris Reed Jr. added 13 and 14. Michigan's free-throw shooting decided it anyway.

The women were absolutely supposed to be there. Undefeated, riding a 54-game winning streak, defending champions, and the model's title pick at 18.0%. South Carolina held them to 19-of-61 from the field, 31.1%, their worst shooting night of the season. Sarah Strong, the AP Player of the Year, went 4-of-16; Azzi Fudd went 3-of-15. The 62-48 final was Connecticut's lowest-scoring game since the 2022 championship, which they also lost to South Carolina.

Two deep runs ended days apart, the women on Friday in Phoenix and the men on Monday in Indianapolis. For the sport's defining dynasty, a week of almosts and a flight home with nothing.

---

## Model Report Card

The CFA Fusion model combines XGBoost efficiency (50%), geospatial travel burden (25%), and momentum and rest (25%), blended 70% score fusion / 30% rank fusion, and produced 132,134 matchup probabilities across both tournaments. The grade, without a curve:

### What It Got Right

- **The Michigan-Arizona semifinal, exactly.** Predicted matchup, predicted winner. In a 68-team field, calling a specific national semifinal is the model's cleanest structural hit.
- **Michigan in the men's championship game.** Predicted as finalist; arrived as champion.
- **All four women's Final Four teams.** Connecticut, South Carolina, Texas, UCLA. Named in advance, all present in Phoenix.
- **South Carolina in the women's final.** Named as finalist, was the finalist.
- **Arizona in the men's Final Four.** Predicted, confirmed.
- **Illinois as a live threat.** Not projected into the Final Four, but rated as a dangerous 3-seed, and their 105-70 opening rout of Penn was the kind of game that rating implied.

### Near-Misses

- **The men's final itself.** Two actual finalists: Michigan (predicted) and UConn (not). Right stage for Michigan, wrong opponent across from them.
- **Duke, by one possession.** Up 19 in the Elite Eight, lost at 0.3 seconds. The pick was closer to right than the zero in the results column shows, which is precisely why the results column is the one that counts.
- **Score texture.** Projected 75-74 in the men's final; actual 69-63. Right competitiveness, wrong totals.

### What Failed

- **Champion selection, both brackets.** The single output most people care about, wrong twice.
- **The Duke injury tax was too small.** The -6.5% for Caleb Foster acknowledged the fragility without really pricing it. In hindsight the correct number was roughly double.
- **Florida's absence.** Slotted into a semifinal they never reached; the second 1-seed on the board lost in the round of 32 to 9-seed Iowa, 73-72.
- **The women's final margin.** Projected a 2-point Connecticut win; reality was a 28-point UCLA blowout in a game UCLA led wire to wire. The model had no mechanism for that kind of locked-in performance. See Lesson 1.

### Grades

| Bracket | Grade | Justification |
| :--- | :---: | :--- |
| Men's | **B** | Exact semifinal call; finalist correct; champion wrong; half the Final Four missed |
| Women's | **B** | Final Four 4-of-4; runner-up correct; champion and both semifinal outcomes wrong |
| Leverage plays | **A−** | 4-1, with the miss losing by four points |

---

## Round 1: The Leverage Plays

A leverage play isn't a prediction of the most likely outcome. It's a bet on the gap between the model's probability and the public's. Five games were flagged before the tournament as the highest-value differentials. Results from March 19:

| Verdict | Game | The Case | Final |
| :---: | :--- | :--- | :--- |
| ✓ | Texas (11) vs. BYU (6) | Fade BYU: Richie Saunders (18 PPG) injured | Texas 79, BYU 71 |
| ✓ | TCU (9) vs. Ohio State (8) | TCU as bracket-buster | TCU 66, Ohio State 64 |
| ✓ | Saint Louis (9) vs. Georgia (8) | Volatility flag on the 8/9 slot | Saint Louis 102, Georgia 77 |
| ✓ | VCU (11) vs. North Carolina (6) | Fade UNC: rim protection resting on a freshman | VCU 82, UNC 78 (OT) |
| ✗ | South Florida (11) vs. Louisville (6) | USF upset candidate | Louisville 83, USF 79 |

**4-1.** The Texas call meant fading a BYU team carrying AJ Dybantsa, in what turned out to be the star freshman's only NCAA tournament game. The Saint Louis "volatility flag" undersold things considerably; the Billikens scored 102, with Dion Brown going 9-of-10 at the rim. The one miss lost by four, with Isaac McKneely scoring 23 to give Louisville its first tournament win since the Pitino era.

**Elsewhere in Round 1, the games that mattered:**

| Game | Line | Note |
| :--- | :--- | :--- |
| High Point 83, Wisconsin 82 | 12 over 5 | Chase Johnston, who had played 406 minutes all season without making a two-point basket, hit his first with 11 seconds left |
| Illinois 105, Penn 70 | 3-seed rout | The depth that later carried Illinois to the Final Four |
| Michigan 101, Howard 80 | 1-seed statement | First of five straight 90-point games |
| Arkansas 97, Hawai'i 78 | 4-seed statement | Comfortable start to a strong tournament |
| Duke 71, Siena 65 | 1-seed escape | The first crack in the favorite |

---

## The Stars

### Elliot Cadeau, Michigan

Two years at North Carolina as a pass-first point guard who never quite made the offense his. One trip through the portal. One season in Ann Arbor, ending with the Most Outstanding Player award in a building where Michigan hadn't celebrated since before he was born.

| Game | PTS | REB | AST | STL |
| :--- | :---: | :---: | :---: | :---: |
| Semifinal vs. Arizona | 13 | 5 | 10 | 4 |
| Final vs. UConn | 19 | 3 | 2 | 2 |

The semifinal line is the honest version of Cadeau: 10 assists and 4 steals in a 30-point blowout, next to 5-of-17 shooting and six turnovers. Brilliant and messy in the same box score. In the final the mess disappeared. He scored a game-high 19 in a rockfight, much of it from the line where Michigan went 25-of-28. His college coach reached the NBA before he did. He'll be fine.

### Lauren Betts, UCLA

Every coronation needs an anchor. Betts spent the final erasing the interior advantage South Carolina's roster was built around: 14 points, 11 rebounds, and a paint that belonged to UCLA for forty minutes. The Final Four Most Outstanding Player award went with it, on the strength of the full run; she'd put up 16 and 11 with three blocks on Texas in the semifinal two days earlier.

### Gabriela Jaquez, UCLA

Seniors rarely get the storybook ending; Jaquez wrote hers in front of ten million people. In the last game of her college career she scored 21 on 8-of-14 from the field, 2-of-4 from three, including the step-back that ended the argument. Four years in the program, and she leaves holding a trophy that had never existed for UCLA until that afternoon.

---

## Lessons for 2027

### 1. Championship margins are structurally underestimated

The model projected a 70-68 women's final. Reality was 79-51, a 26-point miss on margin, and it fits a pattern rather than an anomaly. Women's championship games disproportionately produce blowouts, because by the final one team is often peaking, surgically prepared and defensively locked in, while the other has spent everything surviving its semifinal. South Carolina had just dismantled an undefeated UConn; two days later they had nothing left for a UCLA team that never trailed.

**The 2027 rule:** treat the projected margin for the stronger team in a women's final as a floor, not a midpoint. A mean-reverting score projection systematically underprices the locked-in blowout, and that tail is fat enough to price deliberately.

### 2. Coaching is a real variable, and the data never sees it

The efficiency numbers rated Michigan's roster correctly: 17.6%, second in the field. What they couldn't rate was the specific thing that won the tournament, a coach with a proven March record taking five strangers from the portal and having them play like a five-year program by the first weekend. Dusty May had already taken a 9-seed to a Final Four. He then won a title with a first-year roster, and an NBA franchise hired him to replace a Hall of Famer within the month. Every institution that evaluated May's coaching this season priced it higher than my model did, and my model priced it at zero, because AdjOE has no column for it.

**The 2027 rule:** add a bounded coaching-and-continuity adjustment, on the order of 3-5% in late-round win probabilities, for tournament-proven coaches; and treat portal-heavy rosters as a variance amplifier in both directions rather than a pure negative. Critically, the adjustment gets written down before Selection Sunday, not discovered in April. An override invented after seeing the bracket is just a story you tell yourself.

### 3. Watch the games

The meta-lesson underneath the other two. The margin miss, the Duke overconfidence, the Michigan undervaluation: each traces back to the same gap. The model never watched a game, and during the season neither did I, not with any real attention. Illinois hanging 105 on Penn surprised nobody who watched the Big Ten in February. Michigan's late-game composure was visible all winter. Duke's habit of playing with fire was a known quantity to anyone tracking them closely; the Siena escape was a symptom, and the Elite Eight collapse was the bill coming due.

**The 2027 rule:** maintain a qualitative layer during the season, not the week the bracket drops. Watch conference road games and late-clock possessions against top-50 opponents in January and February. Track a small, honest set of human-observed flags, things like how a team answers a 10-0 run, whether the guards can settle a broken possession, availability nuance that box scores miss, each worth a pre-registered 3-5% probability nudge. The models handle the averages. The eyes are for everything the averages smooth over.

---

## Pre-Tournament Intel: The Scorecard

*Before the model ran, there was research: rankings, podcasts, and the sharp instincts of the professional bettor Alan Boston. Here's how the humans did.*

### Boston's Top 12 vs. Reality

| Rank | Team | Boston's Case | Result | Verdict |
| :---: | :--- | :--- | :--- | :---: |
| 1 | Florida | "Can go back-to-back" | Out in Round 2; Iowa (9), 73-72 | ✗ |
| 2 | Duke | "Can go through everybody" | Elite Eight, up 19, eliminated | ✗ |
| **3** | **Michigan** | **"Wears teams down with size and depth"** | **National champion** | **✓** |
| 4 | Arizona | "Beware the crashout: young; won at Houston; 363rd of 365 in 3PT scoring, 4th in paint points, 1st in FT attempts" | Final Four | ✓ |
| 5 | UConn | "Upside is win it all; coaching solid; could upset the top 4" | National runner-up | ✓ |
| 6-9 | Gonzaga, Purdue, Houston, Iowa State | n/a | None reached the Final Four | ✗ |
| 10 | Illinois / Louisville / Vanderbilt | Three-way tie on his board | Illinois: Final Four; Louisville won a game; Vanderbilt out early | ~ |
| 11-12 | Kentucky, Michigan State | "Kentucky sneaky good" | Neither made a run | ✗ |

Boston's No. 3 won the title, and he called the mechanism too. Size and depth wearing opponents down is exactly how a team scores 90-plus in five straight games. His Arizona worry (young team, crashout risk) was a fair flag even though it didn't land. Florida at No. 1 was the shared blind spot: the model's second semifinalist, Boston's top team, nobody's champion.

### Boston's Sleepers

| Team | The Note | Result |
| :--- | :--- | :--- |
| **High Point** | "Like them again; lost their rim protector, still like them" | ✓ Beat Wisconsin 83-82, then pushed Arkansas to 94-88 |
| Troy | Potential upset | ✗ Lost to Nebraska by 29 |
| Belmont | "Expect 1-2 wins if they make it" | Didn't make the field |
| Oakland · Arkansas State · Yale | Zone defense; sleeper; "James Jones always dangerous" | No deep run recorded |

The High Point call was the gem. Flagged two years running, delivered on the second flag, with the honest rim-protection caveat attached, and the run ended with dignity: Arkansas needed 36 points from future seventh overall pick Darius Acuff Jr. to close them out 94-88 in Round 2.

It also embarrassed one of Boston's own structural calls. He'd said there would be no Cinderella this year, maybe Ole Miss; the Cinderella turned out to be his own sleeper. His other structural note aged much better and is worth keeping for 2027: out-of-conference record tells you more about a tournament team than conference record does.

### The Consensus Test

KenPom's top 12 contained all four men's Final Four teams, at ranks 2 (Arizona), 3 (Michigan), 7 (Illinois), and 11 (UConn), while ranks 1, 4, 5, and 6 (Duke, Florida, Houston, Iowa State) all fell short. ESPN's and Sports Illustrated's "teams that can win it all" lists each named every eventual Final Four participant. The pool was never the problem.

That's the real finding here. Experts, efficiency rankings, and the model all converged on the same 7-8 legitimate contenders, and then everyone ordered that pool wrong in the same direction. Duke and Florida sat on top of every list; Michigan sat third on most of them and won. The edge in 2027 isn't finding the pool. It's having the discipline to de-prioritize its consensus top when the structural signals (Michigan's size and depth, Illinois's defense, UConn's coaching) point one rung down.

---

## Technical Notes, and Why It's Built This Way

| Component | Weight | Script | Why it's there |
| :--- | :---: | :--- | :--- |
| XGBoost on efficiency metrics (AdjOE/AdjDE, Barthag) | 50% | `src/04_predict_2026.py` | Adjusted efficiency is the most predictive public signal in college basketball; it earns the majority weight |
| Geospatial travel burden | 25% | `src/05_geospatial_distance.py` | Neutral-site tournaments aren't actually neutral; distance and time zones are real, and largely uncorrelated with efficiency |
| Momentum and rest engine | 25% | `src/06_momentum_and_fatigue.py` | Season-long averages smooth over late-season form; this term un-smooths them |

**Fusion:** 70% score fusion + 30% rank fusion (`src/08_cfa_fusion_backtester.py`). Score fusion preserves the magnitude of each agent's conviction; rank fusion disciplines the outliers when agents disagree. The 70/30 split came out of backtesting, not aesthetics.

**Probability clipping to [0.015, 0.985]:** log-loss insurance. A single confident wrong answer near 0.999 costs more than dozens of good calls earn back, so the clip caps the catastrophe.

**Injury guardrails** (`src/07_final_pro_ensemble.py`), manual, disclosed, and directional: Duke -6.5% (Caleb Foster), North Carolina -11% (Caleb Wilson, rim protection), Michigan -3% (precautionary). The Duke tax was the right idea at half the right size; the UNC tax paid for itself in the VCU leverage play.

**Simulation:** 10,000 Monte Carlo bracket runs per tournament (`src/11_monte_carlo_bracket.py`).

**Primary submission:** [`submission_2026_CFA_FUSION.csv`](./submissions/submission_2026_CFA_FUSION.csv), 132,134 matchup probabilities for the Kaggle March Machine Learning Mania 2026 competition.

**Methodology paper:** [CFA article (PDF)](./article/CFA_article.pdf)

---

*Tournament completed April 6, 2026. The short version of this story, built for scrolling: [project site](https://cedpaul13.github.io/March_Madness_2026/).*

[Back to README](./README.md)
