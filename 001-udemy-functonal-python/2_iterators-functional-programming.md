# Iterators in Functional Programming with Python

* Iterator is an object that contain multiple other objects. Iterator is like a
  container of other objects. Several of them are: tuple, list, set and dict

## Built-in Iterators
* List (is a mutable sequence with a fixed order)
* Tuple (is an immutable sequence with a fixed order)
* Dict (a mutable key/value mapping without a fixed order)
* Set (an immutable collection of unique elements without a fixed order)
* Unpacking (pythonic technique in which you assign the elements from an
  iterator from a list in one go to multiple variables) - it's way to have
  multiple variables on the left hand assignments `plus, minus, divide, multiply = '+', '-', '/',
  '*'`

### Using a List - Mutable Sequences of Elements with a Fixed Order
* Iterators
  * An iterator is an object that contains multple other objects (is a collection
    of elements)
    * There are various kin iterators
      * Some are built into Python (such as a list, tuple, dict, set)
        * Others you can create yourself (you can create your own generator
          function which is a particular kind of iterator)
  * Functional programming relies heavily on Iterators! (map, filter, reduce)

* Mutatibility
  * An object is mutable if you can change it
    * An object is immutable if you cannot change it
      * Instead you perform a function on it (a function returns a new
        object, instead of changing the object)

* Functional programming doesn't mutate objects! 
  * Take one object, transform it and create a new object or `unwrap(transform(wrap(...)))`

* Order
  * An iterator is ordered if the elements are in a predictable order
    * An iterator is unordered if the elements are in an unpredictable order

#### List is Mutable and Ordered

```py
# Basic List Operations
l = ['Paris', 'Oslo', 'Budapest']
l.append('Kiev')
l.append(1, 'Berlin')
l.remove(0)
kiev = l.pop()


# Slicing
paris = l[0]
# Slicing from to
cities = l[1:3:1] # from positon 1 to positon 3 in steps of 1
# Slicing from to has default if we don't specify the values
cities = l[1:] # from position 1 till the end of the list in steps of 1
cities = l[::] # from positon 0 till the end of the list in steps of 1
# To reverse a list you can use this hack
cities = l[::-1] # from the end till the beggining (negative steps reverse the
order)

# Copying
l1 = ['Pairs', 'Oslo', 'Budapest']
l2 = l1.copy() # copy method creates a copy of the list
# l2 = l1[:] # also creates a copy of the list, it's no longer passed by
reference. It creates a full slice of a List
l1.append('Kiev')
```

### Using a Tuple - Immutable Sequences of Elements with a Fixed Order
* A tuple is immutable and it's ordered
  * Tuples are similar to lists
    * Slightly more efficient and immutable
* List or Tuple? 
  * Lists for large sequences of similar elements
  * Tuples for short sequences of dissimilar elements
  * **This reflects habit more than anything else - it's a convention - IMPORTANT**

```py
t = 'John', 24 # you can also define a tupe by putting round brackets ()
# Sine tuple is immutable we cannot add or remove elements from it, what we can do is concatinate
t = t + ('Berlin')

# Loop through the elements using for statement
for e in t:
  print(e)

# Check if elements exist in the tupe
'John' in t # True
'Johny' in t # False

# Repeat tuple
len(3 * t) # 9 
```

### Using a Dict - Mutable, Key-value Mappings Without a Fixed Order
* Dict is a collection of key => value mappings
* To find an element in a list or tuple, you use the element's position (index)
* Elements in a dict don't have a position
  * Instead, you find elements by their key
  * Keys can be (almost) any Python object
* No order
  * Although you can loop through dict objects
  * The order of the elements is not guaranteed
  * So don't assume a fixed order


```py
# Dict is mutable you can simply add or remove values from a dict
d = {
  'Praying Mantis'  : 'Insect',
  'Whale'           : 'Mammal'
}

del d['Whales']
# adding a new key value
d['Lizard'] = 'Reptile'

# you get the keys
for species in d:
  print(species)

# you get the values
for class_ in d.values():
  print(class_)

# to get both keys / values
for species, class_ in d.items():
  print(species, class_)

# while there is something in my iterator
# works with lists, tuples and any kind of iterator
# while len(d) > 0:
while d:
  # popitem() removes something from a dictionary and returns it  - removed from
  the dict
  species, class = d.popitem()
  print(species, class_
```

