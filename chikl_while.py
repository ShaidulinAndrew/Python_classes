# Перебор пока не будет введен правильный ответ

name = input('Кто создатель Python? ')

while name != 'Гвидо':
    print('Не верно')
    name = input('Кто создатель Python? ')

print('Верно')

# использование break

name = None

while name != 'Гвидо':  # возможна замена на конструкцию while True
    name = input('Кто создатель Python? ')
    if name == 'Гвидо':
        break
    print('Не верно')  # данное сообщение не выводится так как после проверки имени на соответствие break

print('Верно')

# Вывод чисел от 0 до 100

number = 0

while number <= 100:
    print(number)
    number += 1  # тоже самое, что и number = number + 1 (увеличение счетчика)

# Вывод чисел от 0 до n

number = 0
n = int(input('Введите n: '))

while number <= n:
    print(number)
    number += 1

# Вывод четных чисел от 0 до n

number = 0
n = int(input('Введите n: '))

while number <= n:
    if number % 2 == 0:
        print(number)
    number += 1

# Вывод не четных чисел от 0 до n с оператором continue

number = 0
n = int(input('Введите n: '))

while number <= n:
    if number % 2 == 0:
        number += 1
        continue  # Идет пропуск найденных четных чисел. Вывод "Наоборот"
    print(number)
    number += 1

# Использование while - else

number = 0

while number <= 100:
    print(number)
    number += 1  # тоже самое, что и number = number + 1 (увеличение счетчика)
    if number == 33:
        break  # Если цикл остановлен break на экран выводится print('end')
else:
    print('else - end')  # вывод данного сообщения на экран будет только тогда, когда цикл завершен

print('end')

# пример использования while

while True:  # Цикл будет исполняться пока не будет выполнено условие
    number = int(input('Введите число: '))
    if 0 < number < 10:
        print(number*2)
        break
    else:
        print('Число должно быть больше 0 и меньше 10')

