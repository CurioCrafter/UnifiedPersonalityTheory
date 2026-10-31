# Open data, testable claims and ways to expand MBTI theory

Strand 4 of the skeptical MBTI review. Research date: 2026-10-31. Factual summary, not legal advice. Source status is marked per source; several facts come from web-search result summaries and are flagged.

## Bottom line

The public-domain IPIP pool and Open Psychometrics' Big Five, HEXACO and 16PF-style raw files are the cleanest open material for testing type claims. The OEJTS, the open MBTI-like scale, has no raw dataset on the Open Psychometrics raw-data page: its development page calls its data "forthcoming", so the project cannot assume any OEJTS data exists. The text datasets (Kaggle MBTI, PANDORA) rely on self-reported types, and the Kaggle set has documented label leakage and label noise. The best-supported expansion routes are dimensional (Big Five/aspects, HEXACO) and, for individuals, person-specific dynamics. Latent "types" remain contested. LLM output should be treated as a hypothesis generator or a measurement-tool comparison, never as human evidence. The official MBTI items and marks are protected, so the project must describe itself as an independent study and must not reproduce items.

## Open data and instruments

| Name | URL | N | Licence / access | Redistribution allowed? | Known problems |
|---|---|---|---|---|---|
| Open Psychometrics raw-data index | https://openpsychometrics.org/_rawdata/ | 47 datasets listed | Free download; page states respondents were told answers would be used for research and non-consenting responses were removed; no explicit licence on page | Not stated. Treat as unknown; link, do not mirror, until the owner confirms | No OEJTS or MBTI dataset among the 47 titles listed (page read via fetch summary). Self-selected online volunteers |
| OEJTS 1.2 (instrument) | https://openpsychometrics.org/tests/OEJTS/ | Development screening: 25,568 people familiar with type; 2,230 respondents for crowdsourced items | Items and page content under CC BY-NC-SA 4.0 (per development page) | Items: yes with attribution, non-commercial, share-alike. Raw data: none published | Development page reports no reliability, no Big Five correlations, no scoring formulas, data "forthcoming". "Most accurate" claim is the developer's own and its comparison figures were not seen |
| OEJTS item-wording discrepancy | same | n/a | n/a | n/a | Development page says 48 items (12 per scale) selected; the test page says 60 items in two sections. Reason not stated on pages read |
| IPIP item pool | https://ipip.ori.org/ | n/a (item pool) | Public domain; copy, edit, translate, use without permission or fee | Yes | No MBTI/Jungian-type scale listed on the home page. Only Big Five-style and other trait scales found |
| IPIP Big Five Factor Markers data | https://openpsychometrics.org/_rawdata/ (file IPIP-FFM-data-8Nov2018.zip) | 1,015,342 | Free download; terms as for index | Unstated | Volunteer web sample; country mix skewed; page gives no column names |
| BIG5.zip (IPIP-based, 50 items) | same index | 19,719 | as above | Unstated | Small relative to FFM file |
| HEXACO.zip (IPIP-equivalent, 240 items) | same index | 22,786 | as above | Unstated | Volunteer sample |
| 16PF.zip (IPIP items, 163 items) | same index | 49,159 | as above | Unstated | Volunteer sample |
| IPIP-NEO (Johnson) data | Johnson 2014 instrument; the Gerlach et al. paper used his 120- and 300-item web data | >1.5M across four sets in Gerlach et al. | IPIP-NEO items are public domain (IPIP). Whether Johnson's raw data are downloadable was not verified | Unknown | Web volunteers; see Could not verify |
| Kaggle MBTI (Personality Cafe) | https://www.kaggle.com/datasnaek/mbti-type (not opened; handle as shown in search results) | 8,675 users, last 50 posts each | Licence not confirmed | Unknown, check page | Self-reported types; Li et al. estimate about 31% label leakage, about 16% noise, about 29% incorrect labels (self-report) |
| PANDORA | https://arxiv.org/abs/2004.04460 | >10k Reddit users, >17M comments; Big Five labels for >1.6k users; MBTI and Enneagram also | Access terms not found on arXiv abstract page | Unknown, check authors' release | Labels are self-reported and voluntary; Reddit text terms apply |
| MbtiBench (re-annotated Kaggle/Twitter/PANDORA test sets) | https://arxiv.org/abs/2412.12510 | test sets only | Not checked | Unknown | Small cleaned test sets with soft labels from three annotators |

