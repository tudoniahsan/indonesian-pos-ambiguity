# Indonesian POS Ambiguity Resolution

Rule-based system to resolve part-of-speech ambiguity
in Indonesian functional words using distributional features.

## Background

This project grew out of my undergraduate thesis on syntactic category ambivalence in Indonesian functional words. The central problem I was working with is deceptively simple: certain Indonesian words cannot be assigned a part-of-speech category based on their lexical form alone. Their syntactic category — whether they function as a preposition, subordinating conjunction, coordinating conjunction, adverb, or verb — is determined entirely by the distributional context they appear in, particularly the type of constituent that follows them in the sentence structure.

The theoretical basis for this comes from Zellig Harris's distributional linguistics, which holds that the syntactic identity of a word is defined by the environments it can occupy. For the words in this project, that means the category can only be resolved by looking at what comes after them.

The corpus was built from thirteen horror short stories published in Mojok.co's *Malam Jumat* column, all written by a single author, Setiawan, in 2022. The texts were collected manually from the website and compiled into a single corpus file. The genre matters as context: these are informal, first-person supernatural narratives, which means the language reflects natural colloquial Indonesian rather than formal written register — a useful source for observing how these ambiguous words actually behave in real usage.

Sentences were extracted using AntConc concordance software by searching for each target word, then manually classified by the author based on the distributional criteria established in the thesis. This process yielded 222 annotated sentences covering eleven target words: *sejak, karena, sebelum, untuk, dengan, setelah, hingga, buat, sama, akan,* and *sampai*. One note on scope: *sama* as an adjective was excluded from the analysis because its category shift is not determined by the following constituent, placing it outside the distributional framework this project applies. Only its preposition and coordinating conjunction uses are included.

The project then operationalizes those distributional criteria into a rule-based NLP classifier, bridging the linguistic analysis from the thesis into a working computational implementation.

## Words Covered

| Word | POS Categories | Distributional Basis |
|------|---------------|---------------------|
| karena | Sub.CONJ / PREP | Followed by clause vs. nominal phrase |
| untuk | Sub.CONJ / PREP | Followed by clause vs. nominal phrase |
| dengan | Sub.CONJ / PREP | Followed by clause vs. nominal phrase |
| sebelum | Sub.CONJ / PREP | Followed by clause vs. nominal phrase |
| setelah | Sub.CONJ / PREP | Followed by clause vs. nominal phrase |
| hingga | Sub.CONJ / PREP | Followed by clause vs. nominal phrase |
| buat | Sub.CONJ / PREP | Followed by clause vs. nominal phrase |
| sejak | Sub.CONJ / PREP / ADV | Followed by clause vs. nominal phrase vs. interrogative word |
| sampai | VERB / ADV / PREP | Occupies predicate position vs. modifies verb vs. followed by nominal phrase |
| akan | ADV / PREP | Precedes verb vs. followed by nominal phrase |
| sama | Co.CONJ / PREP | Connects equal constituents vs. followed by nominal phrase |

## Dataset

The dataset consists of 222 sentences drawn from thirteen horror short stories published in Mojok.co's *Malam Jumat* column in 2022, all authored by Setiawan. Sentences were extracted using AntConc concordance software and manually classified by the author based on distributional criteria derived from Zellig Harris's distributional linguistics framework.

The corpus covers eleven Indonesian functional words that exhibit syntactic category ambivalence: *sejak, karena, sebelum, untuk, dengan, setelah, hingga, buat, sama, akan,* and *sampai.* The distribution across words and categories is as follows:

| Word | Categories | Sentences |
|------|-----------|-----------|
| untuk | Sub.CONJ (21), PREP (20) | 41 |
| karena | Sub.CONJ (20), PREP (14) | 34 |
| dengan | PREP (16), Sub.CONJ (14) | 30 |
| sejak | PREP (13), Sub.CONJ (9), ADV (2) | 24 |
| akan | ADV (19), PREP (3) | 22 |
| setelah | Sub.CONJ (17), PREP (4) | 21 |
| sebelum | Sub.CONJ (13), PREP (4) | 17 |
| sama | PREP (5), Co.CONJ (2) | 7 |
| sampai | ADV (3), PREP (3), VERB (3) | 9 |
| buat | PREP (7), Sub.CONJ (2) | 9 |
| hingga | PREP (4), Sub.CONJ (4) | 8 |
| **Total** | | **222** |

### Sources

All thirteen source texts are from Mojok.co's *Malam Jumat* column, authored by Setiawan (2022):

