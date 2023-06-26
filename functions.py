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
