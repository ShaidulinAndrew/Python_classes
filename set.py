# множества это неупорядоченные коллекции, содержащие неповторяющиеся элементы

cities = ['Las Vegas', 'Paris', 'Moscow', 'Paris', 'Moscow']
print(type(cities))
print(cities)

# пересохраняем в ту же переменную но с типом множество
cities = set(cities)
print(cities)

# Добавим новый элемент множества
cities.add('Burma')
print(cities)

# удаляем элемент
cities.remove('Moscow')
print(cities)

# Взятие длины множества. Выводит количество элементов
print(len(cities))

# Проверка наличия элемента во множестве
print('Paris' in cities)

# Перебор элементов множества через цикл for
for city in cities:
    print(city)

max_things = {'Телефон', 'Бритва', 'Рубашка', 'Шорты'}
kate_things = {'Телефон', 'Шорты', 'Зонтик', 'Помада'}

# Объединение оператор |
print(max_things | kate_things)

# Пересечение &
print(max_things & kate_things)

# Исключение
print(max_things - kate_things)
print(kate_things - max_things)