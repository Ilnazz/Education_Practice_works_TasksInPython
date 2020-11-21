import re
import random

float_pattern = r'(-?[\d]*[.]?[\d]+?)'
int_pattern = r'(-?[\d]+)'

# Task number 1
print("Задание 1")
cost = float(input("Введите цену одного килограмма конфет: "))
for i in range(1, 11):
    print("{0} килограмм конфет стоит {1}".format(i, '%.2f' % (i * cost)))


# Task number 2
print("\nЗадание 2")
sequence = re.findall(int_pattern, input("Введите числа через пробелы: "))
sequence = list(map(lambda x: int(x), sequence))
sum = 0
length_of_sequence = len(sequence)
index = 0
while index < length_of_sequence:
    sum += sequence[index]
    index += 1
print("Сумма чисел последовательности равна {0}\nЧисло членов последовательности равно {1}".format(sum, length_of_sequence))
sequence = None

# Task number 3
print("\nЗадание 3")
a = int(input("Введите число: "))
b = int(input("Введите число, большее чем первое: "))
sum = 0
for i in range(a, b):
    sum += i
print("Сумма чисел от A до B равна {0}".format(sum))

# Task number 4
print("\nЗадание 4")
sequence = re.findall(int_pattern, input("Введите положительные и отрицательные числа через пробелы: "))
sequence = list(map(lambda x: int(x), sequence))
index = 0
count = 0
sum = 0
while index < len(sequence):
    if sequence[index] <= 0:
       count += 1
       sum += sequence[index]
    index += 1
print("Среднее арифметическое неположительных чисел равно {0}".format(sum / count))
sequence = None

# Task number 5
print("\nЗадание 5")
a = int(input("Введите число: "))
b = int(input("Введите число, большее чем первое: "))
squares = 0
for i in range(a, b + 1):
    squares += i ** 2
print("Сумма квадратов чисел от A до B равна {0}".format(squares))

# Task number 6
print("\nЗадание 6")
sequence = re.findall(int_pattern, input("Введите чётные и нечётные числа: "))
sequence = list(map(lambda x: int(x), sequence))
index = 0
sum = 0
while sequence[index] % 2 == 0:
    sum += sequence[index]
    index += 1
print("Сумма первых чётных чисел равна {0}".format(sum))
sequence = None

# Task number 7
print("\nЗадание 7")
a = float(input("Введите число меньше 200: "))
sum = 0
count = 201 - a
for i in range(int(a), 201):
    sum += i
print("Среднее арифметическое чисел от {0} до 200 равно {1}".format(int(a), sum / count))

# Task number 8
print("\nЗадание 8")
sequence = re.findall(float_pattern, input("Введите вещественные числа: "))
sequence = list(map(lambda x: float(x), sequence))
count = 0
while count < len(sequence) and sequence[count] > 0:
    count += 1


print('В начале последовательности записано {0} положительных чисел'.format(count))

# Task number 9
print('\nЗадание 9')
a = int(input("Введите число: "))
b = int(input("Введите число, которое больше или равно первому: "))
sum = 0
for i in range(a, b+1):
    sum += i
print("Сумма чисел от {0} до {1} равна {2}".format(a, b, sum))

# Task number 10
print('\nЗадание 10')
N = int(input('Введите число, которое больше 0 и принадлежит последовательности 2, 4, 8...: '))
k = 0
square = 1
while square != N:
    k += 1
    square *= 2
print('N = 2^K\n{0} = 2^{1}'.format(N, k))

# Task number 11
print('\nЗадание 11')
a = int(input('Введите число, которое больше 0 и меньше 50: '))
sum_of_squares = 0
for i in range(a, 51):
    sum_of_squares += i * i

print('Сумма квадратов чисел от {0} до 50 равна {1}'.format(a, sum_of_squares))

# Task number 12
print('\nЗадание 12')
N = int(input('Введите число, которое больше 1: '))
# 5^k > N
k = 0
square = 1
while square <= N:
    k += 1
    square *= 5

print('5^K > N\nНаименьшее число K, при котором выполняется неравенство, равно {0}\nТак как 5^{0} > {1}\n{2} > {1}'.format(k, N, square))

# Task number 13
print('\nЗадание 13')
sequence = re.findall(int_pattern, input('Введите числа: '))
sequence = list(map(lambda x: int(x), sequence))
length_of_list = len(sequence)
sum = 0
for i in sequence:
    sum += i
print('Сумма членов последовательности равна {0}\nКоличество членов последовательности равно {1}'.format(sum, length_of_list))

# Task number 14
print('\nЗадание 14')
N = int(input('Введите число, которое больше 1: '))
# 2^K > N
K = 0
index = 1
while index <= N:
    k += 1
    index *= 2

# K в любом случае будет равна +∞
print('2^K > N\nK∈({0}; +∞)'.format(k - 1))

# Task number 15
print('\nЗадание 15')
sequence = re.findall(int_pattern, input('Введите нечётные и чётные числа: '))
sequence = list(map(lambda x: int(x), sequence))
sum = 0
for i in sequence:
    sum += i * (i % 2)

print('Сумма первых нечётных членов последовательности равна {0}'.format(sum))

# Task number 16
print('\nЗадание 16')
N = int(input('Введите число: '))
for_print = N
count = 0

while N > 0:
    count += 1
    N //= 10

print('Число {0} состоит из {1} цифр'.format(for_print, count))

# Task number 17
print('\nЗадание 17')
n = int(input('Введите число, которое больше 1: '))
grader = 0
for i in range(1, int(n) + 1):
    if i * i > n:
        grader = i * i
        break

