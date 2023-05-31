from functional import create
from interface import interface
import os
path = "phone_book.txt"
create(path)
enter = 0
fileContent = 0
while enter != 4:
    enter = interface()
    if enter == 1:
        from functional import add_cont
        stroka = str(input("Введите ФИО и номер телефона через пробел "))
        add_cont(path, stroka)
    elif enter == 2:
        from functional import show_all
        print(show_all(path))
    elif enter == 3:
        from functional import search
        stroka = str(input("Введите фамилию "))
        search(path, stroka)
    elif enter == 5:
        from functional import delete
        delete('phone_book.txt')
    elif enter == 6:
        from functional import delete_name, add_cont
        delete_name(path, fileContent)
        stroka = str(input("Введите ФИО и номер телефона через пробел "))
        add_cont(path, stroka)

print("спасибо за работу")