# Indonesian POS Ambiguity Resolution

Rule-based system to resolve part-of-speech ambiguity 
in Indonesian functional words using distributional features.

## Background

Indonesian functional words like *karena*, *untuk*, *sejak*, 
and *dengan* can function as different parts of speech 
depending on their syntactic context. This project 
operationalizes linguistic distributional criteria to 
automatically classify them.

## Words Covered

| Word | POS Categories |
|------|---------------|
| karena | CONJ / PREP |
| untuk | CONJ / PREP |
| dengan | CONJ / PREP |
| sejak | CONJ / PREP / ADV |
| sebelum | CONJ / PREP |
| setelah | CONJ / PREP |
| hingga | CONJ / PREP |
| sampai | CONJ / PREP / VERB / ADV |
| akan | ADV / PREP |
| buat | CONJ / PREP |

## Method

The system extracts syntactic features from the 
constituent following the ambiguous word:

- **has_predicate** — detects verb prefixes (me-, ber-, di-, ter-)
- **has_pronoun** — detects subject pronouns
- **has_modal** — detects modal verbs
- **token_length** — length of following constituent

These features feed into a rule-based classifier 
grounded in linguistic distributional analysis.

## Dataset

- 187 sentences from Indonesian fiction corpus
- Manually annotated with gold-standard POS labels
- Source: Setiawan (2022)

## Results

| Metric | Score |
|--------|-------|
| Overall Accuracy | **82.89%** |
| Best word (dengan, hingga) | 100% |
| Weakest word (sejak) | 56.5% |

## Error Analysis

Main sources of error:
- Verbs without standard prefixes (e.g. *pergi*, *duduk*)
- Implicit predicates in informal speech
- Ambiguous short constituents (1 token)

## Project Structure
```
indonesian-pos-ambiguity/
├── dataset/
│   └── dataset.csv
├── src/
│   ├── preprocess.py
│   ├── features.py
│   ├── classifier.py
│   ├── main.py
│   └── visualize.py
├── results/
│   ├── results.csv
│   ├── error_analysis.csv
│   └── accuracy_chart.png
└── README.md
```

## Future Work

- ML extension using logistic regression
- Expand to more Indonesian functional words
- Handle implicit predicates and ellipsis