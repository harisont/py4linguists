# Python dictionaries as... dictionaries

## An interactive programming lexicon
Write a command-line application that awaits for an English word from the user input and uses a dictionary built from [this list of programming-related terms](https://raw.githubusercontent.com/aarneranta/python-course-gbg/refs/heads/master/data/terms.csv) to output its Swedish translation.

### Hints
To build a dictionary our of the lexicon listed above:

1. save the lexicon as a plain text file
2. open it and read its content from Python, dividing it into lines
3. initialize a dictionary
4. for each line:
   - check if it is empty or starts with a `#` character (in these cases, you can ignore the entire line)
   - if this is not the case, split it into a "Swedish segment", an "English segment" and a "grammatical segment" (`N` stands for "noun", `A` for "adjective" and `V` for "verb")
   - if the "English segment" contains only one term, as in line
      ```
      språk ; language ; N
      ```
      add the dictionary an item whose key is the English word and whose value(s) is/are the Swedish translation(s). For the moment, you can ignore the grammatical category
    - if, on the other hand, the "English segment" is a list of comma-separated terms, as in
      ```
      tilldelningssats ; assignment statement , assignment ; N
      ```
      create _several_ key-value pairs (in this case, one for "assignment statement" and one for "assignment"). Remember to ignore whitespace

To retrieve elements from your dictionary, use key indexing, e.g.

```python
>>> your_dict("assignment")
tilldelningssats
```

### Extra challenge
Make the dictionary bilingual, i.e. allow the user to get both Swedish translations of English words and vice versa. 
Is one dictionary sufficient to achieve this goal, or do you need two?

## Interlude: Nested dictionaries
Replace the English-Swedish dictionary in the previous exercise with one that also include word class information.
It should look something like

```python
{
    "progamming": {
        "translations": ["programmering"], 
        "class": "N"
    },
    ...
    "programming language": {
        "translations": ["programspråk", "programmeringsspråk"],
        "class": "N"
    },
    ...
}
```

Update your code so that the user still gets the translations of the words they request. Optionally, you can show the word class alongside the Swedish translation of the word. 

## Back to the printing press
Use the nested dictionary from the previous exercise to produce a text file formatted as a simple paper dictionary.
The English words should be sorted alphabetically and divided into sections by their first letter. 
Suggested output format:

```
A
AI (noun): artificiell intelligens, AI
algorithm (noun): algorithm
animation (noun): animering
artificial intelligence (noun): artificiell intelligens, AI
...

B
block (noun): block
...
```

### Extra challenge
Use [Markdown syntax](https://www.markdownguide.org/basic-syntax/) to further improve the output. 
You can render Markdown to HTML on [markdownlivepreview.com](markdownlivepreview.com) or use any other markdown renderer. 