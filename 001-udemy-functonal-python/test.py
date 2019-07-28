import itertools

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
