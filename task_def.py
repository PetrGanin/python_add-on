def sum_int(*args):
    res = 0
    for i in args:
        res+=i
    return res

print(sum_int(10,20,13,18))