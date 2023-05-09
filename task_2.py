# Задача №2 Найдите сумму трехзначного числа.
# 1 решение:
# number = int(input('Введите трехзначное число: '))
# a = (number%100)//10
# b = number%10+number//100
# print(a+b)

# 2 решение:
# number = input("Введите трехзначное число: ")
# a = int(number[0])
# b = int(number[1])
# c = int(number[2])
# print(a+b+c)

# 3 решение:
# number = input("Введите трехзначное число: ")
# Sum = 0
# for i in range(len(number)):
#     Sum+=int(number[i])
# print(Sum)

# Решение №4 через Рондом
import time
from random import random

start_timer = time.time()
number = int(random()*9999999)
print (number)
string = str(number)
Sum = 0
for i in range(len(string)):
    Sum+=int(string[i])
print(Sum)

timer_end = time.time()
timer_sec = timer_end - start_timer
timer_msec = timer_sec * 1000
print(timer_sec)
print(timer_msec)




