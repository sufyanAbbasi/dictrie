# Dictrie

> Note: this is Python 2.7 compatible, not Python 3 (for now)

## Trie Overview

A ***trie*** is a search tree that optimizes word dictionary traversal by organizing words in a tree, character by character. 

Given a dictionary containing **"hell", "hello",** and **"help"**, the following tree represents the words in our dictionary:
```
             h
             |
             e
             |
             l
            / \
           /   \
          p     l
          |    / \
          _   _   o
         
```

You can follow any path down the tree, keeping track of the characters, until you hit an underscore. At this point, you have a valid word. This data structure is particularly useful for efficient autocorrection or finding the shortest/longest word that starts with a given substring.

In Python, a trie can be represented with nested dictionaries like so:

```python
{'h': {'e' : {'l' : {'l': {
                            'o': {
                                  ' ': {}
                                },
                            ' ': {}
                        },
                     'p': {
                           ' ': {}
                          },
                    }
               }
      }
```

where, instead of an underscore, we indicate the end of valid word with a space and empty dictionary. 

This library extends common dictionary indexing to work with tries, for example, `trie['hel']` returns a subtrie:
```python
trie['hel']
>>> {'p': {' ': {}}, 
     'l': {' ': {}, 
           'o': {' ': {}}}}
```

and 

```python
'hello' in trie
>>> True
```

tests whether a key is contained in the trie. It also adds features like iterating over the words in the trie, etc.

### Quickstart

To start using `Dictrie`, clone this repository:

```bash
git clone https://github.com/sufyanAbbasi/dictrie
```

or download the `dictrie.py` file here: https://github.com/sufyanAbbasi/dictrie/dictrie.py

Move this file to your working directory (sorry, no `pip` yet!) and run the following:

```python
from dictrie import Dictrie

if __name__ == "__main__":
    #initialize a trie with an existing word list
    trie = Dictrie(['hell', 'help', 'hello'])
    
    #add some more words to the list
    trie.build_list(['hellish', 'hellcat'])
    
    #or
    
    for word in ['hellish', 'hellcat']:
        trie[' '] = word
    
    #access a subtrie:
    trie['hel']
    
    #test if a key exists in the trie:
    'hel' in trie
    
    #test if a word exists in the trie:
    trie.is_word('hello')
    
    #iterate over all the words in a trie
    for word in trie
        print word
        
    #iterate over the words that start with a given string:
    for word in trie.get_words('hell'):
        print word
    
```


### Initialization
Initialize a bare trie by:

```python
trie = Dictrie()
```

Or by supplying any number of iterables (list, set, etc.) of words:

```python
trie = Dictrie(['hell', 'help', 'hello'], {'hellish', 'hellcat'})
```

Or by supplying a trie with the `dict` keyword:

```python
trie = Dictrie(dict={'h':{e:{y:{' ': {}}}}})
```

### Building a Trie
The following two methods adds words to the dictionary:
As a function:
```python
trie.build_trie(['hell', 'help', 'hello'])
```
Through iteration:
```python
for word in ['hell', 'help', 'hello']:
    trie[' '] = word
```
Here, the key is ignored in this form and each word is automatically placed in the trie.

### Accessing a Subtrie
The Dictrie class extends dictionaries to allow indexing by word substrings. For example:
```python
trie['hel']
```
produces a subtrie of the words that start with the key:
```python
>>> {'p': {' ': {}}, 'l': {' ': {}, 'o': {' ': {}}}}
```

### Testing for Existence
The Dictrie class supports the ```in``` keyword, which checks if the sequence of characters exists in the trie:
```python
'hel' in trie
>>> True
```

To test if a valid word exists in the trie, use the ```is_word(<string>)``` method:
```python
trie.is_word('hel')
>>> False

trie.is_word('hello')
>>> True
```

### Iteration
```python
for word in trie:
    print word
```
prints every word in the trie, from shortest to longest:

```
>>> hell 
    help 
    hello
```

```trie.get_words(<string>)``` returns a generator that iterates over the words that begin with <string> in alphabetical order.

```python
for word in trie.get_words('hell'):
    print word
```
prints every word that begins with **hell** from shortest to longest:

```
>>> hell 
    hello
```

### Testing Dictrie:
[github.com/dwy/english-words](https://github.com/dwyl/english-words) is a fantastic github repo with over 450,000 english words. Download the text file, [words_alpha.txt](https://github.com/dwyl/english-words/blob/master/words_alpha.txt), and place it in your working directory, and run:

```python
with open('words_alpha.txt') as fp:
    for word in fp:
        trie[' '] = word.strip()
```

which builds a trie containing all of the available words. Then run:

```python
for word in trie.get_words('trie'):
    print word
```
to list all words in the dictionary which starts with **trie** in size order:

```
>>> tried
    trier
    tries
    triene
    triens
    triers
    triedly
    ...
    trieciously
    triennially
    trierarchal
    trierarchic
    trienniality
    trierarchies
    triethylamine
    triethanolamine
    triethylstibine

```

## To-Do List
* Limit key type to strings
* Figure out how to better deal with iteration on a subtrie
    * Iterate on the subtrie itself or the words in the list?
* Test for robustness

## Credit
Luciano Romalho's, [**Fluent Python**](http://shop.oreilly.com/product/0636920032519.do), is an amazing resource for taking your Python skill to the next level. I would highly recommend picking it up!