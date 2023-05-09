# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]
import random
start = int(input("введите начало диапозона 1-100 : "))
end = int(input("введите конец диапозона 1-100: "))
listrandom = [random.randint(0,100) for i in range(20)]
print(listrandom)
indexDiopozon = []
for i in range(len(listrandom)):
    if listrandom[i] >=start and listrandom[i] <= end:
        indexDiopozon.append(i)

print(indexDiopozon)