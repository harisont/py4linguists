# Vocab training
In this exercise, you will work with a word list for learners of Swedish: [`adj.csv`](adj.csv) (adapted from [L2Lex-Adj](https://spraakbanken.gu.se/en/resources/l2lex-adj)) contains a long list of adjectives from textbooks for learners of Swedish as a second language at different proficiency levels along with their absolute frequencies in the textbooks.

For example, the segment 

```
acceptabel,B1,1
acceptabel,C1,5
äcklig,A1,1
äcklig,A2,3
äcklig,B1,5
äcklig,B2,1
äcklig,C1,1
```

means that the word "acceptabel" never appears in learning materials targeting learners at level A2 or lower, whereas "äcklig" is used across proficiency levels A1-C1, but more common at level B1.

Read this file and store this information in a nested dictionary, using the words as top-level keys to avoid redundancy.

Then, use the dictionary to produce two custom word lists:

1. a frequency list where adjectives are sorted from most to least common _independently_ from proficiency level (e.g. "äcklig", which appears a total of 11 times should be learned before "acceptabel", which only occurs 6 times)
2. a list where adjectives are sorted _first_ by minimum proficiency level and _then_ by their frequency at that particular level. Do not repeat the same adjective twice, even if it appears at multiple proficiency levels.

(what order do you think makes the most sense for a language learner?)

Write a Python program that produces output in format 1 or 2 based on the value of a configuration variable `FORMAT`.

## Extra challenges
- make `FORMAT` a command-line parameter
- use the Karp API (see [documentation](https://ws.spraakbanken.gu.se/docs/karp)) to query the Saldo morphological dictionary to also retrieve the comparative and superlative of each adjective. Example request for "äcklig" (try it in your web browser): 
 
  ```
  https://spraakbanken4.it.gu.se/karp/v7/query/saldom?q=equals|baseform|äcklig
  ```

  Note that `msd` in the output stands for "morphosyntactic descriptor". The descriptors for (nominative) comparative and superlative are, repsectively, "komp nom" and "super indef nom" (there is also a "super _def_ nom", but let's keep things simple).