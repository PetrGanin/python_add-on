# Задача 28. Напишите рекурсивную функцию sum(a,b), возвращающую сумму
# двух целых неотрицательных чисел. нельзя использовать цикл, и доступно арифметическая
# операция 1+ и 1-.

def sum(a,b):
    if a == 0:
        return b
    return sum(a-1, b+1)
A = int(input("number 1 "))
B = int(input("number 2 "))
print(sum(A,B))