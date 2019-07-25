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

divide_json('tmp/random_data.txt')


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
