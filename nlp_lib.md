# `nlp.py`: a mini Natural Language Processing library
For some of the exercises in this collection, you will need to use an external module, [`nlp.py`](nlp.py).

This module provides four basic Natural Language Processing functions that allow you to:

1. guess the language of a text;
2. segment it into sentences;
3. lemmatize it (i.e. getting the dictionary form of all words it is composed of), and last but not least
4. assign grammatical categories (aka part-of-speech tags) to each of its words.

You can learn more about what these functions' input and output types by checking out their docstrings.

Note that using `nlp.py` requires installing two third-party modules, `langid` and `spacy_udpipe`.
On most Python installations, both should be easy to get via `pip`, e.g.

```
pip install langig
```

If you feel extra confident, you can ignore `nlp.py` and try to use these third-party libraries directly.
However, `spacy_udpipe` is object-oriented and its documentation may be difficult to navigate at first.