## Candidate extensions

Each grade is about the evidence for the model as an extension or replacement of type, not a verdict on MBTI.

1. **Big Five domains as the replacement frame [Strong].** McCrae and Costa (1989) found the four MBTI indices measure parts of four Big Five domains (E, O, A, C), with no counterpart to Neuroticism, and that the scores are continuous rather than type-like [1]. Test: regress OEJTS-style scores on IPIP Big Five scores in a new sample; compare incremental validity for outcomes.
2. **Aspects and facets (hierarchical Big Five) [Moderate].** DeYoung, Quilty and Peterson (2007) found two aspects per domain, giving ten, in a community sample of 481 [5]. Useful for asking whether the S/N and T/F scales map to specific aspects. Single-sample evidence; replication status not checked here.
3. **HEXACO [Moderate].** Ashton and Lee (2007) argue a sixth factor (Honesty-Humility) adds predictive ground the Big Five misses [6]. Abstract only; HEXACO IPIP-equivalent data exist (22,786). Relevance to MBTI is indirect: it tests whether any four-scale model omits important variance.
4. **Latent profile / mixture "types" [Contested].** Gerlach et al. (2018) report four types across four large datasets using a constrained clustering method [2]. Freudenstein et al. (2019) argue the types are neither robust nor exhaustive, reporting only 42% of people assignable, with assignments about as uncertain as a coin toss; the original authors replied that their empirical findings hold but share the concern about use in assessment [3]. Both critique and reply are known only from search summaries. Test: pre-register mixture models with out-of-sample assignment confidence on IPIP data, and report the share of people classifiable.
5. **Network psychometrics [Weak for personality types].** Borsboom and Cramer (2013) is a psychopathology review proposing symptoms as causally interacting [7]. Applying it to type scales would be a new use. Abstract only; no MBTI-specific evidence found.
6. **Person-specific / experience-sampling work [Moderate as a method, Weak as support for type].** Beck and Jackson (2020) found idiographic ESM network models heterogeneous across people, and contemporaneous (not lagged) models consistent over time [8]. Abstract only. Supports testing "does a person's day-to-day behaviour sort into stable type-like patterns", which is a direct test of type theory.
7. **Text-derived measurement [Weak].** See the LLM section and dataset problems. Evidence is limited by self-report labels.

## LLMs in personality research: what is safe and what is not

Safe uses (all as tools, with human data as the ground truth):
- Drafting and cleaning code, codebooks, and literature summaries, with every claim checked against a source.
- Comparing an LLM's trait inference to human self-report as a *measurement-tool evaluation*. Peters and Matz (2024) report zero-shot GPT-3.5/GPT-4 Big Five inference from Facebook status updates correlated about r = 0.29 on average with self-report, similar to supervised models, with accuracy varying by age and gender group [9]. This is modest validity, from search summaries and an open PMC page not fully read.
- Re-labelling or auditing text datasets, as MbtiBench does with human annotators, not LLM labels alone [4].

Not safe:
- Treating LLM-simulated respondents as a human sample. Argyle et al. (2023) show "algorithmic fidelity" for some political survey outcomes with GPT-3 [10], but a 2025 critique (summarised in search results, not read) argues LLMs can misrepresent population opinion and under-represent minority views, and the fidelity test used aggregate statistics.
- Treating LLM Big Five-style answers as having human psychometric structure. Petrov et al. (arXiv 2405.07248) report that generic personas gave promising but imperfect properties, demographic-specific personas gave poor results, and the responses were poor signals of latent traits [11]. A secondary review of that paper (not the paper itself) reports inflated intercorrelations between traits.
- Treating zero-shot binary trait classification as reliable. Di Cursi et al. (2025) report no configuration was consistently reliable across five models and three datasets, and that aggregate accuracy can hide large per-class asymmetries [12].
- Using LLM output to estimate type distributions, factor structure, reliability or validity in the repo's results. Label any such output "simulated, not human evidence". LLM output may be used only to generate hypotheses and test materials.

