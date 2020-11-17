import re

user_input = input('Введите числа через пробелы: ')

numbers_in_strings = re.findall(r'-?\d+\.?\d*', user_input)

numbers = list(map(lambda num_str: float(num_str), numbers_in_strings))

print('Вы ввели числа: ', numbers)

sorted_numbers = sorted(numbers)

print('Отсортированный список чисел: ', sorted_numbers)

middle = len(sorted_numbers) // 2

print('Срединное число списка: ', sorted_numbers[middle])
