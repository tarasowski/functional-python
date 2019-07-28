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


safe_add_str = maybe(lambda s: sum([int(i) for i in s.split('+')]))
print(safe_add_str(1+2))
