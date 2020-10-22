import re
from helpers import ask

# Определяем шаблон для линейного уравнения вида [-]kx [+-] b = [-]c
equation_pattern = r'(-*\d*)\s*x\s*([+-]\s*\d*)?\s*=\s*(-?\d+)'
# Специальный объект, предоставляющий возможность проверки соответствия строки шаблону
equation_matcher = re.compile(equation_pattern, re.IGNORECASE | re.ASCII)


def is_equation(s):
    """Проверяет, является ли строка s линейным уравнением вида [-]kx [+-] b = c"""
    return equation_matcher.fullmatch(s) is not None


def extract_kbc(equation):
    """Извлекает значения коэффициентов k, b и c из линейного уравнения вида [-]kx [+-] b = c"""
    match = equation_matcher.match(equation)
    raw_k, raw_b, raw_c = match.groups()
    # Обработать k
    if raw_k == '':
        k = 1
    elif raw_k == '-':
        k = -1
    else:
        k = int(raw_k)
    # Обработать b
    if raw_b is None:
        b = 0
    else:
        raw_b = raw_b.replace(' ', '')
        if raw_b == '+':
            b = 1
        elif raw_b == '-':
            b = -1
        else:
            b = int(raw_b)
    # Обработать c
    c = int(raw_c)
    # Вернуть коэффициенты
    return k, b, c


def solve_equation(eq):
    """Решает линейное уравнение вида [-]kx [+-] b = [-]c"""
    # Извлекаем коэффициенты
    k, b, c = extract_kbc(eq)
    # Производим проверки и возвращаем результат
    if b == 0:
        if k != 0:
            return c / k
        return 'Уравнение не имеет решений.'
    elif k == 0:
        if b == c:
            return 'Уравнение имеет бесконечное множество решений.'
        else:
            return 'Уравнение не имеет решений.'
    else:
        return (c - b) / k


def input_equation():
    """Принимает линейное уравнение"""
    while True:
        eq = input('Введите линейное уравнение: ').strip()
        if not is_equation(eq):
            print('Уравнение задано неверно.')
        else:
            return eq


def main():
    print('Linear equation solver v1.0')
    while True:
        # Принимаем линейное уравнение
        eq = input_equation()
        # Решаем уравнение
        x = solve_equation(eq)
        print(x)
        if not ask('Продолжить работу', 'y', 'n'):
            break


if __name__ == '__main__':
    main()

