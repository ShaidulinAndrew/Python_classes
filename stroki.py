name = 'Андрей'  # Строка определяется текстом в кавычках. '' или "" или ''' '''
print(type(name))  # Проверка типа данных str

# взятие символа по индексу
name = 'Андрей'
first_letter = name[0]  # 0 - это номер символа в строке. Символы начинаются с 0!!!
print(first_letter)
first_letter = name[-1]  # берем символ с конца строки. Используется знак -
print(first_letter)

# срезы
print(name[1:3])  # срез с 1 по 3 символ
print(name[:3])  # срез с начала строки по 3 символ не включительно
print(name[4:])  # срез с 4 символа до конца строки

# функция len
friends = 'Андрей Максим Иван'
print(len(friends))  # определяем из скольки символов состоит строка включая пробелы

# метод find (поиск подстроки)
print(friends.find('Максим'))  # поиск с какого символа начинается подстрока. Если подстрока не найдена возвращается -1

hero = 'Superman'
if hero.find('man') != -1:
    print('Есть')


# метод split (разбивка)
print(friends.split())  # разбивает строку через пробел в список
friends = 'Андрей$ Максим$ Иван'
print(friends.split('$'))  # разделитель указывается в кавычках

# метод isdigit
print(friends.isdigit())  # метод проверяет состоит ли строка только из цифр, если да то True если нет то False

# метод upper
print(friends.upper())  # приведение всех символов к верхнему регистру

# метод lower
print(friends.lower())  # приведение всех символов к нижнему регистру

# оператор in  # проверка наличия подстроки в строке
hero = 'Superman'

if 'man' in hero:
    print('Есть')

# поиск через функцию find
if hero.find('man') != -1:
    print('Есть')

