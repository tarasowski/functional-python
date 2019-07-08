# Functional Programming in Python


### Interactive Calculator in Python

* Procedural Programming:
  * Line by line (very script like implementation)
  * Heavy use of statements (for loop, return, if else)
  * Heavy use of expressions (anything that evaluates a value)
  * Long functions

* Functional Programming:
  * Little use of statements (no for loops, no if else)
  * Heavy use of expressions
  * Single-line function (every function is a single line expression)

* Programming styles are like painting styles

```py
OPERATORS = '+', '-', '*', '/'

# p_ means procedural implemantation
def p_main() -> int:
    print('Welcome to the barely functional calculator!')
    number1 = p_get_number()
    operator = p_get_operator()
    number2 = p_get_number()
    result = p_calculate(number1, operator,  number2)
    print('The result is: %r' % result)

def p_get_number() -> int:
    while True:
        s = input('Enter an integer: ')
        try:
            return int(s)
        except ValueError:
            print('That is not an integer!')

def p_get_operator():
    while True:
        s = input('Enter an operator (+, -, *, or /): ')
        if s in OPERATORS:
            return s
        print('That is not an operator!')

def p_calculate(number1, operator, number2) -> int:
    if operator == '+':
        return number1 + number2
    if operator == '-':
        return number1 - number2
    if operator == '*':
        return number1 * number2
    if operator == '/':
        return number1 / number2
    raise Exception('Invalid operator!')

#p_main()


# f_ means functional implementation
# every function is a single expression here

# not safe will be refactored later
def f_get_number() -> int:
    return int(input('Enter an integer: '))

# not safe will be refactored later
def f_get_oprator() -> int:
    return input('Enter an operator: ')

# single expression
def f_calculate(number1: int, operator: OPERATORS, number2: int) -> int:
    return number1 + number2 if operator == '+' \
            else number1 - number2 if operator == '-' \
            else number1 * number2 if operator == '*' \
            else number1 / number2 if operator == '/' \
            else None # we return None if operator was not valid 

def f_main() -> int:
    return f_calculate(
            f_get_number(),
            f_get_oprator(),
            f_get_number(),
            )
print('The result is: %s' % f_main())
```

### State and Staless / Side-Effects / Referential transparency
* What is state?
  * Functions are not executed in a void (void functions are those that do not
    return anything)
  * There are global variables
  * Objects with properties
  * These are states (global variables + objects with properties)
  * Can influence how functions work

* When is a function stateless?
  * Always return the same result
  * Giveht the same arguments
  * Regardless of the program's state
  * Also called referential transparency (if a functions is staless and have no
    side effects) - **allows parallel execution**
  * Function without side-effects (functions w/o side-effects that does not
    change the program state)

```py
current_speaker = None

# A stateful example
def register(name):
    global current_speaker
    current_speaker = name

def speak(text):
    print('[%s] %s' % (current_speaker, text))

register('John')
speak('Hello world!')
register('Carlos')
speak('Foobar!')

# Object are also states
# Stateful implementation the object has a self._name and this property is a state that is inside the object (encapsulation)
# Objects are stateful
class Speaker():
    def __init__(self, name):
        self._name = name
    def speak(self, text):
        print('[%s] %s' % (self._name, text))

john = Speaker('John')
john.speak('Hello World')
carlos = Speaker('Carlos')
carlos.speak('Foobar!')


# Stateless implementation of the above examples
def speak(speaker, text):
    print('[%s], %s' % (speaker, text))

speak('John', 'Hello world')
speak('Carlos', 'Foobar!')

```

### Prove that code is correct
* Unit testing
  * Function are tested with different kinds of input
  * To see if they behave well
  * Check if input matches the expected output
  * Case-based testing
  * There is no guarantee
* Formal provability
  * Referential transparency allows formal provability
  * Beautiful in theory
  * Difficult in practice
  * In order to prove a function we can return it to a simplest form (see below
    def simple_reduced)
  * The function becomes deterministic, means that you can replace a function
    with a value

