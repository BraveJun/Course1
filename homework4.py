my_string = input('Введите текст: ')
print(f'Колличество символов введенного текста: {len(my_string)}')
print(f'Введенный текст в верхнем регистре: {my_string.upper()}')
print(f'Введенный текст в нижнем регистре: {my_string.lower()}')
print(f'Введенный текст без пробелов: {my_string.replace(' ', '')}')
print(f'Первый символ введенного текста: {my_string[:1]}')
print(f'Последний символ введенного текста: {my_string[len(my_string) - 1:]}')
