numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(f'Список чисел: {numbers}')
primes = []
not_primes = []
for i in range(len(numbers)):
    sum_del = 0
    if numbers[i] != 1:
        for j in numbers:
            if j > numbers[i]:  # Этот if нужен, чтобы отсеить ненужные делители
                break
            if numbers[i] % j == 0 and j > 1:  # Решил сделать через проверку кол-ва делителей
                sum_del += 1
        if sum_del > 1:
            not_primes.append(numbers[i])
        elif sum_del == 1:
            primes.append(numbers[i])
print(f'Простые числа из заданного списка: {primes}')
print(f'Не простые числа из заданного списка: {not_primes}')
