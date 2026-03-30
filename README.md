# Indonesian POS Ambiguity Resolution

Rule-based system to resolve part-of-speech ambiguity 
in Indonesian functional words using distributional features.

## Background

This project is based on the author's corpus linguistics research on 
syntactic category ambivalence in Indonesian. The study identified 
eleven lexical forms drawn from thirteen horror short stories published 
on Mojok.co that exhibit ambivalent syntactic behavior: *sejak, karena, 
sebelum, untuk, dengan, setelah, hingga, buat, sama, akan*, and *sampai*.

These words cannot be categorized based on lexical form alone — their 
syntactic category (preposition, subordinating conjunction, coordinating 
conjunction, adverb, or verb) is determined entirely by their 
distributional pattern and the type of constituent that follows them 
in the sentence structure.

This project operationalizes those distributional criteria into a 
rule-based NLP classifier, bridging linguistic theory and computational 
implementation.

## Words Covered

| Word | POS Categories | Distributional Basis |
|------|---------------|---------------------|
| karena | Subordinating CONJ / PREP | Followed by clause vs nominal phrase |
| untuk | Subordinating CONJ / PREP | Followed by clause vs nominal phrase |
| dengan | Subordinating CONJ / PREP | Followed by clause vs nominal phrase |
| sejak | Subordinating CONJ / PREP / ADV | Followed by clause vs nominal vs interrogative |
| sebelum | Subordinating CONJ / PREP | Followed by clause vs nominal phrase |
| setelah | Subordinating CONJ / PREP | Followed by clause vs nominal phrase |
| hingga | Subordinating CONJ / PREP | Followed by clause vs nominal phrase |
| buat | Subordinating CONJ / PREP | Followed by clause vs nominal phrase |
| sama | Coordinating CONJ / PREP | Connects equal elements vs followed by nominal |
| akan | ADV / PREP | Precedes verb vs followed by nominal phrase |
| sampai | VERB / ADV / PREP | Occupies predicate vs modifies verb vs followed by nominal |

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

| Method | Accuracy |
|--------|----------|
| Rule-based classifier | **82.89%** |
| ML extension (Logistic Regression) | 71.05% |

The rule-based system outperforms logistic regression due to the small 
dataset size (187 sentences). Linguistically-motivated rules prove more 
data-efficient in low-resource settings — a finding consistent with 
NLP research on morphologically rich and understudied languages.

**Per-word accuracy (rule-based):**

| Word | Accuracy |
|------|----------|
| dengan | 100% |
| hingga | 100% |
| setelah | 90.5% |
| karena | 89.7% |
| buat | 88.9% |
| untuk | 84.6% |
| akan | 80.0% |
| sebelum | 70.6% |
| sampai | 66.7% |
| sejak | 56.5% |

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