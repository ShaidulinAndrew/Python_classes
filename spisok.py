# список обозначается квадратными скобками и может содержать в себе разные типы данных
some_list = ['hello', 123, True]

# можно объявить пустой список
empty_list = []

# можно список заполнить сразу
friends = ['Max', 'Leo', 'Kate']

# тип списка list
print(type(friends))

# возможен поиск по индексу (начинаются с 0) поиск производится по элементно
# т.е. выводит элемент целиком
print('Второй друг: ', friends[1])  # если используем индекс при выводе получаем строку
print('Первый друг с конца: ', friends[-1])  # первый индекс с конца

# Так же можно применить срезы
print(friends[1:2])
print(friends[:2])
print(friends[1:])

# Проверка длины списка функция len. Показывает количество элементов в строке
print(len(friends))

# Добавление нового элемента в список. Метод .append
friends.append('Ron')
print(friends)
print(len(friends))

# Удаление последнего элемента. Метод .pop
print(friends.pop())  # Удаляет последний элемент и выводит его на экран
print(friends)

# Очищение списка. Метод .clear()
friends.clear()
print(friends)

friends = ['Max', 'Leo', 'Kate']

# Удаление элемента по значению элемента .remove()
friends.remove('Kate')
print(friends)

# Удаление элемента по индексу. Функция .del
del friends[0]
print(friends)
friends = ['Max', 'Leo', 'Kate']

# Оператор in
goals = ['стать гуру языка Python', 'здоровье', 'накормить кота']
if 'здоровье' in goals:
    print('Есть')
else:
    print('Нет')



