# Unified Personality Theory

An open project to test Myers-Briggs-style type theory, keep the parts that survive, and build on them. Anyone can check the work, rerun it, or prove it wrong. The research stays free.

The name is a goal and makes no claim. Nothing here is a unified theory yet.

**Independent project.** This repo is not affiliated with or endorsed by The Myers & Briggs Foundation or The Myers-Briggs Company. MBTI and Myers-Briggs are their trademarks, used here only to refer to their instrument and theory. This repo contains no official test items.

## Where things stand

| Question | Evidence so far | Status |
|---|---|---|
| Are the four scale scores reliable? | Retest correlations of about .80 to .87, with Thinking-Feeling the weakest | Fairly well supported, but many of the figures come from the publisher |
| Do people fall into two natural groups on each scale? | Taxometric work and score distributions point to continuous traits | Evidence leans against types |
| Why do so many people change type on retest? | [Our calculation](#first-result-type-changes-need-no-special-explanation): reliability plus a midpoint cut predicts about 53-59% | Model result, needs real retest data |
| What do the scales measure? | They overlap four of the Big Five. None tracks Neuroticism | Replicated |
| Does type predict job or team outcomes? | We found no MBTI-specific meta-analysis | Open. The publisher itself rules out hiring use |
| Does the cognitive function stack hold up? | The direct tests we could locate argue against it, and we have only seen them second-hand | Barely tested |

Read this before relying on any of it: **this is a first pass made with AI agents.** Most journal articles were paywalled, so many claims rest on abstracts, search summaries or Wikipedia. Each source is marked with how much of it was read. Every DOI was looked up on Crossref and resolves to the expected paper, which shows the paper exists but does not show the claim about it is right. Checking the claims against the full papers is the most useful thing you can contribute.

## First result: type changes need no special explanation

Half of people changing type within weeks is the most quoted criticism of the MBTI. We asked how much change you would expect if nobody's personality moved at all and scores simply had their reported reliability.

| Retest correlation per scale | Keeps each letter | Changes four-letter type |
|---|---|---|
| .81 on all four | 80.1% | 58.9% |
| .86 on all four | 83.0% | 52.6% |
| .75, .75, .61 (T-F), .75 | 75.5% | 67.6% |

Reported retest studies, as relayed by secondary sources, give about 83% per letter and about 50% changing type at nine months in one study, and 39-76% changing type at about five weeks across others.

This cuts both ways. Flips are not evidence of an unusually noisy test, since scale scores this reliable produce them when cut at the middle. They also mean the four-letter label is much less stable than the scores behind it, which is a reason to report scores and drop the label.

Limits: the model assumes normal, independent scales cut at the median, and the comparison figures are second-hand. It shows the numbers are consistent with continuous traits, and does not rule out real categories measured with noise. To reproduce it, run `python analysis/h2_type_stability.py`.

## What's here

- [research/](research/) has four literature reviews, with every claim graded:
  - [01 Psychometrics](research/01-psychometrics.md)
  - [02 Validity](research/02-validity.md)
  - [03 Functions and theory](research/03-functions-and-theory.md)
  - [04 Open data and ways to expand](research/04-open-data-and-expansion.md)
- [HYPOTHESES.md](HYPOTHESES.md) lists tests fixed before seeing results, and proposed extensions to the theory.
- [analysis/](analysis/) has scripts that use only the Python standard library.
- [CONTRIBUTING.md](CONTRIBUTING.md) explains how to help, including the rules for AI-assisted work.

## Run it

Python 3.10 or newer, nothing to install.

```bash
python analysis/h2_type_stability.py
```

```bash
python analysis/h1_bimodality.py --self-check
```

```bash
python analysis/check_dois.py
```

## Join in

Pick a claim and check it against the source. Pick a hypothesis and run it. Believers and skeptics are both welcome, and a result against your own view is the most valuable kind. Start with an issue, a discussion or a pull request, and see [CONTRIBUTING.md](CONTRIBUTING.md).

## Not for

This is research. Do not use anything here to hire, diagnose, or make decisions about a person.

## Licence

Free to use, share and build on, including commercially.

- Research and writing: [CC BY-SA 4.0](LICENSE). Credit the project and share adaptations under the same licence, so the research stays open.
- Code: [MIT](LICENSE-CODE).

Datasets and instruments we link to keep their own terms. To cite this work, use "UnifiedPersonalityTheory contributors" and the repo URL.