```py

def smile(l):
    return list(itertools.chain(*[['😄']*i for i in l]))

print(
    smile([1,2])
)

print('Starting test')
assert(smile([]) == [])
assert(smile([1]) == ['😄'])
assert(smile([0]) == [])
print('Done')

def smile_reduced(l):
    return ['😄'] * sum(l)

print(smile([1,2,3]))
``` 

### Complexicty and Overly Deep Recursion

* What is recursion
  * Function that call themselves
  * Recursion is elegant
  * But difficult to follow for most human-beings
  * Max. recursion depth
    * Python has a built-in limitation of 1000 functions on the stack

### Functional Programmin gcan be Unintiutive
* Function programming is not how humans think
* Psychology:
  * We are human after all
  * Humans automatically parse the world into objects
  * Objects can be people, things, ideas and so on
  * Any well-defined something that has a set of properties
* OOP can be intuitive because:
  * Allows you to divide your code into object
  * Just like you mentally divide the world into objects
  * This can lead to intuitive code
* Functional programming can be unintuitive:
  * Does not divide code into objects (you have functions and values that are
    passed into a function)
  * If humans reason about math, fp is a good intuitive
  * And cal lead to unintuitive code
  * In cases where this doesn't match our intuition
* Summary:
  * Pro of fp: statelessness, lack of side effects, and referential transparency
    (no state + w/o side effects), provability
  * Cons of fp: complexity and deep recursion, poor match with human psychology

```py
# By using OOP we can mirror the code into how we think about the world
# If we think about voting we thing about Voter and Politician

# An OOP approach
# We structured our code in a way we think about election
# Procedural & stateful implementation
class Voter:
    def __init__(self, name):
        self.name = name
        self.voted_for = None
    def vote(self, politician):
        self.voted_for = politician
        politician.votes += 1
    def __str__(self):
        return self.name

class Politician:
    def __init__(self, name):
        self.name = name
        self.votes = 0

    def __str__(self):
        return self.name

macron = Politician('Macron')
jean = Voter('Jean')
jean.vote(macron)
print('%s voted for %s' % (jean, jean.voted_for))
print('%s received %d vote(s)' % (macron, macron.votes))

# A functional approach
# A functional approach doesn't mirror the world how we think about the world and makes it unintuitive
def vote(voters, politicians, voter, politician):
    # not purely functional since we are resetting the values for dicts
    voters[voter] = politician
    if politician in politicians:
        politicians[politician] += 1
    else:
        politicians[politician] = 1
    return (voters, politicians)

def voted_for(voters, voter):
    # None is the default value
    return '%s voted for %s' % (voter, voters.get(voter, None))

def votes(politicians, politician):
    # 0 is the default value
    return '%s received %d vote(s)' % (politician, politicians.get(politician, 0))

voters, politicians = vote({}, {}, 'Jean', 'Macron')
print(voted_for(voters, 'Jean'))
print(votes(politicians, 'Macron'))
```

### Lambda Expressions or Nameless Function
* What is a statement?
  * It's an instruction for Python interpreter
  * if, for, def, class, and so on
  * Function definitions are statements (def main(): ...)
  * Don't evaluate to something (has no return value)
  * Statement examples see below:
```py
# Assignement
x = 0
x += 1

# Conditional branching
if x == 1:
  print('x == 1')
elif x == 2:
  print('x == 2')
else:
  print('x not in [1,2]')

# Loops
for x in range(2):
  print(x*2)

while True:
  break

# Function, generator, and class definitions
class MyClass()
  pass
def my_function(x):
  return x*2
def my_generator(x):
  yield x*2

# Other statements
import os
assert True
pass
del x
try:
  raise Exception()
except:
  pass
with open('dev/null') as fd:
  pass
```
* What are expressions?
  * Evaluate to something
  * Can print the result
  * Function calls are expression (main())
    * Every function has a return value even if there is no return value
      specified a function returns `None`
  * Expressions examples see below

