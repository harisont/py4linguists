In this lab, you are going to practice using lists, strings, dictionaries, (nested) loops and -- if you want an extra challenge -- recursion. 
For most of the exercises, you are also going to use an external module, `nlp.py`.

This module provides four basic Natural Language Processing functions that allow you to:

1. guess the language of a text;
2. segment it into sentences;
3. lemmatize it (i.e. getting the dictionary form of all words it is composed of) and last but not least
4. assign grammatical categories (aka part-of-speech tags) to each of its words.

You can learn more about what these functions' input and output types by checking out their docstrings.

To use `nlp.py`, you will need to install two external libraries, `langid` and `spacy_udpipe`.
On most Python installations, both should be easy to get via `pip`.

The point with `nlp.py` is to allow you to focus on the topics of today's lab.  
If you feel extra confident, you can ignore it and try to use these third-party libraries directly.
However, `spacy_udpipe` is object-oriented and its documentation may be difficult to navigate at first.

# Alice through the NLP pipeline
In the previous exercise, you have done frequency analysis of Alice in Wonderland, finding the top 10 (or top $n$) most common words in the text. 
However, it would make sense if forms like "cat" and "cats" (the singular and plural of the same noun), "tall" and "taller" (the positive and comparative of the same adjectives), "she" and "her" (the nominative and accusative of the same pronoun) etc. were each counted as instances of the same word.
You can solve the problem by replacing each word in the text with its dictionary form, or _lemma_.
Use the functions `sentences()` and `lemmas()` from `nlp.py` to modify your code for the previous exercise so that it performs the same frequency analysis, but using lemmas rather than word forms.

## Hints
- Rather than directly splitting the text into words, you will initially need to use `sentences()` to segment it into sentences. This is because `lemmas()` works best on individual sentences and implicitly performs word segmentation by itself.
- Lemmatizing the whole text in `alice.txt` will take quite a while! It might be a good idea to add a `print` statement that tells you how many sentences are still left to process, or simply test your solution on just a small part of the text.
- Don't worry about the `Already downloaded a model for the 'en' language` messages. They come from one of the underlying NLP libraries.