## Trademark and copyright facts

Factual summary, not legal advice.

- **Marks.** The Myers-Briggs Company's trademarks page lists "Myers-Briggs Type Indicator", "Myers-Briggs", "MBTI", "Step I/II/III" and the MBTI logo as marks of the Myers & Briggs Foundation, Inc., and lists other marks (CPI, FIRO-B, Strong Interest Inventory, TKI) under The Myers-Briggs Company [13]. A third-party listing derived from USPTO data shows MBTI registered to the Foundation (Reg. no. 2525809) [14]. Sources disagree in places on which entity is named; verify at USPTO before relying on this.
- **Usage guidance.** Search-result summaries of the Company's trademark guidelines say the marks should be used as adjectives with a noun ("the MBTI assessment"), not as nouns, with a trademark acknowledgement, and that reproducing the marks requires a written licence [14]. I could not open the guideline PDF itself (one URL returned 404, another redirected), so the exact wording is unverified. The guidance found does not address critical, descriptive or comparative use.
- **Copyright.** The Company's Copyright and Permissions page says the instrument, individual items, answer sheets, reports, scoring tools, tables and norms are protected; reproducing, posting online, altering or translating any part requires prior written approval, and no separate research exemption is described [15]. The MBTI is also a restricted-purchase instrument requiring certification or qualifying education [15].
- **Practical consequences for this project** (descriptive, not legal advice): describe the work as an independent, non-affiliated study of "Myers-Briggs-style" or "MBTI"-labelled type theory; use the marks only to refer to the official instrument, as adjectives; do not name the project or domain with the marks; do not reproduce, paraphrase item-by-item, or host official items or scoring keys; use open instruments instead (OEJTS under CC BY-NC-SA, IPIP public domain). Note that the OEJTS's non-commercial share-alike licence constrains any derived repo licence.

## Sources