### Set - Immutable Collections of Unique Elements Without a Fixed Order

```py
mammals = {'Human', 'Whale', 'Dog', 'Cat', 'Human'}
print(mammels)
# {'Human', 'Whale', 'Dog', 'Cat'}

mammals.add('Mouse')


pets = {'Dog', 'Cat', 'Goldfish'}

# Union
print(mammals | pets)
# {'Human', 'Cat', 'Dog', 'Goldfish', 'Whale'}

# Intersection
print(mammals & pets)
# {'Dog', 'Cat'}

# Differnce
print(mammals - pets)
# Only Whale and Human because they are not in pets
# {'Whale', 'Human'}
```

### Unpacking Iterators by Assigning to Multiple Variables

```py
animals = 'Praying Mantis', 'Ant', 'Whale', 'Lizard'
a1, a2, a3, a4 = animals
print(a1, a2, a3, a4)
# Praying Mantis, Ant, Whale, Lizard 

# This tuple is nested and has a hierarchy
animals_by_class = ('Praying Mantis', 'Ant'), 'Whale', 'Lizard')
(a1, a2), a3, a4 = anaimals_by_class
# Praying Mantis, Ant, Whale, Lizard 

# Unpacking an iterator with an unknown length
# Star unpacking
a1, *rest, a2 = animals
print(a1, *rest, a2)
# Praying Mantis ['Ant', 'Whale'] Lizard

# Unpacking a dict

animals_and_classes = {
  'Mantis': 'Insect',
  'Ant': 'Insect',
  'Whale': 'Mammal',
  'Lizard': 'Reptile'
  }

# Unpacking into tuples
(k1, v1), (k2, v2), (k3, v3), (k4, v4) = animals_and_classes.items()
``` 

### Iterators and Generators
* Two things that an iterators has to have:
  * Iterators are objects that you can use in a 'for' loop
  * Iterators are the bare minimum of an collection
    * Objects that implement the iterator protocol
    * They support 'in' and 'for'
    * Iteroators do not cenessarily
      * Have a length
      * Support indexing
* Lists, Dicts, Tuples are sequences that extend the iterator protocol and you
  can loop over them

```py
t = 'a', 'b', 'c'

# These two things below describe the Iterator protocol:
# 1. Looping through the object in a for loop
for e in t:
  print(e)
# a b c

# 2. Using in to check wheter the object contains some elements
print('d' in t)
# False

# Uder the hood iterators using iter(), next(), and StopIteration
# First, iter() provides an actual iteteratob object
# Then, next() retrieves elements from this iterator object
# Unit the iterator is exhausted, in which case a StopIteration is reaised

# Takes a tuple and turns into meta iterable object
i = iter(t)

# Elements are retrieved until a StopIteration has raised and iteration stops
print(next(i)) # a
print(next(i)) # b
print(next(i)) # c
print(next(i)) # StopIteration Exception 

i = iter(t)
while True:
  try:
    e = next(i)
  except StopIteration:
    break
  print(e)
# a b c
```
* You need to understand that we have e.g. `t` which is a tuple that is going to
  be turned into an iterable object by `iter(t)` and only after that it becomes
  an iterator and we can iterate over it

### Creating Your Own Iterator
* An iterator is an object with at least the following methods:
  * __iter__() returns the actual object that will be iterated through
    * returns the object itself
  * __next__() returns the next element and raises a StopIteration when the
    iterator is exhausted
    * returns the next object

```py
import random

class RandomIterator:
  def __init__(self, *elements):
    self._elements = list(elements) # list function converts a tuple to a list
  def __iter__(self):
    random.shuffle(self._elements)
    self._cursor = 0
    return self
  def__next__(self):
    if self._cursor >= len(self._elements):
      raise StopIteration()
    e = self._elements[self._cursor]
    self._cursor += 1

i = RandomIterator(1, 2, 3)
for e in i:
  print(e)
# 3 2 1
```

### Exploring Generators
* A Generator is a function with a yield statement
* Normal function:
  * Return output with the return statement
  * Once a value is returned the function is finished
  * Receive input through function argument
* Generator function:
  * Return output with the yield statement
  * They can yield multiple times
  * Receive input with each yield
