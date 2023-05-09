# передвинуть 1,2,3, на три индекса в право.
array = [1,2,3,4,5,6,7,8,9]
k =3
array2 = array[k:6]+array[:k]+array[6:]
# array2.append(array[k:]+array[:k])
print(array2)