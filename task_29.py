# написать программу, которая на ввод принимает число и определеяет
# простое оно или составное. делится на себя и на 1.

def check(n):
    i = 2
    for i in range(2, n):
        if n % i == 0:
            return "no "
    return "yes "

num = int(input("number "))
print(check(num))