# Практическое задание
# 1: Создайте функцию, принимающую на вход имя, возраст и город проживания человека. Функция должна возвращать строку вида «Василий, 21 год(а), проживает в городе Москва»
# 2: Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.
# 3: Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health = 100,
# damage = 50. ### Поэкспериментируйте с значениями урона и жизней по желанию. ### Теперь надо создать функцию attack(person1, person2).
# Примечание: имена аргументов можете указать свои. ### Функция в качестве аргумента будет принимать атакующего и атакуемого.
#  ### В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого. 
#  # Функция должна сама работать со словарями и изменять их значения.

# def human():
#     name = input('name;')
#     age = int(input('age; '))
#     city = input('city; ')
#     print(f'{name}, {age}, проживает в городе {city}.')

# human()
# def number ():
#     a = []
#     for i in range(3):
#         number1 = int(input('enter a number'))
#         a.append(number1)
#     print(a)
#     print(max(a))
# number()

# морской бой, стреляют по разу.
player_name = input('Введите имя: ')
player = {
    'name': player_name,
    'health': 100,
    'damage': 50,
}
enemy_name = input('Введите имя: ')
enemy = {
    'name': enemy_name,
    'health': 30,
    'damage': 45,
}

def attack(unit, target):
    target['health'] -=unit['damage']
attack(player, enemy)
print(enemy)

attack(enemy, player)
print(player)