import random


# ==============================================================================
# Набор вспомогательных функций

def rand_float(min, max):
    """Возвращает случайное вещественное число в диапазоне [min; max], включая обе границы"""
    return min + random.random() * (max-min)


def input_float(prompt):
    """Ввод вещественного числа. Возвращает введенное пользователем число."""
    while True:
        user_input = input(prompt)
        try:
            float_number = float(user_input)
            return float_number
        except ValueError:
            print('Ошибочное число.')


def input_int(prompt):
    """Ввод целого числа. Возвращает введенное пользователем число"""
    while True:
        user_input = input(prompt)
        try:
            int_number = int(user_input)
            return int_number
        except ValueError:
            print('Ошибочное число.')


def input_float_boundaries():
    """Ввод вещественных границ диапазона. Возвращает пару min, max"""
    while True:
        min = input_float('Введите минимальную вещественную границу диапазона (min): ')
        max = input_float('Введите максимальную вещественную границу диапазона (max): ')
        if min > max:
            print('Ошибка: min > max!')
        elif min == max:
            print('Ошибка: min == max!')
        else:
            return min, max


def input_int_boundaries():
    """Ввод целочисленных границ диапазона. Возвращает пару min, max"""
    while True:
        min = input_int('Введите минимальную целочисленную границу диапазона (min): ')
        max = input_int('Введите максимальную целочисленную границу диапазона (max): ')
        if min > max:
            print('Ошибка: min > max!')
        elif min == max:
            print('Ошибка: min == max!')
        else:
            return min, max


def pair_exists(pair):
  for p in known_pairs:
      if p == pair:
        return True
  return False

def new_rand_pair(a, b):
    """Возвращает пару случайных элементов из списков a и b"""
    if len(a) < 1 or len(b) < 1:
        raise Exception('Ошибка: cписок должен содержать хотя бы один элемент.')
    fst = random.choice(a)
    snd = random.choice(b)
    pair = (fst, snd)
    if not pair_exists(pair):
        known_pairs.append(pair)
        return fst, snd
    
    if len(known_pairs) < len(a):
      raise Exception('Ошибка: количество возможных пар исчерпано.')
    
    return pair
# ==============================================================================


# ==============================================================================
# Функции, решающие задачи
def generate_random_float_number():
    print('Генерация случайного вещественного числа в диапазоне [min; max].')
    min, max = input_float_boundaries()
    random_number = rand_float(min, max)
    print('Случайное вещественное число: ', random_number)


def generate_random_odd_int_number():
    print('Генерация случайного нечетного целого числа в диапазоне [min; max].')
    min, max = input_int_boundaries()
    random_number = random.randint(min, max)
    if random_number % 2 == 0:
        if random_number + 1 > max:
            random_number -= 1
        else:
            random_number += 1
    print('Случайное нечетное целое число: ', random_number)


def generate_random_even_int_number():
    print('Генерация случайного четного целого числа в диапазоне [min; max].')
    min, max = input_int_boundaries()
    random_number = random.randint(min, max)
    if random_number % 2 != 0:
        if random_number + 1 > max:
            random_number -= 1
        else:
            random_number += 1
    print('Случайное четное целое число: ', random_number)


def generate_random_int_number_divisible_by_n():
    print('Генерация случайного целого числа в диапазоне [min; max], кратного числу n.')
    min, max = input_int_boundaries()
    n = 0
    while True:
        n = input_int('Введите число n: ')
        if n > max or n < min:
            print('Ошибка: n должно находиться в диапазоне [{0}; {1}].'.format(min, max))
        else:
            break
    random_number = random.randrange(min, max, n)
    print('Случайное целое число, кратное числу {0}: {1}'.format(n, random_number))


def generate_random_pairs():
    print('Генерация случайных пар из списка девочек и мальчиков.')
    girls_number = boys_number = 0
    while True:
        girls_number = input_int('Количество девочек: ')
        boys_number = input_int('Количество мальчиков: ')
        if girls_number < 1 or boys_number < 1:
            print('Ошибка: количество должно быть >= 1.')
        else:
            break
    girls = ['Девочка_№' + str(n) for n in range(1, girls_number+1)]
    boys = ['Мальчик_№' + str(n) for n in range(1, boys_number+1)]
    pairs_number = girls_number * boys_number
    pairs = [new_rand_pair(girls, boys) for _ in range(pairs_number)]
    print('Случайные пары: ')
    for n, p in enumerate(pairs):
        print(n+1, '-', p[0], 'и', p[1])
# ==============================================================================


# ==============================================================================
# Цикл выбора и запуска необходимой программы
if __name__ == '__main__':
    while True:
        print('Выберите программу для запуска:\n'
              '1. Генерация случаного вещественного числа;\n'
              '2. Генерация случайного нечетного целого числа;\n'
              '3. Генерация случайного четного целого числа;\n'
              '4. Генерация случйного целого числа, кратного числу n;\n'
              '5. Генерация случайных пар из списка девочек и мальчиков.')
        program_number = input_int('Номер программы => ')
        print()
        programs = [
            generate_random_float_number,
            generate_random_odd_int_number,
            generate_random_even_int_number,
            generate_random_int_number_divisible_by_n,
            generate_random_pairs
        ]
        if program_number < 1 or program_number > 5:
            continue
        program = programs[program_number-1]
        program()
        input('Нажмите любую клавишу, чтобы продолжить...')
