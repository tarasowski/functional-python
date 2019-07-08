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