* A Generator is a Type of Iterator because under the hood Python turns an
  Generator into an Iterator object

```py
def my_generator():
  yield 'a'
  yield 'b'
  yield 'c'

for e in my_generator():
  print(e)
# a b c

print('a' in my_generator())
# True

g = my_generator()
print(g.next()) # a
print(g.next()) # b
print(g.next()) # c
print(g.next()) # StopIteration()

# Bydirectional commucation in a generator function

import random
SENTENCES = [
  'How are you?',
  'Fine, thank you!',
  'Noting much',
  'Just chillin'
]

def random_conversation():
  recv = yield 'Hi'
  while recv != 'Bye!':
    recv = yield random.choice(SENTENCES)

# First we need to instanciate it then we can an Iterator object we can loop
through
g = random_conversation()

# .send is like next, but here we say something into the Generator function
# you always need to send first None to send dummy information to allow
Generator to return information to us
print(g.send(None))
while True:
  try:
    reply = g.send('input()')
  except StopIteration:
    break
```

### Lazy Evaluation
* Evalute what you need, when you need it and nothing more
* Eager evaluation:
  * If you loop through a list, all elements are created in advance
  * This is inefficient, because - it consumes memory and not all elements may
    be used. 
* Lazy Evaluation
  * If you loop through an iterator, the iterator may create each element when
    it is called
  * This is efficient, because  only one element is kept in memory. Unused
    elements are never created. 

```py
def eager_fibonacci(n):
  l = [1, 1]
  for i in range(n-2):
    l.append(sum(l[-2:]))
  return l

def lazy_fibonacci():
  yield 1
  yield 1
  l = [1,1]
  while True:
    # makes it lazy because we remember only 2 numbers 
    l = [l[-1], sum(l[-2:])]
    yield l[-1]

for i, f in enumerate(lazy_fibonacci()):
  if i = 10:
    break
  print(f)
```

