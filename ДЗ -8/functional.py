# 55.  Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Поиск по фамилии
# from func import *


# privet()

# 1 - Интерфейс
# 2 - работа с файлом
# 3 - алгоритм


# 1 - добавление контакта
# 2 - вывод всех
# 3 - поиск по фамилии
# 4 - выход

def create(path): # создание файла
    try:
        file = open(path, 'r')
    except IOError:
        print('Создан новый справочник -> phone_book.txt ')
        file = open(path, 'w')
    finally:
        file.close()

def add_cont(file_name, stroka): # добавление контакта
    data = open(file_name, 'a')
    data.write(stroka + "\n")
    data.close()

def show_all(file_name): # вывод всех контактов
    data = open(file_name, "r")
    for line in data:
        print(line[:-1])
    data.close()

def search(file_name, stroka): # поиск
    a = 0
    data = open(file_name, 'r')
    for line in data:
        if stroka in line:
            print(line)
            a = 123
            break
    if a != 123:
        print("нет такого")
    data.close()

def delete(name):
    import os
    os.remove(name)

def delete_name(fName, fileContent):
    if fileContent == 0:
        with open(fName, 'r',) as file:
            fileContent = list()
            for line in file.readlines():
                fileContent.append((list(line.split())))
    print(fileContent)

# Удаляет информацию из файла
    user = int(input('введите номер имени по индексу'))
    del fileContent[user]
    print(fileContent)
    with open(fName, 'w') as file:  #перезапись в файл
        file.writelines("%s\n" % place for place in fileContent)

        


