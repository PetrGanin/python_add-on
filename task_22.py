# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.
from random import randint
array = [randint(1,10) for i in range(10)]
print(array)
array2 = [randint(1,10) for i in range(10)]
print(array2)
for i in array2:
    if i not in array:
        array.append(i)
print(array)
array.sort()
print(array)
arr = set(array)
print(arr)

# эталонное решение:
# mol = [int(x) for x in input().split()]
# n = mol[0]
# m = mol[1]
# set_1 = set()
# set_2 = set()
# list_1 = list()
# a = [int(x) for x in input().split()]
# k = set(a)
# for i in k:
# set_1.add(i)
# b = [int(x) for x in input().split()]
# k1 = set(b)
# for i in k1:
# set_2.add(i)
# lok = set_1 & set_2
# kool = list(lok)
# kool.sort()
# for i in kool:
# print(i, end=' ')