```py
# Values are expressions
print(10*2)
print('a')
# Function calls are expressions
print(print(10))
# List comprehensions are expression
# Allows you to loop through, it's an expression alternative to the for
statement
# This is an expression because we can print out the results
print([x*2 for x in range(2)])
```

### Lambda Expressions
* \ Calculus
  * A formal mathematical system
  * To express functions
  * \ functions are expressions and not statement (unlike def)
  * Without a name (nameless functions, you can a give a name but don't have
    too)

```py
from math import sqrt

def p_pythagoras(x, y):
   return sqrt(x**2 + y**2)

p_pythagoras(1,1)
# 1.4142...

# A simple lambda function

(lambda x,y: sqrt(x**2, + y**2))(1, 2)
# we can give a name to the lambda function
# p_pythogoras = lambda x,y: sqrt(x**2, + y**2)
# 1.4142...

# Recursion requires a name. Functions created with lambda expressions can be
nameless. But for a function to call itself, it needs a name. In such cases a
def statement may be more intuitive

def f_factorial(n):
  return 1 if n == 0 else n*f_factorial(n-1)

l_factorial = lambda n: 1 if n == 0 else n*l_factorial(n-1)

l = [0, 1, 2, 3, 4]
list(map(lambda x: x * 2, l))
```

### Understanding 'and' and 'or' operators
* Short-circuit
* 'and'
  * Gives the first value isn't True
  * The rest is not evaluated
    * 1 and 0  and 1 (the last 'and 1' is not evaluted)
  * Or the last value if all values are True
    * 'a' and 'b' and 'c' (the last value is going to be evaluted)
* 'or'
  * Gives the first value that is True
  * The rest is not evaluted
    * '' or 'a' (or'' is not evaluted)
  * Or the last value if all values are False
    * [] or [] or []
* We can use 'and' and 'or' thereofre as flow control tools
* Just like 'if' statements
* But be careful, this can result in hard-to-read code

```py
def my_and(*values):
  for value in values:
    if not value:
      return value
  return value

def my_or(*values):
  for value in values:
    if value:
      return value
  return value

my_or('', 'a', '') == ('' or 'a' or '')
```

```py
ANIMALS = 'mammals', 'reptile', 'amphibian', 'bird'
EGG_LAYING_ANIMALS = 'reptile', 'amphibian', 'bird'

# returns True if the animal is in the ANIMALS
is_animal = lambda animal: animal in ANIMALS

animal_lays_eggs = lambda animal: animal in EGG_LAYING_ANIMALS

# We are using and here as a flow control tool which determines if the second
function is going to be executied or not
# You can use it for printing values such as in js console.log(x) || x
# lambda x: print(x) or x
lays_eggs = lambda thing: is_animal(thing) and animal_lays_eggs(thing)

lays_eggs('rock')
# False
```

### Diving into 'if' inline expressions
* Conditional branching without statemens, the 'if' expression
* It's all about conditional branching:
  * All non-trivial programs rely on conditional branching
    * Do a if x else do b
 * 'if' statemetns are the most important way to do this
* 'if' statemens are statements
* Which cannot be used in lambda expressions
* But 'if' expressions can

```py
# Conditional branching

# The procedural way
def p_grade_description(gp):
  if gp > 7:
    return 'good'
  if gp > 5:
    return 'sufficient'
  return 'insufficient'

# The functional way
# useful for short conditional branching
(lambda gp: 'good' if gp > 7 else 'sufficient' if gp > 5 else 'insufficient')(8)

gender_code = 0
# true else true else anything else
gender = 'female' if gender_code else 'male'
```

### Higher order functions
* What a higher order function is?
  * a function that operates on other functions
* In python almost everything is an object (value):
  * That means it can be passed as an argument to a function

