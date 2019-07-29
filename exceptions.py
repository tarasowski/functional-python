# Exceptions occur during run-time. Your code may be syntactically correct but it may happen that during run-time Python encounters something which it can't handle, then it raises an exception.
# When a Python script raises exception, it creates an Exception object
# IMPORTANT: If the script doesn't handle exception the program will terminate abruptly. If the script handles exception the program will run further

# Python provides us some basic exception classes
    # Class is an object constructor
    # Object has properties (data) and methods (functions)
# Python Built-in Exceptions
    # Exception - base class for all exceptions
    # IndexError - Raised when index of a sequence is out of range
    # KeyError - Raised when the specified key is not found in the dictionary
    # IOError - Raised when an input/output operations fails
    # ValueError - Raised when a function gets argument of corrent type but improper value int('hello world')

# IndexError


def get_val(xs: list, index: int) -> int:
    try:
        res = xs[index]
    except IndexError as e:
        print(e)
    else:
        return res

get_val([1,2,3,4], 5)

print(
get_val([1,2,3,4], 1)
)

# KeyError

def get_key(obj: dict, key: str) -> int:
    try:
        res = obj[key]
    except KeyError as e:
        print(e)
    else:
        return res

get_key({'a': 1, 'b': 2}, 'c')
print(
get_key({'a': 1, 'b': 2}, 'a')
)

# Syntax
'''
try:
    You do your operations here;
except Exception1:
    If there is Exception1, then execute this block
except Exception2:
    If there is Exception2, then execute this block
'''


def load_f():
    try:
        fp = open('myfile.txt')
        line = f.readline()
        i = int(s.strip())
    except (IOError, ValueError) as e:
        print('Please check the file,either the file is read-only')
    except:
        print('Unexpected error')

load_f()

def load_finally():
    try:
        fh = open('test', 'w')
        try:
            fh.write('Test file!!')
        finally:
            print('Closing the file')
            fh.close()
    except IOError:
        print('Error: File not found or is read-only')


load_finally()
# If file could not be created or is read only, then an exception will be thrown, but before the execution of except block, finally block will be executed

# Programs using try-except to handle exception will run slightly slower. Also the size of the code will increase
# Therefore you should use exceptions to handle exceptional circumstances only and not for normal error handling cases
# A try/except block is extremely efficient if no exceptions are raised. Actually catching an exception is expensive


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

# @maybe is a syntactic sugar for maybe(divdiv)(10, 10)
@maybe
def divdiv(x, y):
    return x / y

res10 = divdiv(10, 0)
res20 = divdiv(10, res10)

if isinstance(res20, Exception):
    print('we are getting an exception')
    print(res20)
else:
    print('everything works as expected')
    print(res20)


# Prefer Exceptions to Returning None

def divide(a, b):
    try:
        print(a / b)
        return a / b
    except ZeroDivisionError:
        return None

result = divide(10, 0)
if result is None:
    print('Invalid inputs')

# Other ways to return results without checking for None downstream
def divide_(a, b):
    try:
        return (True, a / b)
    except ZeroDivisionError:
        return (False, None)

# The caller of this function have to unpack the tuple. That forces them to consider the status part instead of just looking at the result value

success, result = divide_(10, 0)
if not success:
    print('invalid inputs')

# The callers can easily ignore the first part of the tuple (using the undersocre variable name, a convention for unused variables)
_, new_result = divide_(10, 0)
if not result:
    print('Invalid inputs')

# The better way to reduce such errors is to never return None at all. Instead, raise an exception up to the caller and make them deal with it.
# Now the caller should handle the exception for the invalid input case
def divide__(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs') from e

try:
    result = divide__(10, 0)
except ValueError:
    print('Invalid inputs')
else:
    print(f'result is {result}')

# ====== From effective python =====

# Use try/finally when you want exceptions to propagate up, but you also want to run cleanup code even when exceptions occur.


def read_file():
    # You must call open before the try block because exceptions that occur when opening the file (like IOError if the file does not exists) should skip the finally block
    handle = open('/tmp/random_data.txt') # May raise IOError
    try:
        data = handle.read() # may raise UnicodeError
    finally:
        print('runs the finally block for cleanup')
        handle.close() # Always runs after try:


#read_file()

# Use try/except/else to make it clear which exceptions will be handleded by your code and which exceptions will propagate up. 
# When the try block doesn't raise an exception, the else block will run. The else block helps you minimize the amount of code in the try block and improves readability
import json
def load_json_key(data, key):
    try:
        result_dict = json.loads(data) # May raise ValueError
    except ValueError as e:
        # If the data isn't valid JSON, then decoding with json.loads will raise a ValueError. The exception is caught by the except block and handled.
        raise KeyError from e
    # The else clause ensures that what follows the try/except is visually distinguished from the except block.
    else:
        # If decoding is successful, then the key lookup will ossur in the else block. If the key lookup raises any exeptions, they will propagate up to the caller because they are outside of the try block.
        # return result_dict[key] - this version is not very safe and raises errors. Use the version from below to define the default value in case the error occurs
        return result_dict.get(key, 10) # May raise KeyError
print(
load_json_key('{"a": 10, "b": 20, "c": 30}', 'c'),
load_json_key('{"a": 10, "b": 20, "c": 30}', 'd'),
)

# Use try/except/else/finally when you want to do it all in one compound statement.
# For example, say you want to read a description of work to do from a file, proces it, and then update the file in place. 

UNDEFINED = object()

def divide_json(path):
    handle = open(path, 'r+')   # May raise IOError
    try:
        data = handle.read()    # May raise UnicodeDecodeError
        op = json.loads(data)   # May raise ValueError
        value = (
                op['numerator'] /
                op['denominator'])  # May raise ZeroDivisionError
    except Exception as e:
        print('comes from exception', e)
        return UNDEFINED
    else:
        op['result'] = value
        result = json.dumps(op)
        handle.seek(0)              # May raise IOError
        handle.write(result)
        return value
    finally:
        print('runs the close() method to cleanup')
        handle.close()
try:
    data = divide_json('tmp/random_data.txt')
except IOError as e:
    print(f'Error {e}')


def load_file():
    try:
        file = open('/tmp/my_file.dat')
        data = file.readfile()
        important_data = data[0]
        print('Data loaded')
    except FileNotFoundError:
        file = open('/tmp/my_file.dat', 'w')
        print('File created')
    except AttributeError:
        print('Attribute Error')
    except:
        print('Some other problem occured')

load_file()
