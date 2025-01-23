# Alice in Pythonland
The file [alice.txt](alice.txt) contains the full text of Lewis Carroll's _Alice in Wonderland_.
The goal of this exercise is to do a frequency analysis of this text.
Your program should list the top 10 most frequent words of the book and how many times they occur. 

## Basic approach: counting on lists
You can start by converting the text into a list of words.
Once you have that, a possible approach is to iterate over them and use the `.count()` method to find out how many times it occurs in the text. 
Store the words and their counts as a list of pairs.
Finally, use the function `sorted()` to order the list it based on word counts and write a loop that prints the top 10 word-count pairs.

## Advanced approach: dictionaries
The solution above, however, is computationally inefficient because every time you call `.count()` the whole list is searched again to find all occurrences of the word at hand.
A way to solve this problem is to build a dictionary where keys are words and values are their number of occurrences in the text.
Try iterating over the words and checking if the current word is already a key in the dictionary.
If it is not, add a new key-value pair, initializing the word's count at 1.
If it is, update their count by 1.
In this way, the text is only scanned once.
For the last step, however, you will still need to store word-count pairs in a sortable data structure, such as a list.
To convert the dictionary to a list of word-count pairs, you can use the `.items()` method. 

## Hint: converting the text into a list of words
The text is provided in a lowercased and _tokenized_ version, which means, among other things, that there is a space separating punctuation marks from the words closest to them. It and looks like this:

  ```
  chapter i . down the rabbit-hole
  alice was beginning to get very tired of sitting by her sister on the bank , and of having nothing to do : once or twice she had peeped into the book her sister was reading , but it had no pictures or conversations in it , ‘ and what is the use of a book , ’ thought alice ‘ without pictures or conversations ? ’
  ```

  This means that you can obtain words by simply splitting the text on whitespaces.

## Hint: using `sorted()` 
Note that `sorted()` will by default look at the first element of each pair. 
This means that, if the first element of each list item is a the word (and not the count), the list will be sorted alphabetically.
There are many ways to fix this, the most straightforward  being building the list by hand ensuring that you have count-word pairs rather than word-count pairs.
For a more advanced and compact solution, check the [documentation for `sorted()`](https://docs.python.org/3/library/functions.html#sorted).

You will then need to convert the dictionary into a list, sort it based on the word counts and write a loop that prints the top 10 word-count pairs.
To convert the dictionary to a list of word-count pairs, you can use the `.items()` method and to sort the list you can use the function `sorted()`. 

## Extra challenges
- Punctuation is very common and will likely appear among your top 10 words. Try to make it so that punctuation marks are not counted as words.
- Make the input file and the number of top words to display configurable. The program could read them as [command-line arguments](https://www.geeksforgeeks.org/how-to-use-sys-argv-in-python/).