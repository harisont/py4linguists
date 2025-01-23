
# Title case
According to [Wikipedia](https://en.wikipedia.org/wiki/Title_case),

> _**Title case** or **headline case** is a style of capitalization used for rendering the titles of published works or works of art in English. When using title case, __all words are capitalized, except for minor words (typically articles, short prepositions, and some conjunctions) ~~that are not the first or last word of the title~~__. There are different rules for which words are major, hence capitalized. As an example, a headline might be written like this: "The Quick Brown Fox Jumps over the Lazy Dog"._

In this exercise, you are going to write a function, `is_title_case()`, which checks whether an input string is in already formatted in title case (if you are a beginner, you can ignore the barred part of the definition).
We are then going to use them in an interactive program.

Especially if you are new to programming, try to follow these steps:

1. try out the `.istitle()` method in the Python shell on a few strings. How does its behavior differ from what you are asked to implement?
2. think about the function that you need to implement. What is its _type_, i.e. what should it take as input and return as output?
3. start implementing `is_title_case()`. The first thing to do is again to split the input string into words
4. write a loop to iterate over the words obtained in the previous step. This code is pre-written in `hints.py`
5. add a conditional statement that checks whether the word needs capitalization (__hint:__ a possible approach is to check whether the word belongs to an extensive list of articles, prepositions and conjunctions. It might be a good idea to implement this check as a function)
6. if it does, use `.istitle()` or string indexing to check that the first character of the word is in fact uppercase 
7. add return statements where necessary
8. test your function by calling it in a script that asks the user to write some text and tells them whether the string is correctly formatted in title case or not (__hint:__ you can use the built-in `input()` function)

## Extra challenge
Implement `to_title_case()`, which formats an arbitrary string into title case.