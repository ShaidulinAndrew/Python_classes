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
