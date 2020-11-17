# 1
def average(a=0,b=0,c=0):
    return (a+b+c) / 3

print(average(a=1,b=10,c=100))

# 2
def solve_system(a1,b1,c1,a2,b2,c2):
    D = a1*b2 - a2*b1
    x = (c1*b2 - c2*b1) / D
    y = (a1*c2 - a2*c1) / D
    return (x, y)

print(solve_system(2,5,16,2,7,20))

# 3
def get_minutes(N):
    return N % 3600 // 60

N = int(input('Введите сколько секунд прошло с начала суток: '))

minutes = get_minutes(N)

print('С последнего часа прошло {0} минут'.format(minutes))

# 4

def get_number_of_day(k):
    return k % 7 + 1

def get_name_of_day(n):
    days = {
        1: 'понедельник',
        2: 'вторник',
        3: 'среда',
        4: 'четверг',
        5: 'пятница',
        6: 'суббота',
        7: 'воскресенье'
    }
    return days[n]

k = int(input('Введите день года 1-365: '))
n = get_number_of_day(k)
name = get_name_of_day(n)

print('{0} день года - {1}.'.format(k, name))
