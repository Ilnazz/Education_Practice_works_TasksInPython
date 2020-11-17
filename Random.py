import random as rnd

men = ['Марат', 'Ильнур', 'Ильназ', 'Адиль', 'Витя', 'Арсений', 'Фаиль', 'Руслан', 'Амир', 'Раиль']
women = ['Яна', 'Регина', 'Арина', 'Медина', 'Катя', 'Даша', 'Алёна', 'Алина', 'Рузана', 'Юля']

rnd.shuffle(men)
rnd.shuffle(women)

buffer = []

def is_exist(arr):
    m = arr[0]
    w = arr[1]
    for i in buffer:
        if i == (str(m)+str(w)):
            return True
    return False

def get_rand():
    arr = [rnd.randint(0, 9), rnd.randint(0, 9)]
    if is_exist(arr):
        return get_rand()
    else:
        if rnd.random() > 0.5:
            buffer.append(str(arr[0]) + str(arr[1]))
        else:
            buffer.append(str(arr[1]) + str(arr[0]))
        return arr

for i in range(900):
    arr = get_rand()
    m, w = arr[0], arr[1]
    print("{2} день: {0} {1}".format(men[m], women[w], i + 1))
