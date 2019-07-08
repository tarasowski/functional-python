OPERATORS = '+', '-', '*', '/'

# p_ means procedural implemantation
def p_main() -> int:
    print('Welcome to the barely functional calculator!')
    number1 = p_get_number()
    operator = p_get_operator()
    number2 = p_get_number()
    result = p_calculate(number1, operator,  number2)
    print('The result is: %r' % result)

def p_get_number() -> int:
    while True:
        s = input('Enter an integer: ')
        try:
            return int(s)
        except ValueError:
            print('That is not an integer!')

def p_get_operator():
    while True:
        s = input('Enter an operator (+, -, *, or /): ')
        if s in OPERATORS:
            return s
        print('That is not an operator!')

def p_calculate(number1, operator, number2) -> int:
    if operator == '+':
        return number1 + number2
    if operator == '-':
        return number1 - number2
    if operator == '*':
        return number1 * number2
    if operator == '/':
        return number1 / number2
    raise Exception('Invalid operator!')

#p_main()


# f_ means functional implementation
# every function is a single expression here

# not safe will be refactored later
def f_get_number() -> int:
    return int(input('Enter an integer: '))

# not safe will be refactored later
def f_get_oprator() -> int:
    return input('Enter an operator: ')

# single expression
def f_calculate(number1: int, operator: OPERATORS, number2: int) -> int:
    return number1 + number2 if operator == '+' \
            else number1 - number2 if operator == '-' \
            else number1 * number2 if operator == '*' \
            else number1 / number2 if operator == '/' \
            else None # we return None if operator was not valid 

def f_main() -> int:
    return f_calculate(
            f_get_number(),
            f_get_oprator(),
            f_get_number(),
            )
print('The result is: %s' % f_main())

