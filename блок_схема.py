def input_number(txt):
    return float(input("Введите число {0}:".format(txt)))


a1, a2, a3 = input_number("a1"), input_number("a2"), input_number("a3")
b1, b2 = input_number("b1"), input_number("b2")
c1, c2 = input_number("c1"), input_number("c2")
x = input_number("x")

if x >= 1:
    # Находит минимальное среди c1, c2
    min = c1
    if c2 < min:
        min = c2
    # Находит максимальное среди b1, b2
    max = b1
    if b2 > max:
        max = b2
    # Находит максимальное среди max и min
    if min > max:
        max = min
    y1 = max
    print(y1)
else:
    # Если x находится в промежутке (-1; 1)
    if (-1 < x) and (x < 1):
        # Находит минимальное среди a1, a2, a3
        min = a1
        if a2 < min:
            min = a2
        if a3 < min:
            min = a3
        y2 = min
        print(y2)
    # Если x находится в промежутке (-Inf; -1]
    else:
        y3 = 1
        print(y3)