```py
l_factorial = lambda n: 1 if n == 0 else n * l_factorial(n - 1)

# Timing in procedural way
import time
t0 = time.time()
l_factorial(900)
t1 = time.time()
print('Took: %.5f s' % (t1-t0))

# Timing in functional way
def timer(fnc, arg):
  t0 = time.time()
  fnc(arg)
  t1 = time.time()
  return t1-t0

print('Took: %.5f s' % timer(l_factorial, 900))

# Timing with only lambda function
# A tuple is evaluated from left to right
l_timestamp = lambda fnc, arg: (time.time(), fnc(arg), time.time())
l_diff = lambda t0, retval, t1: t1 - t0
# * unpacks a tuple because l_diff expects 3 arguments
l_timer = lambda fnc, arg: l_diff(*l_timestamp(fnc, arg))

print('Took: %.5f s' % l_timer(l_factorial, 900))
```

### Nesting Function in Another Function
* Scope (who can see what?):
  * If you define a variable inside a function
  * You cannot use it outside of this function
  * Phrased differently, the scope of the variable is the function
* Nesting (functions inside functions) - closure:
  * A nested function is a function that is defined inside another function
  * This is no different form defining a variable inside a function


```py
def outer():
  def inner():
    print('I\'m inner')
  inner()

def outer():
  def inner():
    print('Inner:\t\t', x)
  print('Outer before: \t', x)
  inner()
  print('Outer after:\t', x)

x = 'global'


def outer():
  def inner():
    # global x # we are changing x global variable to 'inner'
    # nonlocal x # it changes the x one level up from 'outer' to 'inner'
    x = 'inner'
    print('Inner', x)
  x = 'outer'
  inner()

x = 'global'
outer()
```

### Returning a function from another function
* Because functions are objects
* They cannot only passed to function as arguments
* But also returned by functions a return values
* Functions can generate and return another functions 


```py
# Four steps to baking a (pre-baked) croissant
# This is an algorithm 
preheat_oven = lambda: print('Preheat oven')
put_croissants_in = lambda: print('Putting croissants in')
wait_five_minutes = lambda: print('Waiting five minutes')
take_croissants_out = lambda: print('Take croissants out (and eat them!)')


def perform_steps(*functions):
  for function in functions:
    function()

perform_steps(preheat_oven,
              put_croissants_in,
              wait_five_minutes,
              take_croissants_out
              )

def create_recipe(*functions):
  def run_all():
    for function in functions:
      function()
  return run_all

recipe = create_recipe(preheat_oven,
              put_croissants_in,
              wait_five_minutes,
              take_croissants_out
              )

# A new function that have been generated for us a new function
recipe()
```

### Operator Module - Operators as Regular Functions
* The problem tha toperators are not object (a '+' is not an object, so you
  cannot pass '+' to a function and you cannot return '+' from a function)
* Operator are things like +, -, /, * and so on
* These symbols are part of Python syntax
* They are not objects
* You cannot pass them as arguments to functions

```py
l_factorial = lambda n: 1 if n == 0 else n*l_factorial(n-1)

def chain_mul(*what):
  total = 1
  for (fnc, arg) in what:
    total *= fnc(arg)
  return total

chain_mul((l_factorial, 2), (l_factorial, 3)) # 12

def chain_mul(how, *what):
  total = 1
  for (fnc, arg) in what:
    total = how(total, fnc(arg))
  return total

# Not valid python
chain_mul(*, (l_factorial, 2), (l_factorial, 3))


import operator
def chain_mul(how, *what):
  total = 1
  for (fnc, arg) in what:
    total = how(total, fnc(arg))
  return total

# Valid python
chain_mul(operator.mult (l_factorial, 2), (l_factorial, 3))
```

### Decorators - The @ Prefix
* Decorators are 'wrapping' a function around a function
* Allows you to add functionality to a function
* It is elagantly supported in Python
* If we want to use @ syntax we need to define a function as a def statement and
  not as lambda expression

```py
def factorial(n):
  return 1 if n == 0 else n*factorial(n-1)


import time

# This is a decorator
def timer(fnc):
  def inner(arg):
    t0 = time.time()
    fnc(arg)
    t1 = time.time()
    return t1-10
  return inner

timed_factorial(timer(factorial))
timed_factorial(500)

# The real decorator version

# Timer is essentially the same as passing the function inside the
timed_factorial into def timer
# The timer function that we've defined above is a decorator. You can apply a
decorator to a function directly, using the @ syntax
@timer
def timed_factorial(n):
  return 1 if n == 0 else n*factorial(n-1)

timed_factorial(500)

```

