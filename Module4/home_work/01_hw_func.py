# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    if len(str(ticket_number)) == 6:
      if int(str(ticket_number)[0])+int(str(ticket_number)[1])+int(str(ticket_number)[2]) == int(str(ticket_number)[::-1][0]) + int(str(ticket_number)[::-1][1]) + int(str(ticket_number)[::-1][2]):
       return "Счастливчик"
      else: return "Не повезло"
    else: return "Введите шестизначный номер билета"
    pass


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
