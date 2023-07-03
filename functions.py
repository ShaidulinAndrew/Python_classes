# Функция это фрагмент программного кода (подпрограмма), к которму можно обратиться
# из другого места программы

print(abs(-7)) # модуль числа

numbers = [5, 15, 33, 8, 1, -7, 0]
print(min(numbers))
print(max(numbers)) # минимальное, максимальное значение


print(round(10.6547, 2)) # округление числа (2 число - количество знаков сокращения)

print(sum(numbers)) # сумма элементов последовательности

winners = ['Leo', 'Kate', 'Max']
for number, winner in enumerate(winners, 1): # нумерация последовательсности
    print(number, winner)

# Пользователь вводит 3 числа. Найти мин макс и сумму
# numbers = []

# for i in range(3):
    # number = int(input('Введите число: '))
    # numbers.append(number)
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))

# создание собственных функций

def print_sep ():
    print('-' * 100)

print_sep()

def print_sep2 (sep): # в скобочках указан параметр, который можно менять
    print(sep * 100)

print_sep2('*')
print_sep2('-')
print_sep2('+')


def print_sep3 (sep, sep_len): # в скобочках указан параметр, который можно менять
    print(sep * sep_len)

print_sep3('*', 100)
print_sep3('-', 75)
print_sep3('+', 50)

def get_sep(sep, sep_len):
    return sep * sep_len

sep = get_sep('-', 50)
text = 'Hello {} Func {}'.format(sep, sep)

print(text)

# Значение аргументов по умолчанию
def greeting(who, say='Hello'):
    print(say,who)
greeting('Leo')
greeting('Leo', 'Hi')

# args* kwargs**
def greeting(say, *args): # *who = *args
    print(say, args)
greeting('Hello', 'Leo', 'Max', 'Kate') # Будет кортеж из параметров

def get_person(**kwargs):
    for k,v in kwargs.items():
        print(k, v)
get_person(name='Leo', age=20, has_car=True)

# Локальные и глобальные переменные
def some_f():
    a = 999  # локальная переменная
    print('Переменная внутри функции: ', a)

a = 1  # глобальная переменная
some_f()
print('Переменная после выполнения функции: ', a)

# Можно изменить глобальную переменную внутри функции, но есть риск что во всем коде переменная будет заменена
global_var = 1

def my_f():
    global global_var
    local_var = 100
    print(local_var)
    print(global_var)
    global_var = 999

my_f()
print(global_var)

# функция как объект
def some_f():
    return 10
result = some_f()
print(result)

a = some_f # Сохраняем функцию в переменную
print(a())

#
def my_filter(numbers):
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
    return result

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_filter(numbers))

# Передача параметра в виде функции
# Если нужны нечетные числа
def my_filter(numbers, function):
    result = []
    for number in numbers:
        if function(number):
            result.append(number)
    return result

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def is_even(number):
    return number % 2 == 0

print(my_filter(numbers, is_even))

def is_not_even(number):
    return number % 2 != 0

print(my_filter(numbers, is_not_even))

# Если нужны числа больше 4
def bigger_4(number):
    return number > 4

print(my_filter(numbers, bigger_4))

# lambda-функции используются в одном месте

print(my_filter(numbers, lambda number: number < 5))

# функция sorted
# параметры функции sorted (iterable - последовательность, key - ключ для сортировки, reverse - порядок)

numbers = [1, 8, 6, 4, 2, 7, 3]
print(sorted(numbers))
print(sorted(numbers, reverse=True))

# города и численность населения
cities = [('Москва', 1000), ('Лас-Вегас', 2000), ('Антверпен', 500)]
print(sorted(cities)) # сортировка происходит по городу

def by_count(city):
    return city[1] # указание на элемент кортежа по которому необходимо провести сортировку

print(sorted(cities, key=by_count))
print(sorted(cities, key=by_count, reverse=True))
print(sorted(cities, key=lambda city: city[1], reverse=True))

# функция filter позволяет фильтровать последовательности
# параметры функции filter (function - функция фильтрации, iterable - последовательность)

names = ['Max', 'Leo', 'Kate', 'Andrew']  # необходимо получить строки больше трех символов

print(list(filter(lambda x: len(x)>3, names)))

# функция map - применение функции к каждому элементу последовательности
# параметры функции map(func - функция, iterable - последовательность)

numbers = [1, 8, 6, 4, 2, 7, 3]
print(list(map(lambda z: z**2, numbers)))
print(list(map(lambda z: str(z), numbers)))