### Decorators with Arguments
* A decorator is a function that returns a function
* This requires a nested function
* Or two levels
* A decorator with arguments
  * Is a function that returns a decorator
  * Which is turns returns a function
  * This requires nesting with nesting
  * Or three levels

```py

import time

# timer_with_arguments is a function that generates a decorator
def timer_with_arguments(units='s'):

  # timer is the decorator
  def timer(fnc):
    def inner(arg):
      t0 = time.time()
      fnc(arg)
      t1 = time.time()
      diff = t1 - t0
      if units == 'ms'
        diff *= 1000
      return diff
    return inner
  return timer

@timer_with_arguments(units='ms')
def factorial(n):
  return 1 if n == 0 else n*factorial(n-1)

factorial(100)
```

* '@' are Pythonic approach to higher-order functions

### Currying
* One argument per function
* Design pattern is a standard solution to a common problem
* Currying is one design pattern that is associated with functional programming
  * Reduce a function with multiple arguments to a chain of higher-order
    function that take one argument

```py
def add(a, b, c):
  return a + b + c

# binding arguments to a function, create a function that takes the first
# argument and returns another function that takes the other one and so on

from functools import partial

# We bind the value 10 to the first argument to value 'a'
add_10 = partial(add, 10)
add_10_100 = parial(add_10, 100)
print(add_10_100(1000))
```

```py
# standard python function that allows us to check how many arguments a function
takes
from inspect import signature

def curry(fnc):
  def inner(arg):
    if len(signature(fnc).parameters) == 1:
      return fnc(arg)
    return curry(partial(fnc, arg))
  return inner

@curry
def add(a, b, c):
  return a + b + c

print(add(10)(100)(1000))
```

