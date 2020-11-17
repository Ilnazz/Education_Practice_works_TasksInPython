def input_three_numbers():
    return int(input("Введите число: ")), int(input("Введите число: ")), int(input("Введите число: "))

# Задания 1
print("Задание 1")
for i in range(1, 6):
    print(str(i) + ". " + "0"*25)

print("\n"*2)

# Задание 2
print("Задание 2")
result = 0
for i in range(1, 101):
    result += i

print(result)

print("\n" * 2)

# Задание 3
print("Задание 3")

a, b, c = input_three_numbers()

nums = [a, b, c]

def are_there_equal_numbers(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if i == j:
                continue
            if arr[i] == arr[j]:
                return "yes"
    return "ERROR"


print(are_there_equal_numbers(nums))
print("\n" * 2)

# Задание 4
print("Задание 4")
a, b, c = int(input("Введите число: ")), int(input("Введите число: ")), int(input("Введите число: "))
if a + b == c or a + c == b or b + c == a:
    print("yes")
else:
    print("no")

print("\n" * 2)

# Задание 5
print("Задание 5")

a, b, c = int(input("Введите число: ")), int(input("Введите число: ")), int(input("Введите число: "))
positive_nums = 0
if a >= 0:
    positive_nums += 1
if b >= 0:
    positive_nums += 1
if c >= 0:
    positive_nums += 1
print("{0}, {1}, {2}. количество положительных: {3}".format(a,b,c,positive_nums))

print("\n" * 2)


# Задание 6
print("Задание 6")

for i in range(1, 498):
    if i % 2 == 0:
        print(i)


print("\n" * 2)


# Задание 7
print("Задание 7")

result = 0
for i in range(1, 15):
    result += i
print(result)


print("\n" * 2)


# Задание 8
print("Задание 8")


result = 1
for i in range(1, 9435):
    if i % 2 == 1:
        result *= i

print(result)
