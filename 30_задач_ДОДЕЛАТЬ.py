import random

pattern = r'-?\d+'

# Task number 1
cost = float(input("Введите цену 1-го кг конфет: "))
if cost > 0:
    for i in range(1, 11):
        print("{0} кг конфет стоит {1}".format(i, i * cost))
else:
    print("Неверная цена")

# Task number 2
print("Введите последовательность целых чисел, оканчивающуюся нулем.")
nums = []
num = int(input("Введите число: "))
while num != 0:
    num = int(input("Введите число: "))
    nums.append(num)

nums_sum = 0
nums_count = len(nums)

i = 0
while i < nums_count:
    nums_sum += nums[i]
    i += 1


print("Сумма чисел: {0}".format(nums_sum))
print("Количество чисел: {0}".format(nums_count))


# Task number 3
print(("Введите числа A и B (A < B)."))
A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

sum = 0
for n in range(A, B+1):
    sum += n

print("Сумма чисел от A до B: {0}".format(sum))

# Task № 4
print("Введите последовательность отрицательных целых чисел, оканчивающуюся положительным числом.")
nums = []
while True:
    num = int(input("Введите число: "))
    if num < 0:
        nums.append(num)
    else:
        break

nums_sum = 0
nums_count = len(nums)
i = 0
while i < nums_count:
    nums_sum += nums[i]
    i += 1
average = nums_sum / nums_count
print("Среднее арифметическое всех чисел последовательности: {0}".format(average))

# Task № 5
print("Среди чисел 1, 4, 9, 16, 25, ... найти первое число, большее n.")
n = int(input("Введите число n: "))

for i in range(1, n):
    if i*i > n:
        print("{0} > n".format(i*i))
        break

# Task № 6
print("Среди чисел 1, 5 10, 16, 23, ... найти первое число, большее n.")
n = int(input("Введите число n: "))
i = 1
j = 4
while j < n:
    i += j
    j += 1
print("{0} > n".format(j))

# Task № 7
pupils_number = 25
mark_min = 2
mark_max = 5
marks_first = [random.randint(mark_min, mark_max) for _ in range(0, pupils_number)]
marks_second = [random.randint(mark_min, mark_max) for _ in range(0, pupils_number)]
marks_average_first = sum(marks_first) / len(marks_first)
marks_average_second = sum(marks_second) / len(marks_second)
print("Оценки по физике учеников 1-го класса: ")
print(marks_first)
print("Оценки по физике учеников 2-го класса: ")
print(marks_second)
print("Средняя оценка по физике учеников 1-го класса: {0}".format(marks_average_first))
print("Средняя оценка по физике учеников 2-го класса: {0}".format(marks_average_second))

# Task № 8
A = int(input("Введите число A (> 1): "))
K = 1
sum = 0
while sum < A:
    sum += 1/K
    K += 1
sum -= 1/K
print("K: {0}".format(K))
print("Сумма чисел 1 + 1/2 + … + 1/K: {0}".format(sum))
