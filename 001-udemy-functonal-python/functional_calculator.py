OPERATORS = '+', '-', '*', '/'

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

def repeat(fnc, until):
  def inner(*args):
    while True:
      result = fnc(*args)
      if until(result):
        return result
  return inner
 
is_int = lambda i: isinstance(i, int)
get_number = lambda: int(input('Enter an integer: '))
safe_get_number = repeat(maybe(get_number), until=is_int)

is_operator = lambda o: o in OPERATORS
get_operator = lambda: input('Enter an operator: ')
safe_get_operator = repeat(get_operator, until=is_operator)

# single expression
calculate = lambda number1, operator, number2: \
    number1 + number2 if operator == '+' \
    else number1 - number2 if operator == '-' \
    else number1 * number2 if operator == '*' \
    else number1 / number2 if operator == '/' \
    else None # we return None if operator was not valid 

main = lambda: calculate(
            safe_get_number(),
            safe_get_operator(),
            safe_get_number(),
            )

forever = lambda retval: False
main_loop = repeat(lambda: print(main()), until=forever)

main_loop()
