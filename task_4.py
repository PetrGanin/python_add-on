# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10

Sum = int(input("Введите число, которое делится на 6: "))
user1 = Sum//6 
user2 = user1
user3 = (user1 + user2)*2
if Sum%6 == 0:
    print(f"Петя и Сережа сделали по - {user1} журавлика а Катя сделала - {user3} журавликов")
else:
    print("вы ввели неправельное число")