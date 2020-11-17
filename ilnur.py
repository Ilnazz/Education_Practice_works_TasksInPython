import re

pattern = r'(-?\d*.?\d?\s*[-\+\*/]-?\d*.?\d?)'

def user_input():
    user_input = input('Введите выражение: ')
    if re.match(pattern, user_input) is not None:
        return user_input
    return user_input()

user_input = user_input()

numbers = re.findall(r'-?\d+\.?\d?', user_input)
numbers = list(map(lambda x: float(x), numbers))

sign = re.findall(r'[-\+\*/]', re.findall(r'\d\s*[-\+\*/]\s*\d', user_input)[0])[0]

if sign == '+':
    print(numbers[0] + numbers[1])
elif sign == '-':
    print(numbers[0] - numbers[1])
elif sign == '*':
    print(numbers[0] * numbers[1])
elif sign == '/':
    print(numbers[0] / numbers[1])