1. McCrae, R. R., and Costa, P. T. (1989). Reinterpreting the Myers-Briggs Type Indicator from the perspective of the five-factor model of personality. Journal of Personality 57(1), 17-40. DOI 10.1111/j.1467-6494.1989.tb00759.x; https://pubmed.ncbi.nlm.nih.gov/2709300/ . **Abstract only** (via search summary).
2. Gerlach, M., Farb, B., Revelle, W., and Nunes Amaral, L. A. (2018). A robust data-driven approach identifies four personality types across four large data sets. Nature Human Behaviour 2, 735-742. DOI 10.1038/s41562-018-0419-z . **Abstract only** (search summary).
3. Freudenstein, J.-P., Strauch, C., Mussel, P., and Ziegler, M. (2019). Four personality types may be neither robust nor exhaustive. Nature Human Behaviour (Matters Arising); and Gerlach et al. (2019), Reply, Nature Human Behaviour 3, 1047-1048. https://amaral.northwestern.edu/publications/reply-four-personality-types-may-be-neither-robust-nor-exhaustive/ ; press release https://idw-online.de/en/news724322 . **Abstract only** (search summaries).
4. Li et al. (2024/2025, COLING 2025). Can large language models understand you better? An MBTI personality detection dataset aligned with population traits. https://arxiv.org/abs/2412.12510 ; https://arxiv.org/html/2412.12510v1 . **Full text read** for first 100,000 of 105,642 characters via fetch summary.
5. DeYoung, C. G., Quilty, L. C., and Peterson, J. B. (2007). Between facets and domains: 10 aspects of the Big Five. J. Pers. Soc. Psychol. 93(5), 880-896. https://pubmed.ncbi.nlm.nih.gov/17983306/ . **Abstract only**.
6. Ashton, M. C., and Lee, K. (2007). Empirical, theoretical, and practical advantages of the HEXACO model of personality structure. Pers. Soc. Psychol. Rev. 11, 150-166. DOI 10.1177/1088868306294907 . **Abstract only**.
7. Borsboom, D., and Cramer, A. O. J. (2013). Network analysis: an integrative approach to the structure of psychopathology. Annu. Rev. Clin. Psychol. 9, 91-121. https://pubmed.ncbi.nlm.nih.gov/23537483/ . **Abstract only**.
8. Beck, E. D., and Jackson, J. J. (2020). Consistency and change in idiographic personality: a longitudinal ESM network study. J. Pers. Soc. Psychol. 118(5), 1080-1100. https://profiles.wustl.edu/en/publications/consistency-and-change-in-idiographic-personality-a-longitudinal-/ . **Abstract only**.
9. Peters, H., and Matz, S. C. (2024). Large language models can infer psychological dispositions of social media users. PNAS Nexus. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11211928/ . **Abstract only** (search summary).
10. Argyle, L. P., et al. (2023). Out of one, many: using language models to simulate human samples. Political Analysis 31(3), 337-351. DOI 10.1017/pan.2023.2; https://arxiv.org/abs/2209.06899 . **Abstract only**.
11. Petrov, N. B., et al. (2024). Limited ability of LLMs to simulate human psychological behaviours: a psychometric analysis. https://arxiv.org/pdf/2405.07248 . **Abstract only** (search summary).
12. Di Cursi et al. (2025). Mind reading or misreading? LLMs on the Big Five personality test. https://arxiv.org/abs/2511.23101 . **Abstract only** (search summary). Full author list not seen.
13. The Myers-Briggs Company. Trademarks of The Myers-Briggs Company. https://themyersbriggs.com/en-US/Support/Trademarks . **Full text read** (via fetch summary).
14. The Myers-Briggs Company / CPP. Trademark Guidelines (PDF), and USPTO-derived listing: https://www.mbtionline.com/-/media/MBTIonline/Files/Trademark_Guidelines.pdf ; https://markinton.com/trademark/mbti-75809336 . **Abstract only** (search summaries; PDF not opened).
15. The Myers-Briggs Company. Copyright and Permissions. https://themyersbriggs.com/en-US/Support/Copyright-and-Permissions . **Full text read** (via fetch summary).
16. Open Psychometrics. Raw data index. https://openpsychometrics.org/_rawdata/ . **Full text read** (via fetch summary).
17. Jorgenson, E. (2014). Development of the Open Extended Jungian Type Scales. https://openpsychometrics.org/tests/OEJTS/development/ ; test page https://openpsychometrics.org/tests/OEJTS/ . **Full text read** (via fetch summaries).
18. Goldberg, L. R. et al. International Personality Item Pool. https://ipip.ori.org/ . **Full text read** (home page, via fetch summary).
19. Gjurkovic, M., Karan, M., Vukojevic, I., Bosnjak, M., and Snajder, J. (2021). PANDORA Talks: personality and demographics on Reddit. NLP for Social Media workshop, NAACL 2021. https://arxiv.org/abs/2004.04460 . **Abstract only**.
20. Johnson, J. A. (2014). Measuring thirty facets of the Five Factor Model with a 120-item public domain inventory (IPIP-NEO-120). J. Res. Pers. 51, 78-89. DOI 10.1016/j.jrp.2014.05.003 . **Abstract only** (search result via secondary hosts).

## Could not verify

- Any OEJTS raw dataset, file name, URL, column names, scoring formulas or numeric coding. None appears on the raw-data page; the development page says data are forthcoming. The OEJTS test page and a third-party npm reimplementation (@openmbti/core) mention 8 items per dimension with a threshold of 24, but that is unofficial and not confirmed.
- OEJTS reliability and Big Five correlations (none on the pages read), and the figures behind the "most accurate" comparison claim.
- Data licence for the raw-data files and whether redistribution is permitted.
- Kaggle MBTI dataset licence, and the PANDORA access terms.
- Whether Johnson's IPIP-NEO raw data are publicly downloadable.
- Full text of the Myers-Briggs Company trademark guidelines PDF, and any guidance on descriptive, critical or comparative use of the marks; the legal position of fair or nominative use.
- Full texts of items 1-3 and 5-12 and 19-20 (abstracts or summaries only), and the 2025 critique of silicon samples (Li, Li and Qiu) as described in a search summary.
- The claim of inflated Big Five intercorrelations in LLM data (from a secondary review of item 11).
- Replication status of the DeYoung aspects and the Gerlach types beyond the sources listed.
