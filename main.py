# Запросите от пользователя число, сохраните в переменную,
# прибавьте к числу 2 и выведите результат на экран.

# number = int(input('Введите любое число: '))
# print(number+2)

# Используя цикл, запрашивайте у пользователя число, пока оно не станет больше 0, но меньше 10.
# После того, как пользователь введет корректное число, возведите его в степень 2 и выведите на экран.

# while True:  # Цикл будет исполняться пока не будет выполнено условие
#     number = int(input('Введите число: '))
#     if 0 < number < 10:
#         print(number*2)
#         break
#     else:
#         print('Число должно быть больше 0 и меньше 10')

# Создайте программу “Медицинская анкета”, где вы запросите у пользователя следующие данные:
# имя, фамилия, возраст и вес.
# Выведите результат согласно которому:
# Пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
# Пациенту требуется заняться собой, если ему более 30 и вес меньше 50 или больше 120 кг
# Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.

# first_name = input('Введите Ваше имя: ')
# last_name = input('Введите Вашу фамилию: ')
# age = int(input('Введите Ваш возраст: '))
# weight = int(input('Введите Ваш вес: '))
#
# if age < 30 and 50 < weight < 120:
#     print(f'Привет {first_name, last_name}, при Вашем возрасте {age} лет и весе {weight} кг, Вы в отличной форме!')
# elif age > 30 and (weight < 50 or weight > 120):  # скобки используются для группировки, так правильнее
#     print(f'Привет {first_name, last_name}, при Вашем возрасте {age} лет и весе {weight} кг, Вам нужно заняться собой!')
# elif age > 30 and (weight < 50 or weight > 120):
#     print(f'Привет {first_name, last_name}, при Вашем возрасте {age} лет и весе {weight} кг, Вам обратиться к врачу!')
# else:
#     print('Какой то иной ответ')
