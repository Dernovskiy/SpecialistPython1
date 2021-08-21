# Напишите функцию, находящую среднее арифметическое всех аргументов
# Функция должна вызываться с любым количеством аргументов

def average(*args):
    i = 0
    sum = 0
    for number in args:
      sum= sum + number
      i+=1
    return sum/i

print(average(3, 4, 8))
print(average(1, 4, 5, -3, 8, 4))
print(average(-10, 12, 6.3, -5.5, 7, 0.2))
