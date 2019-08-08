# Consider Generators Instead of Returning Lists


def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result

address = 'Four score and seven years ago...'
result = index_words(address)
print(result[:3]) # [0,5,11]

# There is a problem with index_words is that it requires all results to be stored in the list before being returned
# For huge inpurts, this can cause your program to run out of memory and crash
# In contrast, a generator version of this function can easily be adapted to take inputs of arbitrary length

# A better way to write this function is using generator.
# Generators are functions that use yield expressions.
# When called, generator functions do not actually run but instead immediately return an iterator.
# With each call to the next built-in function, the iterator will advance the generator to its next yield expression
# Each value passed to yield by the generator will be returned by the iterator to the caller


def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1

result_ = list(index_words_iter(address))
print(result_)


def index_file(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset
        for letter in line:
            offset += 1
            if letter == ' ':
                yield offset

with open('./utils/sample.txt', 'r') as f:
    it = index_file(f)
    print(list(it)[:3])

# The only gotach of defining generators like this is that the callers must be aware that the iterators returned are stateful and can't be reused


# Source: https://www.dataquest.io/blog/python-generators-tutorial/
# We refer to any object that can support iteration as an iterable
# Iterables support something called the Iterator Protocol (just a couple of methods on an object)
# Iterables describe how a for loop should traverse its content based on beginning and the end (indexes)
# Generators are iterables themselves and can be used in for loops
# Iteration is the idea of repeating some process over a sequence of items. In Python, iteration is useally related to the for loop.
# Python generators generate values one at a time for a given sequence, instead of giing the entirety of the sequence at once.
# Two ways to create a generator: generator function / generator expression

def function_a():
    return 'a'

def generator_a():
    yield 'a'

# Calling a regular function tells Python to go back to where the function is located in our code, perform the code within the block, and return the result
# In order to get the generator function to yield its value, you need to pass it into the next() function
# next() is a special function that asks, "What's the next item in the iteration?". 
# next() is the precise function that is called when you run a for loop. Lists, dicts, string implement next(), so this is why you can incorporate them into loops

print(
next(generator_a())
)

# Generators produce a stream of values. 

def multi_generate():
    yield 'a'
    yield 'b'
    yield 'c'

# Assigning multi_generate to mg is a crutial step in using a generator function. Bidning generator to mg allows us to create a single instance of a generator we can refer back to
mg = multi_generate()
next(mg) # a
next(mg) # b
next(mg) # c
#next(mg) # StopIterationException

# We've noted that as we keep passing in mg into next, we get the other yield results.
# This is possible only if the generator somehow remembers what it last did. 
# This memory distinguishes generator functions from regular functions. 
# Once you use a function, it's a one-and-done deal. A generator will keep yielding values until its out.

def beer_data_generator():
    file = './utils/recipe_data-2.csv'
    for row in open(file, 'r', encoding='ISO-8859-1'):
        yield row

# Python objects like lists and dicts can be iterated over, we can also iterate over files that we open() as well.
# The for loop will start with the first row in the CSV file, yield that row, and then save its current place in reading the file
# until the generator function is called again

# Initialize the generator / create the generator
beer = beer_data_generator()



# Why not to use list comprehensions?
# As a programmer, you may encounter Big Data. Big Data file is too big to assign to a variable
# We assume that our beer file is too large in size that we are incapable of storing all of the data in a list of lists


# The generator expression
lc_example = [n**2 for n in [1,2,3,4,5]] # list comprehension
genex_example = (n**2 for n in [1,2,3,4,5]) # generator expression

# next() it's often better to use generators in for loops.
# Using next() forces us to have to deal with the StopIteratior overselves.
# lines does the same as the function beer_data_generator()
beer_data = './utils/recipe_data-2.csv'
lines = (line for line in open(beer_data, encoding='ISO-8859-1'))

# generators produce values one-at-a-time as opposed to giving them all at once

# Motivation for Generators
# Imagine we have 4GB of RAM and we have a file of 3GB.
# If we were to read the entirety of our data set into a variable, it would take up a bit more than 3GB of RAM
# Storing our data in a list of lists would take up so much memory that any analysis we do would take long to do

# Laziness
# Generators produce a single value from a defined sequence, but only when we ask next() or within a for loop.
# We call this lazy evaluation
# Generators are lazy because they only give us a value when we ask for it
# The flipside here is that only that single value takes up memory
# The result is that generators are incredibly memory efficient, which makes them perfect candidate for using Big Data files.
# Once we ask for the next value of a generator, the old value is discarded
# Once we go through the entire generator, it is also discarded from memory as well

# What we have done so far we took the csv file, created a generator that will yield each line in the CSV one at a time
# Generators are iterators themselves too
# We can create another generator that takes the output of another generator
# The end result of our generators is a stream of lists, each containing the data within a row of the CSV
# If we iterate through lists, we'll be able to easily access the data elements within
# We made a pipeline for our data set, starting from raw data set and sending it through 2 generators
lists = (l.split(',') for l in lines)

# Remember: generators aren't lists themselves, they generate a single element of a sequence and only take up the amount that element needs.
# By piping generators together, we've created quick way for us to read data that would be inaccessible through normal means. 
# We didn't need to create any temporary lists to hold intermediate values as we processed them
# In this pipeline, each generator is put in charge of a single operation that will eventually be applied to all rows of the data set

# Take the column names out of the generator and store them, leaving only data
columns = next(lists)

# Take these columns and use them to create a dictionary
beerdicts = (dict(zip(columns, data)) for data in lists)

# Now that we have our generator pipeline, we can start consuming the data produced by the generators and create some insights
# We usually consume generators using for loops

def consume_generator():
    beer_counts = {}
    for bd in beerdicts:
        if bd['Style'] not in beer_counts:
            beer_counts[bd['Style']] = 1
        else:
            beer_counts[bd['Style']] +=1
    most_popular = 0
    most_popular_type = None
    for beer, count in beer_counts.items():
        if count > most_popular:
            most_popular = count
            most_popular_type = beer

    print(most_popular_type)

abv = (float(bd['ABV']) for bd in beerdicts if bd['Style'] == 'American IPA')

# The consumption/reduction and reduction of a generator pipeline can be done with a for loop, sum(), min(), max(), reduce()
