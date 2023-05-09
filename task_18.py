# Задача 18: Требуется найти в массиве A[N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# Ввод: 5
# Ввод: 1 2 6 4 9
# Ввод: 8
import random
number = int(input("введите число: "))

listrandom = [random.randint(0,9) for i in range(number)]
print(listrandom)

N = int(input("Введите число, для поиска близкому по значению: "))
first = abs(N - listrandom[0])

main = listrandom [0]
for i in range(1, len(listrandom)):
    if first > abs(listrandom[i] - N):
        first = abs(listrandom[i] - N)
        main = listrandom[i]

print(f'Ближайшее число к {N} в списке {listrandom} является {main}')