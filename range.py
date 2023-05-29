# создает последовательность/ Выводится от 0!

numbers = range(10)
print(numbers)  # сам диапазон не выводится, т.к. имеет специальный класс range
print(type(numbers))

print(list(numbers))  # вывод через list

winners = ['Max', 'Leo', 'Kate']
for i in range(len(winners)):
    print(i)  # индекс элемента из списка
    print(winners[i])  # данные победителя

    print(i+1, ')', winners[i])  # более наглядная форма вывода

# Параметры range (start_or_stop, stop, step)

print(list(range(1, 100, 2)))  # вывод нечетных чисел в строку по порядку

for number in range(1, 100, 2):
    print(number)  # вывод нечетных чисел в столбик
