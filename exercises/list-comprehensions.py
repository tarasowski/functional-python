# https://www.youtube.com/watch?v=_6U1XoxyyBY
# For loops examples
colors = ['red', 'green', 'blue']
rations = [0.2, 0.3, 0.1]

for i, color in enumerate(colors): 
    print(i, color, rations[i])

for color, ratio in zip(colors, rations):
    print(color, ratio)

animals = {'birds': 3, 'cats': 2, 'dogs': 1}

# f'' stands for f-strings / fantastic strings 
for item in animals:
    print(f'I have {animals[item]} {item}')

for animal, count in animals.items():
    print(f'I have {animal} {count}')

my_favorite_numbers = [1,1,2,3,5,8,13]


# List comprehension
# It's an expression
doubled_comprehend = [n * 2 for n in my_favorite_numbers]
print(doubled_comprehend)

# You can copy the for loop into a comprehension
# Python doesn't care about whitespace inside a square brackets, or parens
# See this looks like the foor loop, first we start with [], then the formula n * 2 that we are appending to a list, next the for loop
# This is why it's called a list comprehension, because we rebuild a list again with new values
# The point of list comprehension is to build a list

from math import sqrt

doubled_numbers = [
        # lambda n: n * 2 - you cannot use lambda here, it's not a function that gets called
        sqrt(n) 
        for n in my_favorite_numbers
]
print(doubled_numbers)

# The thing that we get back is a map object
# map() returns an iterator
doubled_map = map(lambda n: n*2, my_favorite_numbers)
# If you want to convert the map object to a list you can do
print(list(doubled_map))

#tuple() returns nothing the iterator is exhausted
print(tuple(doubled_map))

def mult2(n):
    return n * 2

doubled = []

for n in my_favorite_numbers:
    if n % 2 == 1:
        doubled.append(n * 2)
    
print(doubled)

dn = [
    #mult2(n) 
    (lambda n: n * 2)(n) # mapping
    for n in my_favorite_numbers
    if n % 2 == 1 # filtering
]

print(dn)

# Exercises

# matrix is a list of lists
def flatten(matrix):
    return [
            item
            for row in matrix
            for item in row
    ]

#    flattened = []
#    for row in matrix:
#        for x in row:
#            flattened.append(x)
#    return flattened

print(
    flatten([[1,2],[3,4]]),
    flatten([]),
)

matrix = [[1,2,3], [-4,5,-7]]

# list comprehension inside a list comprehension
negative_matrix = [
        [-n for n in row] # inner comprehension
        for row in matrix # outer comprehension
]


print(negative_matrix)


# Generator expressions
# One thing we can do with generators is iterate over it with a loop with a list comprehension
# Generators are like list comprehensions but they don't take up the memory like a list
# They are lazy iterables, they promise that in some point if future if you start looping over me, i'm going to give you items back
numbers = [1,2,3,4]
g = (
        n**2 
        for n in numbers
    )

for x in g:
    print(x)

# Here you'll get nothing, because Generators gets exhausted
# Generators create Iterators
# Iterators can be consumed one by one
# Unlike with lists, you can loop over lists twice. You can loop over lists as many times as you want
for x in g:
    print(x+1) 

# Why to use generator here? In order to save memory
# We have a list of all of this words, this is not a list of words, this is a promise when you loop over `words`
with open('dictionary.txt') as dictionary_file:
    words = (
            line.rstrip()
            for line in dictionary_file
            )
    words_over_five_letters = [
            word
            for word in words
            if len(word) > 5
            ]

# set functions expects an iterable and gives us back a set ()
# the same goes to tuple(), it accepts an iterable and creates a tuple ()
# the sames goes to list(), it accepts an iterable and creates a list [] out of a generator expression
# this is a set comprehension
reversed_words = {
        word[::-1]
        for word in words_over_five_letters
        }

#reversed_words = set(
#        word[::-1]
#        for word in words_over_five_letters
#        )

#for word in words_over_five_letters:
#    # set() don't have append because there is no end, they are unordered
#    reversed_words.add(word[::-1])

reversible_words = [
        word
        for word in words_over_five_letters
        if word in reversed_words
        ]

for word in reversible_words:
    print(word)

# Made a Generator by Generator Expression
squares = (n**2 for n in numbers)

