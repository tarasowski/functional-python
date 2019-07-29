def curry(func):
    def curried(*args, **kwargs):
        if len(args) + len(kwargs) >= func.__code__.co_argcount:
            return func(*args, **kwargs)
        return (lambda *args2, **kwargs2:
                curried(*(args + args2), **dict(kwargs, **kwargs2)))
    return curried

@curry
def myfun(a,b,c):
    return a + b + c 

fn1 = myfun(10)(20)
fn2 = fn1(20)

print(fn2)




