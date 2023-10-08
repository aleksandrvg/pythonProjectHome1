radius = int(input('Введите радиус круга: '))
arc_length = int(input('Введите длину дуги: '))


def area_sector(radius, arc_length):
    areaSector = arc_length * radius / 2
    return areaSector


print(area_sector(radius, arc_length))
