f = open('first.txt', 'r')

f.clouse()#файл необходимо закрывать, чтобы не кушало систему

#закрытие череч виф
with open('first.txt', 'r') as f:
    for line in f:
        print(line)