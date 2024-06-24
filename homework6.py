my_dict = {'Мансур': 1999, 'Лена': 1990, 'Артур': 2002, 'Наташа': 1985}
print(f'Исходный словарь: {my_dict}', '\n')
print(f'Известный год рождения: {my_dict['Мансур']}')
print(f'Если указан неизвестный год рождения: {my_dict.get('Максим', 'Год рождения не найден')}', '\n')
my_dict.update({'Сергей': 1997, 'Даша': 2000})
print(f'Дополненный словарь: {my_dict}', '\n')
outcast = my_dict.pop('Артур')
print(f'Словарь с удаленной парой: {my_dict}', '\n' + f'Значение удаленной пары: {outcast}', '\n'*2)

my_set = {1, 2, 1, 2, 'Руки', 'Вверх', 'Руки', 'Вниз', (1, 2, 3), (1, 2, 3)}
print(f'Мое множество: {my_set}', '\n')
my_set.add('Влево')
my_set.add('Вправо')
print(f'Множество с двумя добавленными элементами: {my_set}', '\n')
my_set.discard('Вверх')
print(f'Множество с одним удаленным элементом: {my_set}')
