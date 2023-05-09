# открываем файл на чтение
f = open('first.txt', 'r')
print(f.read())
# f = open('first.txt', 'w')#запись файла
# print(f.read())

# пробегаемся по файлу
for line in f:
    print(line.replace('/n', '')) #убираем перенос строки replace /n на пустую.
for line in f:
    print(line)

f.close()