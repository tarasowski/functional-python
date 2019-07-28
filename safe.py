def safe(f):
    def inner(*args):
        for a in args:
            if isinstance(a, Exception):
                return a
        try:
            return f(*args)
        except Exception as e:
            return e
    return inner

# @safe is syntactic sugar for safe(divide)(20, 0)
@safe
def divide(x, y):
    return x / y



print(f'from safe function {divide(20, 0)}')


def divide_(x, y):
    return x / y

# won't get executed an exception has been raised that is unhandled which leads to termination of the program
print(f'from unsafe function {divide_(20, 0)}')




