# Multilingual title case
In [Title case](title_case.md), you implemented a function `is_title_case()` that checks whether a string is formatted in title case (and possibly a function `to_title_case()` that formats the given string in title case -- if not, you may want to do it now). 

At some point, both of these functions need to decide whether a word in "important" enough to deserve capitalization. 
During the lab, I suggested you to do that by relying on lists of "minor" English words, also known as "stopwords". 
However, it is difficult to make these lists exhaustive, especially if you are compiling them yourself.
In addition, the solution you get is - unless you implemented multiple lists for different languages - language-specific.

Modify your solution using the functions in [`nlp.py`](nlp.py). 
The goal is to write a function that guesses the language of the input string and relies on part-of-speech tagging to decide whether a word is "important" or not.
You can consider "minor" all words that are categorized as `DET` (determiner, which includes articles), `ADP` (adposition -- pre- or postposition), `CCONJ` (coordinating conjunction) and `SCONJ` (subordinating conjunction). 
If you are curious, the full list of POS tags used in `nlp.py` is available [here](https://universaldependencies.org/u/pos/index.html).


## Hints

- You can assume that the input string is a single sentence.
- Again, you do not need to perform word segmentation yourself.