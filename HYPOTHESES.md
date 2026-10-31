# Hypotheses

Each test states its decision rule before the result is known, and git history shows when. If you change a rule after seeing data, say so here. All data must come from real people. Model-simulated answers do not count.

## Tests

### H1. The traits behind the scales are continuous, not two-peaked

- **Claim tested:** type theory says people sort into two groups on each preference.
- **Status: run once, supported on the proxy, with a real limit (below).** Data is `BIG5.zip` (N = 19,719; SHA-256 `67953298d75d3279d0486e7f4ec0195efc26a9e790b15e511cbcf4551751ba53`) from the [Open Psychometrics raw data page](https://openpsychometrics.org/_rawdata/). The page states no licence, so the data stays out of this repo.
- **Proxy:** no open dataset of MBTI-style scale scores was found, so this uses IPIP Big Five scores for the four traits the scales overlap (E, O, A, C), with N as a comparison. It tests the underlying traits and not the official instrument.
- **Decision rule per trait:** `continuous` if the bimodality coefficient is at or below 5/9 and the smoothed histogram has one mode. `two-peaked` if the coefficient is above 5/9 and there are two or more modes. Anything else is `mixed`. The type claim counts as unsupported here if E, O, A and C are all `continuous`.
- **Run:** `python analysis/h1_bimodality.py path/to/data.csv`
- **Result (2026-10-31):** all five traits came out `continuous`, so the type claim is unsupported on this proxy.

  | Trait | n | Bimodality coefficient | Modes | Verdict |
  |---|---|---|---|---|
  | Extraversion | 19,718 | 0.438 | 1 | continuous |
  | Neuroticism (comparison) | 19,718 | 0.420 | 1 | continuous |
  | Agreeableness | 19,718 | 0.448 | 1 | continuous |
  | Conscientiousness | 19,718 | 0.384 | 1 | continuous |
  | Openness | 19,718 | 0.412 | 1 | continuous |

- **Limits:** these are Big Five scores from online volunteers, not MBTI scales. Simulation (`analysis/simulate_methods.py`) also shows this rule misses weak categories. A two-peaked verdict needs a pure category, a second mode appears once the category share of stable variance reaches about 0.7, and a share of 0.6 still reads as `continuous`. So this result rules out strong categories only. The simulation's normal scores give a lower coefficient (0.364) than the real data, so the coefficient alone is not a clean measure here. The single mode is the informative part. A taxometric test on item-level data is the stronger follow-up.

### H2. Reliability alone explains type changes on retest

- **Status: model calculated, real test open.** See the [README](README.md#first-result-type-changes-need-no-special-explanation). With retest correlations of .81 to .86, the model predicts 52.6-58.9% changing type. Simulation shows correlation between scales up to .4 barely moves this (55.8% to 55.1%).
- **Real test:** with scale scores from a retest sample of at least 1,000, compare observed type stability to the model using each scale's observed correlation and actual score distribution.
- **Decision rule:** the hypothesis fails if observed whole-type stability differs from the model by more than 5 percentage points, in either direction, at a retest gap of 12 weeks or less. More stability than predicted would favour real categories.

### H3. The ordered function stack adds nothing to the four scales

- **Status: open, needs new data** from a function-level measure and a pre-specified behavioural outcome.
- **Decision rule:** compare a model using four continuous scales with one adding stack-order terms. The stack is supported if it improves cross-validated R-squared by at least .02 in two independent samples.

### H4. Scales add nothing beyond the Big Five

- **Status: open, needs a sample with both measures** and an outcome such as well-being or job satisfaction.
- **Decision rule:** the hypothesis fails if the four scales add more than .02 R-squared over all five Big Five domains in cross-validation.

### H5. Type reports feel accurate whether or not they match

- **Status: open, needs a consented experiment.** No test using randomised MBTI-style descriptions was found.
- **Design:** participants rate their true report and a randomly chosen one, blind to which is which.
- **Decision rule:** the hypothesis is supported if the mean accuracy ratings differ by less than 10% of the scale range. It fails if matched reports rate clearly higher.

## Proposed extensions

These are ideas for building on type theory. None is established. Each needs a test of its own before it moves up.

1. **Scores with uncertainty in place of letters.** Report each scale as a score with the probability of each pole given measurement error, so someone near the cut is not told they are simply one letter. The H2 result motivates this, and it can be built from reliability figures alone.
2. **A fifth scale for emotional stability.** No MBTI scale tracks Neuroticism. 16Personalities' Identity scale is a commercial take on the same gap, with publisher-only evidence. Test whether adding it improves prediction (H4 data would answer this).
3. **An open, public-domain type measure.** No open instrument with published reliability and raw data was found. OEJTS has a non-commercial licence and its data is listed as forthcoming. Build scales from public-domain IPIP items and publish reliability and validity with the data.
4. **Types as a tested model.** Fit mixture models to open trait data and report what share of people can be confidently assigned out of sample. The evidence for data-driven types is disputed, so this could fail outright.
5. **Function-level behaviour over time.** If functions exist as Jung described them, day-to-day behaviour within a person should show them. Experience-sampling methods can test this without relying on any one questionnaire.

Add your own by pull request. A hypothesis needs a result that would count against it.
