# Посчитать факториал (произведение 1 до N) и треугольное число ( сумма чисел от 1 до N) для числа N **Через рекурсию**
def factorial (N):
    if N == 0:
        return 1
    return factorial(N-1)*N

def Sumnumber (N):
    if N == 0:
        return 1
    return Sumnumber(N-1)+N

num1 = int(input('number sum '))
print(Sumnumber(num1))

num = int(input('number '))
print(factorial(num))

