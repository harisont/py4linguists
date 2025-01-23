
# Title case
According to [Wikipedia](https://en.wikipedia.org/wiki/Title_case),

> _**Title case** or **headline case** is a style of capitalization used for rendering the titles of published works or works of art in English. When using title case, __all words are capitalized, except for minor words (typically articles, short prepositions, and some conjunctions) ~~that are not the first or last word of the title~~__. There are different rules for which words are major, hence capitalized. As an example, a headline might be written like this: "The Quick Brown Fox Jumps over the Lazy Dog"._

Write a function `is_title_case()`, which checks whether an input string is in already formatted in title case (if you are a beginner, you can ignore the strikethroughed part of the definition).
Then, test your function by calling it in a script that asks the user to write some text and tells them whether the string is correctly formatted in title case or not.

## Hints
- try out the `.istitle()` method in the Python shell on a few strings. How does its behavior differ from what you are asked to implement?
- think about the function that you need to implement. What is its _type_, i.e. what should it take as input and return as output?
- like in [Palindromes](palindromes.md), you will need to split the text into words. Then you can use a `for` loop to iterate over them
- the simplest way to decide whether a word needs capitalization is to check if it belongs to a list of articles, prepositions and conjunctions

## Extra challenges
- implement `to_title_case()`, which formats an arbitrary string into title case
- instead of hardcoding a list of "minor" words into your Python script, store those words in an separate text file and make it so that your program reads from it