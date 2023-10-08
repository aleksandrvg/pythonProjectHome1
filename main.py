import math

print('Выберите вариант расчета площади сектора круга')
choice = int(input('1 - по длине дуги, 2 - по количеству секторов: '))


def area_sector1(radius, arc_length):
    areaSector = arc_length * radius / 2
    return areaSector


def area_sector2(radius, number_sectors):
    areaSector = math.pi * radius ** 2 / number_sectors
    return areaSector


if choice == 1:
    radius = int(input('Введите радиус круга: '))
    arc_length = int(input('Введите длину дуги: '))
    print(area_sector1(radius, arc_length))

elif choice == 2:
    radius = int(input('Введите радиус круга: '))
    number_sectors = int(input('Введите количество секторов: '))
    print(area_sector2(radius, number_sectors))

else:
    print('Нет такого варианта расчета')
