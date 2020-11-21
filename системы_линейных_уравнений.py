"""Решает систему линейных уравнений"""

import re
from helpers import ask

# Определяем шаблон для линейного уравнения вида [-]ax [+-] by = [-]c
equation_pattern = r'(-*\d*)\s*x\s*([+-]\s*\d*)\s*y\s*=\s*(-?\d+)'
# Специальный объект, предоставляющий возможность проверки соответствия строки шаблону
equation_matcher = re.compile(equation_pattern, re.IGNORECASE | re.ASCII)


def is_equation(s):
    """Проверяет, является ли строка s линейным уравнением вида [-]ax [+-] by = [-]c"""
    return equation_matcher.fullmatch(s) is not None


def extract_abc(equation):
    """Извлекает значения коэффициентов a, b и c из линейного уравнения вида [-]ax [+-] by = [-]c"""
    match = equation_matcher.match(equation)
    raw_a, raw_b, raw_c = match.groups()
    # Обработать a
    if raw_a == '':
        a = 1
    elif raw_a == '-':
        a = -1
    else:
        a = int(raw_a)
    # Обработать b
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
    return a, b, c


def solve_system(eq1, eq2):
    """Решает систему линейных уравнений eq1 и eq2 по методу Крамера"""
    # Извлекаем коэффициенты
    a1, b1, c1 = extract_abc(eq1)
    a2, b2, c2 = extract_abc(eq2)
    # Вычисляем определители
    d = a1 * b2 - b1 * a2
    dx = c1 * b2 - b1 * c2
    dy = a1 * c2 - c1 * a2
    # Если главный определитель равен 0, тогда система не имеет решений
    if d == 0:
        return None, None
    # Вычисляем x и y
    x = dx / d
    y = dy / d
    return x, y


def input_equation(txt):
    """Принимает линейное уравнение"""
    while True:
        eq = input(txt).strip()
        if not is_equation(eq):
            print('Уравнение задано неверно.')
        else:
            return eq


def main():
    print('Linear equations system solver v1.0\n'
          'Система из двух линейных уравнений вида:\n'
          '[-]ax [+-] by = [-]c\n'
          'Где a, b, c - целые числа\n'
          'Пример уравнения: -6x + 5y = -10')
    while True:
        # Принимаем линейные уравнения
        eq1 = input_equation('Введите первое уравнение: ')
        eq2 = input_equation('Введите второе уравнение: ')

        # Решаем систему из двух уравнений
        x, y = solve_system(eq1, eq2)
        if x is None:
            print('Данная система уравнений не имеет решений.')
        else:
            print('Ответ: ({0}; {1})'.format(x, y))

        if not ask('Продолжить работу', 'да', 'нет'):
            break


if __name__ == '__main__':
    main()

