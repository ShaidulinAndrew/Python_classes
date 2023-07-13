# Запросите от пользователя число, сохраните в переменную,
# прибавьте к числу 2 и выведите результат на экран.

# number = int(input('Введите любое число: '))
# print(number+2)

# Используя цикл, запрашивайте у пользователя число, пока оно не станет больше 0, но меньше 10.
# После того, как пользователь введет корректное число, возведите его в степень 2 и выведите на экран.

#while True:  # Цикл будет исполняться пока не будет выполнено условие
     #number = int(input('Введите число: '))
     #if 0 < number < 10:
         #print(number*2)
         #break
     #else:
         #print('Число должно быть больше 0 и меньше 10')

# Создайте программу “Медицинская анкета”, где вы запросите у пользователя следующие данные:
# имя, фамилия, возраст и вес.
# Выведите результат согласно которому:
# Пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
# Пациенту требуется заняться собой, если ему более 30 и вес меньше 50 или больше 120 кг
# Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.

#first_name = input('Введите Ваше имя: ')
#last_name = input('Введите Вашу фамилию: ')
#age = int(input('Введите Ваш возраст: '))
#weight = int(input('Введите Ваш вес: '))

#if age < 30 and 50 < weight < 120:
    #print(f'Привет {first_name, last_name}, при Вашем возрасте {age} лет и весе {weight} кг, Вы в отличной форме!')
#elif age > 30 and (weight < 50 or weight > 120):  # скобки используются для группировки, так правильнее
    #print(f'Привет {first_name, last_name}, при Вашем возрасте {age} лет и весе {weight} кг, Вам нужно заняться собой!')
#elif age > 30 and (weight < 50 or weight > 120):
    #print(f'Привет {first_name, last_name}, при Вашем возрасте {age} лет и весе {weight} кг, Вам обратиться к врачу!')
#else:
    #print('Какой то иной ответ')

# Тест

#print('Соревнования по Python')
#count = int(input('Введите количество участников: '))
#i = count  # счетчик учистников
#members = []

#while i > 0:
    #name = input('Кто занял {} место'.format(i))
    #members.append(name)  # добавляем участников в список members
    #i-=1  # уменьшаем счетчик участников
#print('В соревнованиях участвовали: ', members)

#members.reverse()  # т.к. участников записывали с конца, нужно перевернуть список через reverse
#result = members[:3]
#result = 'Победители: {}. Поздравляем!'.format(result)
#print(result)

# Даны два произвольных списка. Удалите из первого списка элементы присутствующие во втором списке
# my_list_1 = [2, 5, 8, 2, 12, 12, 4]
# my_list_2 = [2, 7, 12, 3]

#my_list_1 = set(my_list_1)
#my_list_2 = set(my_list_2)
#print(list(my_list_1 - my_list_2))
#  решение через set неверное

# for number in my_list_1:
#     if number in my_list_2:
#         my_list_1.remove(number)
# print(my_list_1)
# # так же неверное решение
#
# for number in my_list_1[:]:
#     if number in my_list_2:
#         my_list_1.remove(number)
# print(my_list_1)
# # верное решение. необходимо взять срез, тогда когда мы делаем удаление из списка
#
# # Дана дата в формата дд.мм.гггг. Задача вывести дату в текстовом виде например второе ноября 2013 года
# date = '13.01.1987'
# d, m, y = date.split('.')
# print(d, m, y)
#
# months = {
#     '01': 'Января', '02': 'Февраля', '03': 'Марта', '04': 'Апрелья', '05': 'Мая', '06': 'Июня',
#     '07': 'Июля', '08': 'Августа', '09': 'Сентября', '10': 'Октября', '11': 'Ноября', '12': 'Декабря'
# }
#
# days = {
#     '01': 'Первое', '02': 'Второе', '03': 'Третье', '04': 'Четвертое', '05': 'Пятое', '06': 'Шестое',
#     '07': 'Седьмое', '08': 'Восьмое', '09': 'Девятое', '10': 'десятое', '11': 'одиннадцатое', '12': 'двенадцатое',
#     '13': 'тринадцатое', '14': 'четырнадцатое', '15': 'пятнадцатое', '16': 'шестнадцатое', '17': 'семнадцатое',
#     '18': 'восемнадцатое', '19': 'девятнадцатое', '20': 'двадцатое', '21': 'двадцать первое', '22': 'двадцать второе',
#     '23': 'двадцать третье', '24': 'двадцать четвертое', '25': 'двадцать пятое', '26': 'двадцать шестое',
#     '27': 'двадцать седьмое', '28': 'двадцать восьмое', '29': 'двадцать девятое', '30': 'тридцатое', '31': 'тридцать первое',
# }
#
# result = f'{days[d]} {months[m]} {y} года'
# print(result)
#
# # Дан список заполненный произвольными числами. Получить новый список
# # элементами которого будут только уникальные элементы исходного
# numbers = [1, 1, 1, 2, 3, 3, 4, 4, 4, 5, 1, 2, 7]
#
# result = []
# for number in numbers: # проверяем числа в списке
#     if numbers.count(number) == 1: # если число встречается в спике один раз, добавляем в переменную
#         result.append(number)
# print(result)
#
# # Игра загадать число
# import random
#
# number = random.randint(1, 100)
# print(number)
#
# user_number = None
# count = 0
# levels = {1: 10, 2: 5, 3: 3}
#
# level = int(input('Выберите уровень сложности от 1 до 3: '))
# max_count = levels[level]
#
# user_count = int(input('Введите количество игроков: '))
# users = []
# for i in range(user_count):
#     user_name = input(f'Введите имя игрока {i}: ')
#     users.append(user_name)
# print(users)
#
# is_winner = False
# winner_name = None
#
# while not is_winner:
#     count += 1
#     if count > max_count:
#         print('Все пользователи проиграли')
#         break
#     print(f'Попытка № {count}')
#     for user in users:
#         print(f'Ход пользователя {user}')
#         user_number = int(input('Введите число: '))
#         if user_number == number:
#             is_winner = True
#             winner_name = user
#             break
#         elif number < user_number:
#             print('Ваше число больше загаданного')
#         else:
#             print('Ваше число меньше загаданного')
# else:
#     print(f'Победитель {winner_name}')

# написать функцию принимающую на вход имя, возраст и город проживания. На выходе строка
# строка вида "Василий, 21 год(а), проживает в городе Москва

def info_person(name, year, city):
    result = f'{name}, {year}, год(а) проживает в городе {city}'
    return result
print(info_person('Ivan', 21, 'New York'))
print(info_person('Sergey', 25, 'Moscow'))

# написать функцию принимающую на вход три числа, на выходе большее из них

def max_of_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

print(max_of_three(35, 18, 23))

def get_max(a, b, c):
    result = max(a, b, c)
    return result
result = get_max(35, 18, 23)
print(result)
print(get_max(35, 18, 23))

# игра атака

player_name = input('Введите имя игрока: ')
player = {
    'name': player_name,
    'health': 100,
    'damage': 50,
    'armor': 1.2
}

enemy_name = input('Введите имя врага: ')
enemy = {
    'name': enemy_name,
    'health': 50,
    'damage': 30,
    'armor': 1
}

def get_damage(damage, armor):
    return damage / armor
def attack(unit, target):
    damage = get_damage(unit['damage'], target['armor'])
    target['health'] -= damage

attack(player, enemy)
print(enemy)

attack(enemy, player)
print(player)

#