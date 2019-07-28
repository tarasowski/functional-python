from functools import reduce, partial

pipe = lambda fns: lambda x: reduce(lambda v, f: f(v), fns, x)

def mult(x):
    return x * 2

def add(x):
    def n(y):
        return x + y
    return n

def add_(x,y):
    return x + y

result = pipe([mult, 
              mult, 
              mult,
              add(50),
              partial(add_, 100),
              (lambda x: print(f'print result of pipe: {x}') or x)
              ])

result(50)
