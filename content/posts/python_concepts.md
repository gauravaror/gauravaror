---
title: "Python_concepts"
date: 2020-10-31T16:51:02+11:00
draft: false
---

# Python Concept: One day at a time #

## Python dunder methods ##

Python functions which start with a double underscore are known as dunder -- du(double) under(underscore) functions. They are majorly used for overriding the functionality of class in python (think OOPs).

If you define a new class. When you try printing this class instance, python prints a cryptic string which contains the name of the class and its memory address. You can implement `__repr__` function to define how it should be printed.

You can also implement `__add__` to define the behaviour how adding something to the object should work.


## Class Objects

A variable which is defined directly inside the class is called a class variable. You can access them via `self`.

```
class NLP:
    taste = "sweet"
```
class variables should not be mutable objects, but if used should be used with caution. Consider the example below:

```
In [1]: class NLP: 
   ...:     tools = [] 
   ...: anlp = NLP()                                                                                                                                                    
In [2]: bnlp = NLP()                                                                                                                                                    In [5]: anlp.tools.append('spacy')                                                                                                                                      
In [6]: bnlp.tools.append('nltk')                                                                                                                                       
In [7]: anlp.tools                                                                                                                                                      
Out[7]: ['spacy', 'nltk']
```
Adding `spacy` to `anlp` instance added `spacy` for `bnlp` instance as well. This behaviour can be undesirable in cases where another instance removes a tool you were currently using. This might create an issue while debugging as your object is being fiddled by another instance.

Just wondering this could be a desirable behaviour as well. In this case, because this could enable sharing knowledge of available tools across different instances. In all, mutable objects as class variables should be used with caution.

Detailed description: [Python tutorial on Classes](https://docs.python.org/3/tutorial/classes.html)
