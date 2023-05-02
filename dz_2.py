def calculate(expression):
    operands = []
    operators = []
    current_operand = ''
    for character in expression:
        if character in ['+', '-', '*', '/']:
            operators.append(character)
            operands.append(float(current_operand))
            current_operand = ''
        else:
            current_operand += character
    operands.append(float(current_operand))

    while len(operators) > 0:
        if '/' in operators:
            index = operators.index('/')
            new_operand = operands[index] / operands[index+1]
            operands = operands[:index] + [new_operand] + operands[index+2:]
            operators.pop(index)
        elif '*' in operators:
            index = operators.index('*')
            new_operand = operands[index] * operands[index+1]
            operands = operands[:index] + [new_operand] + operands[index+2:]
            operators.pop(index)
        elif '+' in operators:
            index = operators.index('+')
            new_operand = operands[index] + operands[index+1]
            operands = operands[:index] + [new_operand] + operands[index+2:]
            operators.pop(index)
        elif '-' in operators:
            index = operators.index('-')
            new_operand = operands[index] - operands[index+1]
            operands = operands[:index] + [new_operand] + operands[index+2:]
            operators.pop(index)
    return operands[0]

result = calculate(input('Введите математическое выражение: '))
print(result)

assert calculate("2+3*4-5/2") == 10.5
assert calculate("1+2+3+4+5") == 15
assert calculate("10*5-7*3+2") == 23

# У вас ошибки в проверке