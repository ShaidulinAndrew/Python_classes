# Словарь устроен по принципу ключ: значение

friend = {
    'name': 'Max', 'age': '23'
}

print(type(friend))
print(friend)

print(friend['age'])

# Добавляем в словарь новое значение
friend['has_car'] = True
print(friend)

# Меняем значение в словаре. У одного ключа возможно только одно значение, поэтому
# идет замена значения
friend['has_car'] = False
print(friend)

# удаление значения из словаря
del friend['age']
print(friend)

# оператор in в словаре
if 'has_car' in friend:
    print('Есть машина')

# перебор словаря по ключам
for key in friend.keys():
    print(key)

for key in friend:
    print(key)
    print(friend[key])

# перебор по значениям
for val in friend.values():
    print(val)

# перебор пары ключ значение
for item in friend.items():
    print(item)

for key, val in friend.items():
    print(key)
    print(val)
