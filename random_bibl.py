from random import randint, choice, sample, shuffle
# 1. загадайте случайное число от 1 до 100
print(randint(0,100))
# 2. выброть победителя лотереи из списка players
players = ['Max', 'leo', 'Kate', 'Rone', 'Bill', 'Ermi']
print(choice(players))
# 3. выбрать 3 победителей лотереи из списка players
print(sample(players, 3))
# перемешать карты в стопке
cards = ['5','9', '13', '0', 'q', 'K', 'a', 'M', 'D']
shuffle(cards)
print(cards)