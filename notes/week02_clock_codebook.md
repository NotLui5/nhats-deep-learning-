# Week 2 — NHATS clock-drawing codebook and teaching notes

## 1. Verified NHATS documentation (one named round)

- **Study:** National Health and Aging Trends Study (NHATS).
- **Selected round:** **Round 1 (2011)**.
- **Variable:** `cg1dclkdraw` — "R1 D SCORE OF CLOCK DRAWING TEST", in the Sample Person (SP) file, Cognition (CG) section.
- **Valid scores:** integers **0, 1, 2, 3, 4, 5**.
- **Direction:** higher = better. A lower *current* score than a valid *previous* score indicates worsening performance on this task.

| Score | Meaning in the NHATS clock-drawing scale |
|---|---|
| 5 | Accurate depiction of a clock |
| 4 | Reasonably accurate depiction |
| 3 | Mildly distorted depiction |
| 2 | Moderately distorted depiction |
| 1 | Severely distorted depiction |
| 0 | Not recognizable as a clock |

**Who is assessed / eligibility:** The Round 1 NHATS sample represents Medicare beneficiaries aged 65 or older. The clock task belongs to the cognitive assessment given to sample persons interviewed in the community or in residential care other than nursing homes. If an interview uses a proxy, the proxy must permit asking the sample person cognitive questions, and the sample person must be able to participate. The interviewer asks the person to draw a clock showing 11:10, allowing two minutes. The code `-1` denotes people for whom the task is inapplicable (in Round 1, `r1dresid` equal to 3 or 4). Eligibility does **not** mean that everyone completed the task.

### Raw missing/special codes for `cg1dclkdraw` in Round 1

| Raw value | Codebook meaning |
|---|---|
| -1 | Inapplicable |
| -2 | Proxy says the sample person cannot be asked |
| -3 | Proxy permits asking, but the sample person cannot answer |
| -4 | Sample person did not attempt the clock drawing |
| -7 | Sample person refused to draw the clock |
| -9 | Missing |

**Crucial:** The six negative codes are **not** low cognitive scores; they describe different reasons why no valid clock score is present. Do not input them into this week's function. Converting raw NHATS codes to Python `None` is **outside Week 2's scope** (planned for Week 4).

**Official sources (checked November 14, 2026):**

1. Freedman, V. A., Schrack, J. A., & Skehan, M. E. (2026). *National Health and Aging Trends Study User Guide: Rounds 1–14, Final Release.* NHATS. See cognitive assessment section, clock scoring methodology, and **Appendix III, p. 148**, which specifies `cg#dclkdraw` for Rounds 1–11 and its raw special codes.  
   https://nhats.org/sites/default/files/public-documentation/NHATSUserGuideR14_02102026.pdf
2. Kasper, J. D., & Freedman, V. A. (2012). *NHATS Round 1 User Guide: Final Release.* See the cognition section, scoring methodology (**p. 57**), and **Appendix III, p. 75** (`cg1dclkdraw`).  
   https://nhats.org/sites/default/files/2021-01/NHATS_Round_1_User_Guide_Final_Release_0.pdf

> The teaching exercise compares **synthetic** scores at two times. Selecting Round 1 documents the meaning of the scale; it does not mean that the exercise uses actual longitudinal NHATS records. Verify each round's definitions before real-world longitudinal analysis.

## 2. Decision rule used in the script

- If **either** score is `None`: return `None` (unknown).
- **Otherwise**, if `current < previous`: return `True` (decline).
- **Otherwise**: return `False` (same or improved).

The Python script has one required function, uses `if` / `elif` / `else`, and contains no loops or additional functions.

### Six synthetic calls — expected results (written before execution)

| Scenario | Previous | Current | Expected output | Reason |
|---|---:|---:|---|---|
| Decline | 5 | 3 | `True` | 3 is less than 5 |
| Improvement | 2 | 4 | `False` | 4 is greater than 2 |
| No change | 3 | 3 | `False` | Scores are equal |
| Zero is a valid score | 1 | 0 | `True` | Zero is a valid measured score and is less than 1 |
| Missing previous | `None` | 3 | `None` | Cannot compare without a previous score |
| Missing current | 4 | `None` | `None` | Cannot compare without a current score |

### Observed outputs after running the script

```text
1. Decline     | Expected: True  | Observed: True
2. Improvement | Expected: False | Observed: False
3. No change   | Expected: False | Observed: False
4. Zero score  | Expected: True  | Observed: True
5. Previous NA | Expected: None  | Observed: None
6. Current NA  | Expected: None  | Observed: None
```

**All six observations agree with the six expectations.**

## 3. Key explanations for trainees

**Why `is None`, not `if not previous`?** Because `not 0` is `True` in Python, even though **0 is a valid NHATS score**. The condition `previous is None` checks for a missing value without confusing it with zero.

**`None`, `0`, and `False` are different:** `None` means that the score is unavailable; `0` means the lowest valid clock score; and `False` is the function's Boolean result meaning no decline was found. Raw NHATS codes such as `-1` and `-9` are numbers with codebook-defined reasons for absence, not Python `None`.

**Parameters versus arguments:** `previous` and `current` are parameters in the `def` line; in `is_worsening(5, 3)`, `5` and `3` are arguments.

**`return` versus `print`:** `return` sends a result back to code that called the function; `print` only displays something in the terminal.

**Boolean logic:** `or` means that **at least one** score is missing; `and` requires both statements to be true; and `not` reverses a Boolean value. The function needs `or` because either missing score prevents a valid comparison.

## 4. Short clinical reflection

**Does a decline in clock score establish a dementia diagnosis? No.** This is one brief cognitive task, not a definitive diagnostic test. Performance can be affected by many factors (for example, fatigue, sensory or motor difficulties, acute illness, and testing variability), and a score difference does not by itself establish persistent cognitive and functional decline. Dementia assessment requires a fuller clinical history, functional evaluation, and appropriate cognitive and medical assessment.

## 5. Terminal and GitHub steps

Within your **existing** `nhats-deep-learning` project (no second repository):

```bash
conda activate nhats-course
cd path/to/nhats-deep-learning
python src/week02_conditions.py
```

After checking that the six observed outputs match expectations:

```bash
git status
git add src/week02_conditions.py notes/week02_clock_codebook.md
git commit -m "Complete Week 2 conditions and functions"
git push
```

Finally, verify both files and the latest commit in your existing private GitHub repository and give the assessor access as instructed by your course organiser.