1. [Gunung Semeru: Lagu Pilu di Balik Keagungan Mahameru](https://mojok.co/maljum/gunung-semeru-lagu-pilu-di-balik-keagungan-mahameru/)
2. [Gunung Slamet: Mengantarmu Pulang ke Samarantu (Bagian 2)](https://mojok.co/maljum/gunung-slamet-mengantarmu-pulang-ke-samarantu-bagian-2/)
3. [Gunung Slamet: Mengantarmu Pulang ke Samarantu (Bagian 3 - Tamat)](https://mojok.co/maljum/gunung-slamet-mengantarmu-pulang-ke-samarantu-bagian-3-tamat/)
4. [Mengantarmu Pulang ke Samarantu: Kisah Sosok Kinanti](https://mojok.co/maljum/mengantarmu-pulang-ke-samarantu-kisah-sosok-kinanti/)
5. [Rumah Kontrakan Arini](https://mojok.co/maljum/rumah-kontrakan-arini/)
6. [Kontrakan Arini Bagian 2: Semua Berawal dari Gunung Argopuro](https://mojok.co/maljum/kontrakan-arini-bagian-2-semua-berawal-dari-gunung-argopuro/)
7. [Perumahan di Ujung Sawah: Misteri Kunjungan Almarhum Nenek](https://mojok.co/maljum/perumahan-di-ujung-sawah-misteri-kunjungan-almarhum-nenek/)
8. [Sampai Bertemu di Gunung Arjuno](https://mojok.co/maljum/sampai-bertemu-di-gunung-arjuno/)
9. [Sampai Bertemu di Gunung Arjuno (Bagian 2)](https://mojok.co/maljum/sampai-bertemu-di-gunung-arjuno-bagian-2/)
10. [Gunung Arjuno: Sebuah Pesan Kematian dari Sisi Lain Pulau Jawa (Bagian 3)](https://mojok.co/maljum/gunung-arjuno-sebuah-pesan-kematian-dari-sisi-lain-pulau-jawa-bagian-3/)
11. [Asrama Itu Berdiri di Atas Lahan Pemakaman (Bagian 1)](https://mojok.co/maljum/asrama-itu-berdiri-di-atas-lahan-pemakaman-bagian-1/)
12. [Asrama Itu Berdiri di Atas Lahan Pemakaman (Bagian 2)](https://mojok.co/maljum/asrama-itu-berdiri-di-atas-lahan-pemakaman-bagian-2/)
13. [Asrama di Atas Tanah Kuburan: Kisah Kelam yang Tidak Tuntas (Bagian 3 - Tamat)](https://mojok.co/maljum/asrama-di-atas-tanah-kuburan-kisah-kelam-yang-tidak-tuntas-bagian-3-tamat/)

## Method

The classifier works on a simple but linguistically motivated principle: for all eleven target words, the key disambiguation signal lies in the type of constituent that follows them. If the following constituent contains a predicate — meaning it functions as a clause — the target word is a conjunction. If it is a nominal phrase without a predicate, the target word is a preposition.

To operationalize this, the system extracts four features from the constituent following each target word:

- **has_predicate** — detects the presence of verbal prefixes (*me-, ber-, di-, ter-*), which typically mark an active or passive verb in Indonesian, signaling that the following constituent is a clause
- **has_pronoun** — detects subject pronouns, which often co-occur with predicates in clause-initial positions
- **has_modal** — detects modal verbs (*akan, bisa, harus,* etc.), another indicator of clause structure
- **token_length** — measures the length of the following constituent, since clauses tend to be longer than nominal phrases

These features feed into a rule-based classifier where the decision logic is grounded directly in the distributional criteria from the thesis. The main challenge this approach faces is with verbs that lack standard prefixes — bare verbs like *pergi* or *duduk* are common in colloquial Indonesian but invisible to prefix-based detection. This is one of the primary sources of misclassification, discussed further in the Error Analysis section.

## Results

| Method | Sentences Evaluated | Accuracy |
|--------|-------------------|----------|
| Rule-based classifier | 215 | **82.33%** |
| ML extension (Logistic Regression) | 43 (test set) | 76.74% |

The rule-based system outperforms logistic regression, which is consistent with findings in low-resource NLP settings — linguistically-motivated rules tend to be more data-efficient than statistical models when training data is limited. It is worth noting that the two methods are not evaluated on identical conditions: the rule-based classifier was evaluated on all 215 sentences, while logistic regression used an 80/20 train/test split and was evaluated on 43 sentences only. This limits direct comparison but reflects the exploratory nature of the ML extension.

Seven sentences containing *sama* were excluded from both evaluations. As discussed in the Method section, *sama*'s category shift is not determined by the following constituent, placing it outside the distributional framework this system applies.

**Per-word accuracy (rule-based):**

| Word | Correct | Total | Accuracy |
|------|---------|-------|----------|
| hingga | 8 | 8 | 100.0% |
| dengan | 28 | 30 | 93.3% |
| setelah | 19 | 21 | 90.5% |
| buat | 8 | 9 | 88.9% |
| untuk | 35 | 41 | 85.4% |
| karena | 29 | 34 | 85.3% |
| akan | 18 | 22 | 81.8% |
| sebelum | 12 | 17 | 70.6% |
| sejak | 15 | 24 | 62.5% |
| sampai | 5 | 9 | 55.6% |

## Error Analysis

The main sources of misclassification fall into five categories.

**1. Verbs without standard prefixes**

The `has_predicate` feature relies on detecting verbal prefixes (*me-, ber-, di-, ter-*). This fails for bare verbs common in colloquial Indonesian — words like *pergi, masuk, tinggal, datang, bekerja* carry no detectable prefix but function as predicates. This is the primary source of error for *sebelum* and *sejak*, where five out of seventeen and five out of twenty-four sentences respectively were misclassified for this reason.

**2. Non-standard predicates**

Some constituents contain predicates that fall outside standard prefix patterns. *kebelet* in *saat itu kebelet pipis* is a colloquial predicate without a prefix, and *clear* in *semua clear* is an English loanword functioning as an adjectival predicate. Neither is detectable by the current feature set, causing these clauses to be misidentified as nominal phrases.

**3. Implicit subjects with bare verb predicates**

For *untuk*, constituents like *kembali ke basecamp*, *datang ke asrama*, and *tidak panik* contain bare verbs with implicit subjects — a common pattern in Indonesian infinitival clauses. The classifier correctly identifies these as CONJ based on constituent structure, but this also means the system is sensitive to any bare verb, including cases where context would suggest otherwise.

**4. Interrogative constituents in *sejak***

The two ADV instances of *sejak* — *sejak kapan kamu percaya* and *sejak kapan Kinanti meminjam* — were consistently misclassified as CONJ. The interrogative constituent *kapan kamu percaya* contains the pronoun *kamu*, which triggers `has_pronoun` and pushes the prediction toward CONJ. A dedicated rule for interrogative words like *kapan* would resolve this.

**5. *Akan* as preposition**

All three PREP instances of *akan* were misclassified as ADV. The current rule uses `token_length == 1` as the sole PREP signal, which is too narrow — nominal phrases like *kenangan akan almarhumah Arini* and *sikap tetangga di kampung ini* are multi-token but still function as prepositional complements. Detecting PREP *akan* likely requires semantic rather than purely distributional features.

## Future Work

- **Expand the corpus** beyond 222 sentences and beyond a single author and genre. The current dataset comes entirely from one author's horror narratives on Mojok.co, which limits generalizability to other registers of Indonesian.
- **Handle non-standard predicates** by extending `has_predicate` to cover bare verbs, colloquial forms, and loanword predicates — the primary source of misclassification in this system.
- **Add an interrogative rule for *sejak*** to correctly identify the ADV category when followed by *kapan* or other interrogative words.
- **Refine *akan* as preposition** using semantic features or a dedicated lexical list of nominal phrases that typically follow prepositional *akan*.
- **Extend to regional languages** — the distributional framework applied here is theoretically applicable to similar functional word ambiguity in Bahasa Sunda and other regional languages of Indonesia, where NLP resources remain severely limited.
- **Neural extension** — a BERT-based classifier using IndoBERT could leverage sentence-level context to resolve cases where constituent-level features are insufficient, particularly for *sampai* and *sejak*.

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
│   ├── visualize.py
│   └── ml_classifier.py
├── results/
│   ├── results.csv
│   ├── error_analysis.csv
│   └── accuracy_chart.png
└── README.md
```

## Usage

```bash
# Install dependencies
pip install pandas scikit-learn

# Run rule-based classifier
python src/main.py

# Run ML extension
python src/ml_classifier.py
```

## About

Rule-based POS ambiguity resolution for Indonesian functional words, grounded in Zellig Harris's distributional linguistics framework. Based on undergraduate thesis research on syntactic category ambivalence in Indonesian.
