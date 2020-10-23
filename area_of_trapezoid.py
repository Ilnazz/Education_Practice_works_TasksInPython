"""Находит площадь трапеции"""

from math import sqrt
from helpers import ask, input_number


def main():
    print('Trapezoid solver v1.0')
    while True:
        # Запрашиваем тип трапеции
        trapezoid_type = input_number(
              'Выберите тип трапеции:\n'
              '1)Произвольная; 2)Равнобедренная; 3)Прямоугольная.\n'
              'Введите номер варианта > ')
        # Инициализируем значения оснований и высоты
        a, b, h = 0, 0, 0
        # Произвольная трапеция
        if trapezoid_type == 1:
            a = input_number('Меньшее основание: ')
            b = input_number('Большее основание: ')
            h = input_number('Высота: ')
        # Равнобедренная трапеция
        elif trapezoid_type == 2:
            a = input_number('Меньшее основание: ')
            b = input_number('Большее основание: ')
            c = input_number('Боковая сторона: ')
            h = sqrt(c ** 2 - ((a - b) ** 2) / 4)
        # Прямоугольная трапеция
        elif trapezoid_type == 3:
            a = input_number('Меньшее основание: ')
            b = input_number('Большее основание: ')
            h = input_number('Боковая сторона, перпендикулярная основанию: ')
        else:
            print('Неверный вариант. Повторите ввод.')
            continue

        S = (a + b) / 2 * h
        print('Площадь равна: ', S)

        if not ask('Продолжить работу', 'y', 'n'):
            break


if __name__ == '__main__':
    main()
