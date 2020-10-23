"""Запускает одну из программ по выбору"""

from helpers import input_number
import linear_equation
import linear_equations_system
import quadratic_equation
import area_of_trapezoid
# Предлагаем выбрать программу для запуска
option = input_number('Выберите программу для исполнения: \n'
                      '1) Решение линейного уравнения\n'
                      '2) Решение системы линейных уравнений\n'
                      '3) Решение квадратного уравнения\n'
                      '4) Нахождение площади трапеции\n'
                      '> ')
# Запускаем выбранную программу
if option == 1:
    linear_equation.main()
elif option == 2:
    linear_equations_system.main()
elif option == 3:
    quadratic_equation.main()
elif option == 4:
    area_of_trapezoid.main()
else:
    print('Неверный вариант. Попробуйте снова.')
