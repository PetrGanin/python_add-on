# вывести уникальные значения из списка. количество уникальных значений
a = [1,1,2,0,-1,3,4,4, 5,6]
b = []
for i in a:
    if(not i in b):
        b.append(i)
print(len(b))
print(len(set(a)))