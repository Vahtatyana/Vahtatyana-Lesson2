year = int(input('Введите год рождения Пушкина А.С.: '))

if year != 1799:
    print('Неверный год рождения')
elif year == 1799:
    date = input('Введите дату рождения Пушкина А.С.: ')
    if date == '6 июня' :
        print('Верно')
    else:
        print('Неверный день рождения')