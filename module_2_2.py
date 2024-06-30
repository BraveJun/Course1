first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third =  int(input('Введите третье число: '))
if first == second and first == third and second == third:
    print('Колличество чисел с равным значением: 3')
elif first == second or first == third or second == third:
    print('Колличество чисел с равным значением: 2')
else:
    print('Колличество чисел с равным значением: 0')