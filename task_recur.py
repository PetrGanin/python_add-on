# Дано натуральное число Н и последовательность из Н элементов.
# требуется вывести последовательность из Н элементов в обратном порядке.

def rotate (n):
    if n == 0:
        return " "
    else:
        a = int(input("введите элементы: "))
        return rotate(n-1) + f" {a} "
    

n = int(input("enter N "))
print(rotate(n))