# Under the hood it does
# squares.__next__() this is what happens under the hood and they are called a dunder or magic method
# they add some functionality that python understands 
# __len__() equivalent to len()
# __add__() equivalent to + operator
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))

# any() and all() are purpose made to use with generator expression
print(any(n > 1 for n in numbers))

codition = False
for n in numbers:
    if n > 1:
        codition = True
        break

# you can pass generator expression into a function core
# you can remove the parens around the generator expression
# the generator doesn't store the items when it's gone
cond = any(
        n > 1 
        for n in numbers
       ) 

t = [1,2,3,4,5]
h = map(lambda x: x * 2, t)
z = filter(lambda x: x < 5, h)
li = list(z)

# you can loop over generators because they are single-use iterables
for n in z:
    # it doesn't get printed because the Iterator is already exhausted
    print('from iterator first time')
    print(n)

for n in z:
    # it doesn't get printed because the Iterator is already exhausted
    print('from iterator first time')
    print('from iterator second time')
    print(n) 


print(li)
print(li)
print(li)

number = 50
rg = list(range(1, number+1))
rg2 = range(number)

def is_prime(number):
    return all(
            number % n != 0
            for n in range(2, number)
            )

print(is_prime(number))

words = {
        'esta': 'is',
        'la': 'the',
        'en': 'in',
        'gato': 'cat',
        'casa': 'home',
        'el': 'the'
        }
import time
def translate(spanish_sentence):
    # because we are using a generator expression we're able to use a join method
    # if a function call has a single positional argument, it can be a generator expression without extra parentheses, but in all other cases you have to parenthesize it. 
    return " ".join(
                words[spanish_word]
                for spanish_word in spanish_sentence.split()
            )
   # english_sentence = [] 
   # for spanish_word in spanish_sentence.split():
   #    english_sentence.append(words[spanish_word]) 
   # return ' '.join(english_sentence)

t0 = time.time()
translate('el gato')
t1 = time.time()
print(f' time {t1 - t0}')
print(
translate('el gato')
)

from string import ascii_lowercase

# dict comprehension
letters = {
        n + 1: letter
        for n, letter in enumerate(ascii_lowercase)
        }

print(letters)

# comprehensions build up a new list
# if you use print(n) you can use a for loop because you are not trying to build up a list

x = [print(n) for n in range(5)]
print(x)

# List object is not an iterator
# Iterable is an object, which one can iterate over
# Iterators have __next__() method, which returns the next item of the object. 
# Note that every iterator is also an iterable, but not every iterable is an iterator
# For example, a list is iterable but a list is not an iterator
hh = [1,2,3,4]

import csv
data = [('blue', 0.2), ('red', 0.3), ('green', 0.5)]

# open a scv file in a write mode
# how we know that we can turn a list comprehension into generator expression?
# if we only looping it over once
with open('data.csv', mode='w', encoding='utf-8-sig') as csv_file:
    writer = csv.writer(csv_file)

# we have here the first list wich is called data and the second list which is called rows
# but we can use generator expression in order not to store two lists into the memory
#    rows = [
#            (frequency, color)
#            for color, frequency in data
#    ]

# there is no need to have a name for generator expression
    writer.writerows(
            (frequency, color)
            for color, frequency in data
    )


# Generator functions
# They don't have a return, they have yield
# returns a generator object
def all_together(*iterables):
# generator function
#    for iterable in iterables:
#        for x in iterable:
#            yield x

# generator expression
            return (
                    x
                    for iterable in iterables
                    for x in iterable
                    )

all_together([1,2], (3, 4))

from functools import reduce
import time
def map1(x: int):
   return x * 2
def map2(x: int):
   return x - 1
def filter1(x: int):
   return x < 20
def reduce1(a: int, x: int):
   return a + x

if __name__ == '__main__':
    start = time.time()
    data = range(0, 1000000)
    result = reduce(reduce1, filter(filter1, map(map2, map(map1, data))))
    print(f'generator: {result}')
    end = time.time()
    print(f'generator time: {end - start}')    
    data = list(range(0, 1000000))
    result = reduce(reduce1, filter(filter1, map(map2, map(map1, data))))
    print(f'list: {result}')
    end = time.time()
    print(f'list time: {end - start}')

