age = int(input('Введите Ваш возраст: '))

if age < 18:
    print('В доступе отказано')
elif age == 18:
    print('Доступ ограничен')
elif age > 18 and age < 30:
    print('Доступ разрешен')
else:
    print('Разрешен доступ ко всем разделам сайта')

print('Пользовательское соглашение')