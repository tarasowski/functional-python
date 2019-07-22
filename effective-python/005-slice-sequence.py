# Python includes syntax for slicing sequences into pieces.
# Slicing can be extended to any Python class that implementes the __getitem__ and __setitem__ special methods
# The basic for of sclicing syntax is somelist[start:end], where start is inclusive and end is exclusive


a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

def slicing_a():
    print('First four: ', a[:4])
    print('Last four: ', a[-4:])
    print('Middle two', a[3:-3])
    # when slicing form the start leave out the zero index
    assert(a[:5] == a[0:5])
    # when slicing to the end of the list leave out the final index
    assert(a[5:] == a[5:len(a)])
    # using negative numbers is helpful for doing offset relative to the end of the list
    assert(a[:] == a)
    assert(a[:5] == a[0:5])
    assert(a[:-1] == a[0:len(a) - 1])
    assert(a[-3:] == a[-3:len(a)])
    # The result of slicing a list is a whole new list. Modifying the result of slicing won't affect the original list
    b = a[4:]
    print('Before:      ', b)
    b[1] = 99
    print('After:       ', b)
    print('No change:   ', a)
    c = a[:]
    # if you leave out both the start and the end indexes when slicing, you'll end up with a copy of the original list
    assert(c == a and c is not a)
    #If you assign a slice iwth not start or end indexes, you'll replace its entire contents iwth a copy of what's referenced (instead of allocating a new list)
    z = a
    print('Before', a)
    a[:] = [ 101, 102, 103]
    assert(a is z)
    print('After ', a)


if __name__ == '__main__':
    slicing_a()
