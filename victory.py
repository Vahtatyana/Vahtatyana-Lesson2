kol = 0
vsego = 5

#1795
otv = input("Введите год рождения А.С.Грибоедова: ")
if otv == "1795":
    print("Верно")
    kol = kol + 1
else:
    print("Не верно")

#1803
otv = input("Введите год рождения В.Ф.Одоевского: ")
if otv.lower() == "1803":
    print("Верно")
    kol = kol + 1
else:
    print("Не верно")

#1809
otv = input("Введите год рождения Н.В. Гоголя: ")
if otv.lower() == "1809":
    print("Верно")
    kol = kol + 1
else:
    print("Не верно")

#1812
otv = input("Введите год рождения А.И. Герцена: ")
if otv.lower() == "1812":
    print("Верно")
    kol = kol + 1
else:
    print("Не верно")

#1711
otv = input("Введите год рождения М.В. Ломоносова: ")
if otv.lower() == "1711":
    print("Верно")
    kol = kol + 1
else:
    print("Не верно")

print(kol, "верных ответов из", vsego)
print(vsego - kol, "неверных ответов из", vsego)
print((kol / vsego) * 100, "% верных ответов из", vsego)
