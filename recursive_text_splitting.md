# Recursive text splitting
Large Language Models can only handle a certain amount of _tokens_ (~words) at a time.
A common solution to this problem is to split the text as soon as that limit is reached and process the rest separately.
However, this can lead to a situation where the text is split in a way that isn't optimal for the task at hand. 

For example, if our model can only process 6 words at a time, the simplest way to split the text

> My name is Susanna . I study Language Technology . I live in Gothenburg .

would be

> My name is Susanna . I _(6 tokens)_

> study Language Technology . I live _(6 tokens)_

> in Gothenburg . _(3 tokens)_

However, this is a lucky case where the length of each sentence is such that the model could process each of them individually, probably resulting in better performance:

> My name is Susanna . _(5 tokens)_

> I study Language Technology . _(5 tokens)_

> I live in Gothenburg . _(5 tokens)_

Write an alternative splitting function `sentence_aware_split()` that, given a text and a maximum length, tries to split it using sentence boundaries as much as possible. 
Follow this algorithm:

- __base case__: if the text is shorter than the maximum length, return a list containing a single string -- the full text
- otherwise (__recursive case__):
  1. divide the text into two similarly-sized parts, using sentence boundaries (full stops, question and exclamation marks) to decide where to split. If there are no sentence boundaries, you can use other punctuation or just split the text in half. You may use `nlp.sentences()` here
  2. apply `sentence_aware_split()` to both halves, so that the text is further split if necessary
  3. return the results in (flattened, i.e. not nested) list. To flatten the list, you may use the function
      
      ```python
        def flatten(xss): return [x for xs in xss for x in xs]
      ```
  
For the example above, with maximum length 5, the result should be

```python
  ["My name is Susanna .", 
   "I study Language Technology .", 
   "I live in Gothenburg ."]
```

You mat assume that the text is tokenized as in the example above, with punctuation being separated from the closest word.