from functools import reduce, partial

def pipe(*args):
    def h(x):
        return reduce(lambda a, fn: fn(a), args, x) 
    return h

def mult(x):
    return x * 2

def add(x):
    def n(y):
        return x + y
    return n

def add_(x,y):
    return x + y

result = pipe(mult, 
              mult, 
              mult,
              add(50),
              partial(add_, 100)
              )


print(result(50))