### Corouties - Implementing Concurrency through Generators
* Rapid Alternation = Parallel
* Generator functions can suspend and resume
* Therefore, multiple generators can run in rapid alternation
* Such generators are often called coroutines
* The term light-weight threading is also used
* Different ways to do things in parallel
  * Multi processing == Multiple separate processes (like you start a program
    multiple times)
    * Each process has its own memory
    * Communicatioin between processes is difficult (they cannot share variables)
    * The operation system decides which process runs when
  * Threading == Multiple threads within a single process
    * Threads share memory (are separate process but do share memory)
    * Communication between threads is (relatively) easy
    * The operating system decides which thread runs when
    * In Python, the global interpreter lock (GIL) makes threading inefficient
  * Coroutines == Functions run in rapid alternation
    * More stable and transparent (just a normal code)
    * The program determine which coroutines run when
    * Very efficient (no overhead, just a normal code, no overhead to define
      which process to run when)
    * Cooperative (if you write a function that you want to use as a coroutine
      it must not block, don't occupy the CPU)
    * Coroutines are the fundament of async/await

* This is an coroutine example because they communicate with each other see
  example `SENTENCES`
```py

def fibonacci():
  yiel 1
  yield 1
  l = [1, 1]
  while True:
    l = [l[-1], sum(l[-2:])]
    yield l[-1]

def tribonacci():
  yield 0
  yield 1
  yield 1
  l = [0, 1, 1]
  while True:
    l = [l[-2], l[-1], sum(l[-3:])]
    yield l[-1]

for i, (f, t) in enumerate(zip(fibonacci(), tribonacci()):
  if i == 10:
    break
  print(f, t)

import random

SENTENCES = [
  'How are you?',
  'Fine, thank you!',
  'Noting much',
  'Just chillin',
  'Bye!'
]

def speaker():
  while True:
    yield random.choice(SENTENCES)

def replier():
  while True:
    recv = yield
    print('Received: %s' % recv)
    if recv == 'Bye!'
      break
    print('Replied: %s' % random.choice(SENTENCES))


s = speaker()
r = replier()

# .send() is the same as asking .next()
r.send(None)

while True:
  recv = s.send(None)
  try:
    r.send(recv)
  except StopIteration:
    break

```

### Convenience Iterators - The Collections Module
* namedtuple - a tuple with named fields
  * Fields in a regular tuple have an index but not name
  * Fields in a namedtuple have an index and a name
  * Can make code more readable
* OrderDict - A dict with an order
  * A regular dict has no (predictable) order
  * An orderDict does
* defaultdict - A Dict with Default Values
  * Retrieving a non-existing key from a regular dict gives a KeyError
  * A defaultdict gives a default value

```py
# Unlike tuple or list the namedtuple is not built-in into Python but rather
it's in the collections module and the collections module is part of the Python
standard library

from collections import namedtuple

# namedtuple is a factory function that creates a class
Person = namedtuple('Person', ['name', 'age'])
jay_z = Person(name='Sean Carer', age=47)

# Very explicit we explicitly refer to jay_z.name, jay_z.age
print('%s in %s years old' % (jay_z.name, jay_z.age))


from collections import OrderedDict

# Has a guarantee to be ordered
d = OrderDict([
  ('Lizard', 'Reptile'),
  ('Whale', 'Mammal')
])

for species, class_ in d.item():
    print('%s is a %s' % (species, class_))


from collections import defaultdict

favorite_programming_languages = {
  'Claire': 'Assembler',
  'John': 'Ruby',
  'Sarah': 'JavaScript'
}

# if the key 'Sebastian' doesn't exists return the default value
print(favorite_programming_language.get('Sebastian', 'Python'))


d = defaultdict(lambda: 'Python')
d.update(favorite_programming_languages)
print(d['Harry']) # Python
```

### List and Dict Comperehensions and Generator Expressions
* Statement in Python is an instruction and a way to tell Python to do something
  * A 'for' loop is a stamement
  * A statement doesn't evaluate to anything
* Expression is anything that evaluates to something
  * For example 10 + 10
  * Used heavily in fp
* A list comprehensions are an expressive alternative to 'for' statements


```py
from math import sqrt
for i in range(5):
  print(sqrt(1))

[sqrt(i) for i in rage(5)]

# Filtering list comprehensions

for i in range(5):
  if i%2:
    continue
  print(i)

[print(i) for i range(5) if not i%2]
```

### Dict Comprehensions
* Processing a dict in a single expression

```py

SPECIES = 'whale', 'grasshooper', 'lizard'
CLASS = 'mammal', 'insect', 'reptile'

d = dict(zip(SPECIEL, CLASS))

d = { species.capitalize(): class_.capitalize() for species, class_ in zip(SPECIES, CLASS) }
# Filtering

# If something is between curly braces you are allowed to split it into multiple
lines
d = { 
  species.capitalize(): class_.capitalize() 
  for species, class_ in zip(SPECIES, CLASS) 
  if class_ != 'insect'
  }
```

### Generator Expressions

```py
from math import sqrt

g = (sqrt(i) for i in range(5))
for i in g:
  print(i)

print(next(g)) # 0
print(next(g)) # 1

# Filtering generator expressions
g = (i for i in range(10) if not i%2)

# Breaking generator expressions
def fibonacci():
  yield 1
  yield 1
  l = [1,1]
  while True:
    l = [l[-1], sum(l[-2:])]
    yield l[-1]

def stop():
  raise StopIteration()

g = (i for i in fibonacci() if i < 10 or stop())
for i in g:
  print(i) # 1 2 3 4 5 6 7 8  
```

### Nested Comprehensions
* Defining loops within loops with a single expression
* Typical scenraio for nested loops when you need all combinations of the
  lements of two iterables, very different from `zip()`

```py
grid = []
for x in range(2):
  for y in range(2):
    grid.append((x,y))
print(grid)
# [(0,0), (0,1), (1,0), (1,1)]

grid_ = [ (x, y) for x in range(2) for y in range(2) ]
print(grid_)
# [(0,0), (0,1), (1,0), (1,1)]
```

* Explained that statements are instructions to the Python interpreter and
  expressions are things that evaluate to something

### Functions that work with Iterators

#### Convinient Functions
* Several built-in (means you can use it right away w/o importing) functions for working with iterators
* zip(), map(), enumerate(), and filter()
* zip(): linking elements from multiple iterators
* enumerate(): getting indices along with elements

```py
speciel_list = ['Whale', 'Lizard', 'Ant']
class_list = ['Mammal', 'Reptile', 'Insect']
cuteness_list = [3, 2, 1, 0]

for i in range(len(species_list)):
  species = species = species_list[i]
  class_ = class_list[i]
  print('%s is a %s' % (species, class_))

for species, class_ in zip(species_list, class_list):
  print('%s is a %s' % (species, class_))

for species, class_, cuteness in zip(species_list, class_list, cuteness_list):
  print('%s is a %s and has a cuteness of %s' % (species, class_, cuteness))

# We are using map() in a for loop that automatically iterates through all
elements
from math import sqrt
fibonacci = [1,1,,2,3,5,8]

for i in map(sqrt, fibonacci):
  print(i)

# Generator expression
for i in (sqr(j) for j in fibonacci):
  print(i)

# enumerate() - example
i = 0
for species in species_list:
  print(i, species)
  i +=1

for i, species in enumerate(species_list):
  print(i, species)
# 0 Whale
# 1 Lizard
# 2 Ant

# filter()
for i in fibonacci:
  if i%2:
    continue

for i in filter(lambda i : not i%2, fibonacci)
  print(i)
# 2
# 8

### Numerical and logical function for working with Iterators
none_true = [0,0,0]
some_true = [0,1,0]
all_ture = [1,1,1]

def check_any(i):
for e in i:
  if e:
      return True
  return False

check_any(none_true)


# with any() check if any of the lements evaluate to True
any(some_true) # True
any(non_true) # False

True in (bool(e) for e in none_true)

# with all() all elements evalute to True
all(all_true) # True
all(some_true) # False

# generator expression
False not in (bool(e) for e in all_true)

# sorted() takes an iterator with numeric element, sorts it, and returns a list
numbers = [2, -1, 2, 4]
sorted(number)

# min() & max() to sort numbers in iterator
# sum() to get the sum of an iterator

### The Itertools Module
* The itertools module which provides:
  * A wide variety of functions to create (or operate on) iterators
  * To select and group elements from iterators
  * To implement combinatorial logic
  * Functions from itertools are not built-in but they are part of the standard
    library. Means you don't need to install it separetely

```py
import itertools as it

# count() retuns an infinite counter
for i in it.count(start=10, steps=-1):
  if not i:
    break
  print(i)

# cycle() loops an iterator infinetely
# repeat() creates an infinite iterator from a single element
# chain() links multiple tal to head (to flatten a list)
for e in it.chain('abc', [3,2,1], 'cba')
  print(e)
# a b c 3 2 1 c b a
``` 

### The FuncTools Module

```py
import functools as ft
import math
import itertools as it
import time

# first we specify the function we want to partial
# then we specify the argument we want to bind
sqrt_9 = ft.partial(math.sqrt, 9)

# @lur_cache() decorator remembers the results of a function call, and when the
function called again with the same set of arguments, returns this result right
away. This is a form of caching, and is related to the functional-programming
concept memoization


@ft.lru_cache()
def prime_below(x):
  return next(
    it.dropwhile(
      lambda x: any(x//i == float(x)/i for i in range(x-1, 2, -1)),
      range(x-1, 0, -1)
      )
    )

t0 = time.time()
print(prime_below(10000))
t1 = time.time()
print(prime_blow(10000))
t2 = time.time()
print('First took %.2f ms' % (1000.*(t1-t0)))
print('Then took %.2f ms' % (1000.*(t2-t1)))
# 9973
# 9973
# First took 78.71 ms
# Then took 0.25 ms

# The @singledispatch decorator allows you to create different implementations
of a function, given different argument types. The type of the first argument is
used to decide which implementation of the function should be used

@ft.singledispatch
def add(a, b):
  return a+b

@add.register(str)
def _(a, b):
  return int(a) + int(b)

print(add('1', '2'))

```


```py
adam_sandler_movies = [
  ('Paul Bart', 0.06),
  ('Blended', 0.14),
  ('Grown Ups', 0.07),
  ("That's my boy", 0.2),
  ('Hotel Transylvania', 0.44)
]
selected_titles = map(
  lambda movie: movie[0],
  filter(lambda movie: movie[1] >= 0.2,
    adam_sandler_movies
    )
  )
print(list(selected_titles))
# ["That's my Boy", 'Hotel Transylvania']
```
