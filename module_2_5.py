def get_matrix(n, m, value):
    matrix = []
    for j in range(n):
        stroki = []
        matrix.append(stroki)
        for k in range(m):
            stroki.append(value)
    return matrix


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
print('')

for i in result1:  # решил вывести матрицы визуально
    print(i)
print('')
for i in result2:
    print(i)
print('')
for i in result3:
    print(i)
