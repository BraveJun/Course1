def enter():
    n = int(input('Введите число от 3 до 20 для подбора пароля: '))
    return n


def selection():
    for i in range(1, number):
        numbers.append(i)
    for j in numbers:
        for k in numbers[j:]:
            pair = j + k
            if number % pair == 0:
                result.append(j)
                result.append(k)


'''
Если в парах пароля допустимы нули и одинаковые числа:

def selection():
    for i in range(number):
        numbers.append(i)
    for j in numbers:
        for k in numbers[j:]:
            pair = j + k
            if pair == 0:
                continue
            elif number % pair == 0:
                result.append(j)
                result.append(k)
'''

while True:
    number = enter()
    result = []
    numbers = []
    if number > 20 or number < 3:  # защита от дурака
        print('Вы ввели неподходящее число!')
        continue
    else:
        selection()
    print('Ваш пароль: ', *result, sep='')
    break  # можно убрать break, если после вывода пароля нужно снова запрашивать число
