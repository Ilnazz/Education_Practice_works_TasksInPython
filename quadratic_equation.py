from helpers import ask


def solve_quadratic_equation(a, b, c):
    """Решает квадратное уравнение"""
    D = b ** 2 - 4 * a * c
    if D < 0:
        roots_n = 0
        return roots_n, None, None
    elif D == 0:
        roots_n = 1
        x = (-b) / 2 * a
        return roots_n, x, None
    else:
        roots_n = 2
        x1 = ((-b) + D ** 0.5) / 2 * a
        x2 = ((-b) - D ** 0.5) / 2 * a
        return roots_n, x1, x2


def get_coefficient(letter):
    """Принимает значение буквенного коэффициента letter"""
    while True:
        coef_str = input('Введите значение коэффициента {0}: '.format(letter)).strip()
        try:
            return int(coef_str)
        except ValueError:
            print('Неверное значение коэффициента.')


def main():
    print('Quadratic equation solver v1.0')
    while True:
        # Принимаем коэффициенты
        a = get_coefficient('a')
        b = get_coefficient('b')
        c = get_coefficient('c')
        # Решаем уравнение
        result, x1, x2 = solve_quadratic_equation(a, b, c)

        if result == 0:
            print('Данное квадратное уравнение не имеет действительных решений.')
        elif result == 1:
            print('Ответ: x = {0}'.format(x1))
        else:
            print('Ответ: x1 = {0}; x2 = {1}'.format(x1, x2))

        if not ask('Продолжить работу', 'y', 'n'):
            break


if __name__ == '__main__':
    main()
