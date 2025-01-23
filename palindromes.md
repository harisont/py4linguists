# Palindromes 
According to [Wikipedia](https://en.wikipedia.org/wiki/Palindrome),

> A **palindrome** is a word, number, phrase, or other sequence of symbols that reads the same backwards as forwards, such as "madam" or "racecar".

Write a function that checks whether the input word is a palindrome. The function should return a boolean.

## Hint
To reverse a string, you can use the function

```python
def reverse(x):
    return x[::-1]
```

## Extra challenges
- Make the function case-insensitive, so that `your_function("Anna")` also returns `True`.
- The Italian sentence
    
    > I topi non avevano nipoti
    
    ('The mice did not have any grandchildren') would be a palindrome if it wasn't for the spaces.
    Adapt your to ignore spaces, so that `your_function("I topi non avevano nipoti")` also returns `True`.