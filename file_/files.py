'===================Module & package=================='
# файл с расширением .py - это module
# несколько модулей - это пакет 


'==============File============'
#open() - функция которая открывает файл в определенном режиме

#r - read (только для чтения)
#w - write (только для записи, каждый раз файл очищается)
#a - append (только для дозаписи, добавляется в конец)
#x - создает файл, но если он существует выйдет ошибка


'=================READ================'
# file = open('test1.txt', 'r')
# print(dir(file))
# print(file.writable()) # False потому что открыли в режиме чтения
# print(file.readable()) #True

# print(file.read()) # метод read 
# file.seek(0) # индекс с которого надо читать и повторное чтение
# print(file.read(8)) #  индекс сколько надо читать

# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())  #readline() - возврвщает str

# print(file.readlines())  #возвращает list с элементами str



# print(file.tell()) # функция которая показывает где находится каретка
# file.close()

'==============WRITE=============='
# file = open('test1.txt', 'w')
# file.write('Makers HELLO WORLD')
# file.writelines(['hello world\n makers\n bootcamp'])

# file.close()


'=============APPEND============'
# добавляет в конец

# file = open('test1.txt', 'a')
# file.write('py33\n')
# file.seek(0)
# file.write('py32\n')


'====================Контекстный менежер===================='
#with

with open('test1.txt') as f:
    print(f.read())

print(f.closed) #True - файл закрылся


