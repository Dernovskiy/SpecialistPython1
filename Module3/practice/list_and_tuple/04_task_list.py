# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

my_list = [2,3,4,-7]
sum_number = 0
for number in my_list[:]:
    if number >= 0:
     sum_number = sum_number + number
    number += 1
print('Сумма всех элементов = ',sum_number)
