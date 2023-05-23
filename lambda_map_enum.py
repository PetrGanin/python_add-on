# number = list(map(int, input().split()))
# print(number)
# list_res = list(filter(lambda x: x > 9 and x < 100, number))
# print(list_res)



# 2. Дан список, вывести отдельно буквы и цыфры, пользуясь filter.

# list_1 = [12,"sadf",5643,"save"]
# list_str = list(filter(lambda x: type(x) == str, list_1))
# list_num = list(filter(lambda x: type(x)==int, list_1))
# print(list_num, list_str)

# 3 напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
number = input("enter namber: ")
number = number.replace(",", "")
sum_2 = sum(map(lambda x: int(x), number))
# res = int(map(lambda x: x+res, number))
print(number)
print(sum_2)