### Monads or Variables that decide how they should be treated???
* A Manad is a functional design pattern
* nan (not a number):
  * nan is a special numeric value
  * Any operation on nan returns nan
  * nan * 1 = nan
  * nan overrides operations (as soon as opertion is applied to nan, the
    operation doesn't run the nan is returned right away)
* The Maybe Monad is like nan
  * Two kinds of values
  * Normal values (Just)
  * Invalid values (Nothing)
  * Any function applied to Nothing returns Nothing
* The List Monad ([1,2,4])
  * The list monad defines a series of values
  * A function applied to a List moand is applied to each element
  * The result is a new List monad
* **Monads take control of functions**


```py
def camelcase(s):
  return ''.join([w.capitalize() for w in s.spit('_')])

print(camelcase('some_function'))

class Just:
  def __init__(self, value):
    self._value = value
  def bind(self, fnc):
    try:
      return Just(fnc(self._value))
    except:
      return Nothing()
  def __repr__(self):
    return self._value

class Nothing:
  def bind(self, fnc):
    return Nothing()
  def __repr__(self):
    return 'Nothing'

print(Just('some_function').bind(camelcase))
# SomeFunction
print(Nothing().bind(camelcase))
# Nothing
print(Just(10).bind(camelcase))
# Nothing


# List monad

class List:
  def __init__(self, values):
    self._values = values
  def bind(self, fnc):
    return List([fnc(value) for value in self._values])
  def __repr__(self):
    return str(self._values)

List(['some_text', 'more_text']).bind(camelcase)
# ['SomeTet', 'MoreText']
```
* In Python instead of using a Maybe Monad you can use exceptions because they
  are very friendly way to deal with problems in your code

### Memoization
* Can be used to speed up computational processing
* Referential transparency (a function is ref transparnent when return values depend only on arguments)
* Once a return value has been determined a function never needs to be called again
* We can store the returned valued and return it right-away


```py
# Runs every time
def prime(n):
  for i in range(n, 0, -1):
    if all([i // x != i / x for x in range(i-1, 1, -1)]):
      return i

print(prime(10000000))
# can take time to complete

# We can use Caching to speed up function calls by storing the result in a cache
# Runs only if cache is empty
# This in principal is memoization
cache = {}
def cached_prime(n):
  if n in cache:
    return cache[n]
  for i in range(n, 0, -1):
    if all([i // x != i / x for x in range(i-1, 1, -1)]):
      cache[i]
      return i

# Memoization
# Memoization is a type of caching in which return values are stored for specific arguments. Therefore, the implementation above is an example of memoization. But it can be implemented more elegantly using a decorator!

def memoize(fnc):
  cache = {}
  def inner(*arg):
      if args in cache:
        return cache[args]
      cache[args] = fnc(*args)
      return cache[args]
  return inner

@memoize
def memoize_prime(n):
  for i in range(n, 0, -1):
    if all([i // x != i / x for x in range(i-1, 1, -1)]):
      return i

print(memoize_prime(1000000))
```

### Errors and Exceptions in Lambda Expression
* An Exception is an object
* Can be part of a raise statement
* raise Exception('error!')
* This causes the program to crash
* Unless caught in a try ... except statement
* Both raising and catching exceptions requires statements!!!
  * Statements are not allowed in lambda expression

```py
def add_str(s):
  return sum([int(i) for i in s.split('+')])

print(add_str('1+2'))
# 3
print(add_str(1+2))
# AttributeError no split method on integers

# make add_str safe
def add_str(s):
  try
    return sum([int(i) for i in s.split('+')])
  except AttributeError:
    return None

print(add_str(1+2))
# None

l_add_str = lambda s: sum([int(i) for i in s.split('+')])

print(l_add_str('1+2'))
# 3
print(l_add_str(1+2))
# AttributeError no split method on integers
# But there is no try except for Lambda
```
* In python `except` statement specific which exception we want to catch
* Maybe Monad for Lambda Error Handling
  * A functional approach to error handling
  * A Maybe Monad can give us a Nothing value
  * But not very Pythonic
  * Let's take a more Pythonic approach
  * A Maybe-like decorator
    * In which Exceptions objects are Nothing values
    * Everything else are Just values

```py
l_add_str = lambda s: sum([int(i) for i in s.split('+')])

# A Maybe-like decorator

def maybe(fnc):
  def inner(*args):
    for a in args:
      if isinstance(a, Exception):
        return a
    try:
      return fnc(*args)
    except Exception as e:
      return e
  return inner

safe_add_str = maybe(lambda s: sum([int(i) for i in s.split('+')]))
print(safe_add_str(1+2))
# 'int' object has no attribute 'split'

```
* Exceptons are fine! Event though Exceptions are not entirely compatible with a
  functional programming style, they are still a very good way to deal with
  errors!

### Fully Functional Interactive Calculator

```py
OPERATORS = '+', '-', '*', '/'

def maybe(fnc):
  def inner(*args):
    for a in args:
        if isinstance(a, Exception):
          return a
    try:
      return fnc(*args)
    except Exception as e:
      return e
  return inner

def repeat(fnc, until):
  def inner(*args):
    while True:
      result = fnc(*args)
      if until(result):
        return result
  return inner
 
is_int = lambda i: isinstance(i, int)
get_number = lambda: int(input('Enter an integer: '))
safe_get_number = repeat(maybe(get_number), until=is_int)

is_operator = lambda o: o in OPERATORS
get_operator = lambda: input('Enter an operator: ')
safe_get_operator = repeat(get_operator, until=is_operator)

# single expression
calculate = lambda number1, operator, number2: \
    number1 + number2 if operator == '+' \
    else number1 - number2 if operator == '-' \
    else number1 * number2 if operator == '*' \
    else number1 / number2 if operator == '/' \
    else None # we return None if operator was not valid 

main = lambda: calculate(
            safe_get_number(),
            safe_get_operator(),
            safe_get_number(),
            )

forever = lambda retval: False
main_loop = repeat(lambda: print(main()), until=forever)

main_loop()
```
