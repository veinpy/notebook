# Snokel Notebook

---

### SnorkelSession
> 和database链接的功能

---

### DocPreprocessor
> 文本预处理。
>
> **TSVDocPreprocessor**

---

### CorpusParser
> document -> sentences -> tokens -> NER
> 
> Spacy OR jieba

---

### Generat Candidates
> 抽取candidates (是一个object)

#### Define Candidate Schema
> subclass of **Candidate**

#### CandidateExtractor
> **ContextSpace**,  define "space" of all candidates we consider
> 
>		比如 **Ngrams** subclass
> 
> **Matcher** 过滤candidates
> 
> **CandidateExtractor**
> 
> 		UDF， 提取labeling用的candidates

---

### Creating and Modeling a Noisy Training Set

#### Labeling Functions
> 
> Pattern-based LFs
> 	commono sense text paterns
> 
> Distant Supervision LFs
> 	load a list of known candidates and 
> 	check to see if the candidate pair matches 
> 	one of these
> 
> 	Developing Labeling Functions

#### Applying Labeling Functions
> **LabelAnnotator** class, 生成 Labels 和 LabelKeys
> 
> Note that this will delete any existing Labels and LabelKeys for this candidate set

#### Fitting the Generative Model