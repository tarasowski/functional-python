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
next(mg) # StopIterationException

