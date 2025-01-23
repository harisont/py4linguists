# Syntax highlighting for natural language
According to the blog [linusakesson.net](linusakesson.net),

> _Syntax highlighting is a standard feature of most modern text editors and development environments. The basic idea is to exaggerate the visual difference between various syntactical elements, to make it easier for the programmer to distinguish between keywords, punctuation and variable names._

In the code snippet

```python
  def is_important(word):
     stopwords = ARTICLES + PREPOSITIONS + CONJUNCTIONS
     # one-line conditional :)
     return False if word.lower() in stopwords else True
```

for instance, keywords such as `def` and `return` are highlighted in green, values such as `True` and `False` are dark blue and comments are italicized and light blue. 

Many programmers find syntax highlighting helpful, whereas some, such as Linus Åkesson himself, think it is a terrible idea. After all, it would be absurd to syntax-highlight natural language -- why would we ever want to do that for code? 

...But is it actually _that_ crazy to syntax-highlight natural language? Try to do that and see for yourself.
With the help of `nlp.py`, write a function that takes a string of text as input and returns a [Markdown](https://www.markdownguide.org/basic-syntax/)-formatted string where 

- `NOUN`s, proper nouns (`PROPN`) and `VERB`s are highlighted in **bold** (to highlight a word in bold, you will need to surround that in `**`)
- `ADJ`s and `ADV`s are highlighted in _italics_ (to italicize a word, you will need to surround that in `_`)

For example:

```
  **Syntax** **highlighting** is a _standard_ **feature** of _most_ 
  _modern_ **text** **editors** and **development** **environments** . 
  The _basic_ **idea** **is** to **exaggerate** the _visual_ 
  **difference** between _various_ _syntactical_ **elements** , to 
  **make** it _easier_ for the **programmer** to **distinguish** 
  between **keywords** , **punctuation** and _variable_ **names** .
```

To render one such screen and make it look like 

> **Syntax** **highlighting** is a _standard_ **feature** of _most_ _modern_ **text** **editors** and **development** **environments** . The _basic_ **idea** **is** to **exaggerate** the _visual_ **difference** between _various_ _syntactical_ **elements** , to **make** it _easier_ for the **programmer** to **distinguish** between **keywords** , **punctuation** and _variable_ **names** .

you can paste it [markdownlivepreview.com](markdownlivepreview.com) or use any other markdown renderer.
Feel free to include your comments about this topic in your submission on Canvas.

## Extra challenge
If you know another markup language, such as HTML, you can try to do some more complex highlighting, for instance by using different colors for different parts of speech.