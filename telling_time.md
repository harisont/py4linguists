# Telling the time
Write a function that converts times in `HH:MM` (24h) format into text in a language of your choice, e.g.

```python
>>> time = "8:30"
>>> to_eng(time)
"It is half past eight"
>>> to_swe(time)
"Klockan är halv nio"
>>> to_ita(time)
"Sono le otto e mezza"
```

Based on your level of experience, you can make this exercise as easy or as complex as you want. 
For example, you can use a simpler textual format, such as

```python
>>> time = "8:30"
>>> to_eng(time)
"It is eight thirty"
>>> to_swe(time)
"Klockan är åtta och trettio"
>>> to_ita(time)
"Sono le otto e trenta"
```

What to do with times such as 15:45 is also up to you. 
Anything from

```python
"It is fifteen fortyfive"
```

to 

```python
"It is quarter to four"
```

is a valid answer.

## Extra challenge
Use the [datetime module](https://docs.python.org/3/library/datetime.html) to make the program tell the current time (this should be easy for everyone to do after lecture 5).