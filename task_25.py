# Пользователь вводит 2 числа А и B,
# нужно возвести в целую степень число А в B.
def degree (a,b,c):
    if b != 0:
        c *=a
        b -=1
    else:
        return c
    return degree (a,b,c)

num1 = int(input("Введите число А: "))
num2 = int(input("Введите число B: "))
c = 1
print(degree(num1 ,num2,c))

