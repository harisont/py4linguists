# Alice through the NLP pipeline
In [Alice in Pythonland](alice_pythonland.md), you have done frequency analysis of Alice in Wonderland, finding the top 10 (or top $n$) most common words in the text. 
However, it would make sense if forms like "cat" and "cats" (the singular and plural of the same noun), "tall" and "taller" (the positive and comparative of the same adjectives), "she" and "her" (the nominative and accusative of the same pronoun) etc. were each counted as instances of the same word.
You can solve the problem by replacing each word in the text with its dictionary form, or _lemma_.
Use the functions `sentences()` and `lemmas()` from `nlp.py` to modify your code for the previous exercise so that it performs the same frequency analysis, but using lemmas rather than word forms.

## Hints
- Rather than directly splitting the text into words, you will initially need to use `sentences()` to segment it into sentences. This is because `lemmas()` works best on individual sentences and implicitly performs word segmentation by itself.
- Lemmatizing the whole text in `alice.txt` will take quite a while! It might be a good idea to add a `print` statement that tells you how many sentences are still left to process, or simply test your solution on just a small part of the text.
- Don't worry about the `Already downloaded a model for the 'en' language` messages. They come from one of the underlying NLP libraries.