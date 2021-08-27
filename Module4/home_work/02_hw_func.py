# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc),
# точки соединены отрезками AB, BC и AC. Найдите отрезок с минимальной длинной.
# Если отрезков с минимальной длиной несколько - вывести любой

# При решении задачи необходимо использовать функцию расстояния между двумя точками.

def distance(x1, y1, x2, y2):
    # TODO: your code here
    dist = ((x2 - x1)**2  + (y2 - y1)**2)**0.5
    return dist

def can_triangle(p1,p2,p3):
    # TODO: your code here
    AB = distance(*p1,*p2)
    BC = distance(*p2,*p3)
    AC = distance(*p1,*p3)
    min = 'AB'
    if AB > BC and AC > BC:
     min = 'BC'
    elif AB > AC: min = 'AC'
    return AB, BC, AC, "Самый короткий отрезок: ", min

# Пример вызова функции
print (can_triangle((10, 12), (14, 12), (12, 12)))
print (can_triangle((6, 6), (7, 6), (5, 6)))
