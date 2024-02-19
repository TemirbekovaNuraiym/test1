'=============Типы данных строки(String)============='

# String - это неизменяемый тип данных, который преназначен для хранения текста, заключенного в одинарные либо двойныекавычки
# string1 = 'строка с одинарными кавычками'
# string2 = "строка с двойными кавычками"
# #string3 = 'строка не правильная"
# string4 = "Don't"#внутри двойной все одинарные = просто символы
# string5 = '''для больших текстов используем три открывающие и три закрывающие'''
# 'Многострочный текст в одинарных кавычках, можно использовать любые'


# string6 = 'hello' + ' ' + 'world'
# print(string6)


# string7 = 'hello world' * 8
# # print(string7)


'======================Экранизация строк============================='
# '\n' #перерносит текст на нрвую строку
# print('hello\nworld') 
# прерносит слово после бэкслеша на строку ниже



# '\t'  #табуляция
# print('hello\tworld')
# #hello   world

# str1 = 'don\'t' #отображает кавычку
# print(str1)

# str2 = "don\"t"
# print(str2)

# str3 = 'символ - \\'
# print(str3)


# '\v' #перенос на новую строку со смещением вправо на длину предыдущей строки (делает лесинку)

# print('hello\vworld\vmakers\vbootcamp')

# '\r' #перенос каретки на начало строки (слово после r стоновится в начало)

# print('makers bootcamp\r Hello')



'=================Форматирование строк==============='
#1
# title = 'iPhone14'
# price = 150
# format_1 = 'Мой телефон', title, 'стоит',price, 'долларов'
# print(format_1)

# format_2 = f'мой телефон {title} стоит {price} долларов' 
# print(format_2)

# первый способ форматирования это с помощю f и фигурных скобок

# #2
# string = 'Название: {} Цена: {} $'
# print(string. format ('iPhone', 150))

#3
# string = 'Название: %s Цена: %s'
# print(string % ('iPhon', 150))



'=================Методы строк=================='

# методы - функции которы относятся к определенному классу к ним модно орбращаться через точку

# print(dir(str))

# string = 'makers'
# print(string.upper()) #метод делает текст юольшими юуквами
# print(string.lower()) # делает малентким
# print(string.swapcase()) # меняет каждую букву наоборот

# print(string.title()) #первые буквы делает заглавным каждое слово
# print(string.capitalize()) #делает заглавным только первую букву первого слово
# print(string.center('10' ',')) #добвит пробелы справа и слева чтобы текст стал по серидине(также можноо указать какой то символ после цифры)
# print(string.count('h')) #считает сколько таких символов в тексте как в скобке
# print(string.startswith('a')) #проверяет с какой буквы начинается слово ( bool булевый тип данных)(true or false)
# print(string.endswith(d)) #так же как и предыдущий только с конца

# print(string.islower()) # проверяет является ли все символы в перерменной с маленькой
# print(string.isupper()) # таеже только с большими
# все команды которые начинаются на is это для проверки

# string = '234243545'
# print(string.isdigit()) #проверка на цифру в тексте True
# print(string.isalpha()) # проверка на буквы в тексте False

# print(string.isalnum()) #проверяет на цифры и буквы или все вместе, но если добавить символ какой то то выйдет ошибка

# string = 'hello world makers bootcamp'
# print(string.split()) #делит текст на части по пробелу или же вместо пробелов можно поставить что то другое
#join() соеденяет 

# string = 'hello'
# reversed_s = string[::-1]
# print(reversed_s) # делает слово наоборот





# title = 'iPhone14'
# price = 150
# format_1 = 'Мой телефон', title, 'стоит',price, 'долларов'
# # print(format_1)

# format_2 = f'мой телефон {title} стоит {price} долларов' 
# print(format_2)


'=============================================РАЗДЕЛ ИНДЕКСА==================================================='

#индекс - это порядковый номер элемента последовательност(символа в строке), (индексация начинатся с 0)

'h e l l o    w  o  r  l  d'
#0 1 2 3 4 5  6  7  8  9  10
# string = 'hello world'
# print(string[0])#h
# print(string[7])#o
# print(string[10])#d
# print(string[-1])#d

# #срезы - это подстрока(часть строки) string[start:end:step]
# string = 'hello world'
# print(string[3:5])#lo
# print(string[6:]) #world
# print(string[:])#hello world
# print(string[:5])#world
# print(string[::-1])#dlrow olleh
# print(string[::2])#hlowrd
# print(string[::3])#hlwl
# print(string[::4])#hor



string = 'hello world'
string1 = string[::-1]
# print(string1[])



string = 'hello world'
#print(string[-1]+string[1:4]+string[0])

string1 = 'hello'
string2 = 'world'
#print(f'{string1} {string2}')

string = 'bskjvcnlkmdc'
res = string[:5] + 'K' + string[6:]
#print(res)

string = 'The quick brown fox jumps over the lazy dog' 
# print(string.replace('o', '*'))


string = 'hello'
# print(string[1:3])



string = "  hello  "
length = len(string.strip())
# print(f'{string.strip()} {length}')



a = string
print(a * 3)




#13
number_str = input('Введите числа через запятую: ')
list_ = number_str.split(',')
list_.sort()
print(list_)


#11
string = 'hello'
print(string[-1]+string[1:-1]+string[0])

#14
string = 'hello'
print(string[1:-1:2])


#Объявите переменную string со значением в виде любой строки.

#Размножьте строку три раза, при этом каждое повторение должно быть на новой строке, необходимо использовать экранирование.
string = 'hello\n'
print(string * 3)

#Объявите переменную string со значением в виде любой строки.Необходимо найти индекс буквы 'e'.
string = 'hello'
print(string.index("e"))