import math

# Площадь сектора круга
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


# Сумма чисел
def sum_range(start, end):
    sum = 0
    res = start
    while res < end + 1:
        sum += res
        res += 1
    print(f'Сумма чисел от {start} до {end} равно {sum}')


print('Сумма чисел')
start1 = int(input('Введите 1-е число: '))
end1 = int(input('Введите 2-е число: '))
if start1 > end1:
    start2 = end1
    end2 = start1
else:
    start2 = start1
    end2 = end1
sum_range(start2, end2)