print('Первое число большее, чем {0} равно {1}'.format(n, grader))

# Task number 18
print('\nЗадание 18')
n = int(input('Введите число, которое больше 0: '))
delta = 4
member = 1
while member < n:
    member += delta
    delta += 1

print('Среди чисел последовательности 1, 5, 10, 16, 23, ... первое число большее, чем {0} равно {1}'.format(n, member))
input('Нажмите enter чтобы продолжить...')

# Task number 19
print('\nЗадание 19')
marks = [random.randint(2, 5) for i in range(0, 20)]
print('Оценки учеников по физике')
for y in range(4):
    line = '[  '
    for x in range(5):
        line += '{:<2}'.format(str(marks[x + y * 5]))
    print(line + ' ]')

mid_mark = 0

for i in range(20):
    mid_mark += marks[i]

mid_mark /= 20

print('Средняя оценка равна {0}'.format(mid_mark))

# Task number 20
print('\nЗадание 20')
a = int(input('Введите число: '))

k = 1
sum = 0
while sum < a:
    sum += 1 / k
    k += 1
k -= 1
print('Наибольшее из целых чисел K, для которых сумма 1 + 1/2 + 1/4 ... 1/K будет меньше A равно {0}, '
      '\nсумма этих чисел равна {1}'.format(k, '%.2f' % sum))

# Task number 21
print('\nЗадание 21')
resistances = re.findall(int_pattern, input('Введите сопротивления резисторов: '))
resistances = list(map(lambda x: int(x), resistances))
total_resistances = 0
for i in resistances:
    total_resistances += i

print('Общее сопротивление цепи при последовательном подключении резисторов равно {0}'.format(total_resistances))

# Task number 22
print('\nЗадание 22')
N = int(input('Введите число, которое больше 0: '))
k = 1
while k**2 <= N:
    k += 1
if k != N:
    k -= 1
print('Наибольшее целое число K, квадрат которого не превосходит N: K^2 <= N, равно {0}'.format(k))

# Task number 23
print('\nЗадание 23')
N = int(input('Введите количество учеников в классах: '))
first, second = [random.randint(2, 5) for i in range(N)], [random.randint(2, 5) for i in range(N)]
for y in range(int(N / 4)):
    line_f = '[ '
    line_s = '[ '
    for x in range(int(N / 5)):
        line_f += '{:>2}'.format(str(first[x + y * 4]))
        line_s += '{:>2}'.format(str(second[x + y * 4]))
    print(line_f, ' ]', ' ' * 4, line_s, ' ]')

sum_f, sum_s = 0, 0
for i in range(N):
    sum_f += first[i]
    sum_s += second[i]

print('Средняя оценка в первом классе равна {0}\nСредняя оценка во втором классе равна {1}'.format('%.2f' % (sum_f / N), '%.2f' % (sum_s / N)))
input('Нажмите enter чтобы продолжить...')

# Task number 24
print('\nЗадание 24')
index = 0
while index < 11:
    print('{:<20}'.format('2^{0} = {1}'.format(index, 2 ** index)), '{:<20}'.format('2^{0} = {1}'.format(index * 2, 2 ** (index * 2))))
    index += 1

# Task number 25
print('\nЗадание 25\n12 районов с населением (N) и площадью (S): ')
areas = [(random.randint(2, 10), random.randint(5, 20)) for i in range(12)]
for y in range(3):
    line = '[ '
    for x in range(4):
        line += '{:<14}'.format('(N: {0}, S: {1})'.format(areas[x + y * 3][0], areas[x + y * 3][1]))
    print(line, ' ]')

p = []
index = 0
while index < 12:
    p.append(areas[index][0] / areas[index][1])
    index += 1

print('Плотность населения районов: ')

for y in range(3):
    line = '[ '
    for x in range(4):
        line += '{:<14}'.format('P: {0}'.format('{%.2f}' % p[x + y * 3]))
    print(line, ' ]')

# Task number 26
print('\nЗадание 26')
index = 1
delta = 2
day = 1
while index < 100:
    index += delta + day
    day += 1
    delta *= 2

print('Подарок превысит 100$ к {0} дню рождения'.format(day))

# Task number 27
print('\nЗадание 27')
for i in range(2, 10):
    print('Через {0} часов(а) будет {1} клеток(и)'.format((i - 1) * 3, 2**(i - 1)))

# Task number 28
print('\nЗадание 28')
# y = -0.5x + x
# y = 0.5x
# y = x / 2

min = int(input('Введите минимальный x: '))
max = int(input('Введите маскимальный x: '))
step = float(input('Введите шаг: '))
if step == 0:
    step = 1

index = min

print('{:>5}'.format('x'), '|', '{:>5}'.format('y'))
while index <= max:
    print('{:>5}'.format(index), '|', '{:>5}'.format(index / 2))
    index += step

# Task number 29
print('\nЗадание 29')
first = 10
sum_of_week = 0

for i in range(10):
    print('За {0} день лыжник пробежал {1} км'.format(i + 1, first))
    if i < 7:
        sum_of_week += first
    first *= 1.1
    first = float('%.2f' % first)
print('\nЗа неделю лыжник пробежал {0} км'.format('%.2f' % sum_of_week))

# Task number 30
print('\nЗадание 30')
n = int(input('Введите число: '))
list = list(str(n))

sum = 0
product = 1
index = 0
while index < len(list):
    sum += int(list[index])
    product *= int(list[index])
    index += 1

print('Сумма цифр числа {0} равна {1}'.format(n, sum), '\nПроизведение цифр числа {0} равно {1}'.format(n, product))
