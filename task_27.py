# Напишите программу, 
# которая заменяем максимальное значение на минимальное.
def maxreplace (a):
    maxnum = max(a)
    minnum = min(a)
    for i in range(len(a)):
        if a[i] == maxnum:
            a[i] = minnum
    return(a)

list = [2,5,1,5,2,5,1,2]
print(maxreplace(list))