# Write helper functions instead of complex expressions
# As soon as your expressions get complicated, it's time to consider splitting them into smaller pieces and moving logic into helper functions.


from urllib.parse import parse_qs
my_values = parse_qs('red=5&blue=0&green=',
                    keep_blank_values=True)

print(repr(my_values))

print('Red:' , my_values.get('red')) # 5
print('Green:' , my_values.get('green')) # 0
print('Opacity:' , my_values.get('opacity')) # None

# It would be nice if a default value of 0 was assigned when a parameter isn't supplied or is blank

def get_first_int(values, key, default=0):
    found = values.get(key, [])
    if found[0]:
        found = int(found[0])
    else:
        found = default
    return found

green = get_first_int(my_values, 'green')

print(green)
