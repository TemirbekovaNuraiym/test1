'===============Логические и условные операторы====================='

# логические операторы - выражения которые возвращают True или False

# 'равенство'
# 3 == 4 # False
# 4 == 4 # True

# 'не равенство'
# 4 != 5 # True
# 3 != 3 # False

# 'больше'
# 10 > 0 # True
# -8 > 2 # False

# 'меньше'
# 5 < 4 # False
# 5 < 10 # True

# 'больше или равно'
# 4 >= 10 #False
# 10 >= 5 #Ttue

# 'меньше или равно'
# 10 <= 5 # False
# 5 <= 10 # True

# a = 10
# b = '10'
# a == b
# так не правильно. строки можно сравнивать, но не иешать типы данных между собой


# a = 4
# b = 6
# print(a + b > 9)
# print(a < b - 3)
# print(a <= - b)
# print(a != b)
# print(b == a)


# print(a >= 12 and b < 34)




'==============And, Or, Not================='
# and - и (что бы получить True обе стороны должны быть True или с одной стороны, в остальных случаях будет False)
# or - или 
# not - не


# a = 5
# b = 6

# a == 5 and b ==6 # True
# True and True

# a == 5 and b == 3 #Fals
# True and False 

# a > 10 and b < 2 # False
# False and False 

'-------------------------------------------------------------------------------------------------------'

# a = 20 
# b = 5

# a == 20 or b > 1 # True
# True or True 

# a == 20 or b < 1 # True 
# True or False 

# если хотя бы одна часть выражения True то возвратится True

'----------------------------------------------------------------------------------------------------------'


# # not False - True
# # not True - False

# a = 5
# not a < 10 # False
# not a != 5 # True

# not not not not not a != 10 # True

'---------------------------------------------------------------------------------------------------------'


# a = 59 
# s = 32

# print(a + 5 > s)

# print(a != s and a < 34)
# print(a - 9 > s or (s + 4 == a))

'=============================Boolean Type======================================='
# булевый тип данных имеет всего два значения. используется для решения ситуативных задач

# bool(1) # True
# bool(0) # False
# bool(-123) # True


# bool('hello') # True
# bool(' ')  # True
# bool('') # False

# bool([]) #False
# bool([[]]) # True

# bool(True) # True
# bool(False) # False

'================================None Type===================================='
# None - неизменяемый тип данных с одним значением - None, который используется для обознояения отсуоствя значения

# a = None
# print(a)


'==========================Условные операторы==========================='

# условные операторы - конструкция, которая используется для тогочтобы при разных входных данных код работал по разному

# if условие 1:
#    тело1

#    if условие:
#       тело 1 # тело1 булет выполнять если условие1 - True. выполняется если условие1 - True

      

#  if условие1:
#    тело1
# elif условие2:
#    тело2

# if num > 0:
#     print(f'Число {num}')








# x = 54
# y = 23
# # print(y)

# x = 85
# y = 67
# z = 90
# if y < x and z:
#     print(y)
# else:
#    print(False)
    
#  if 5 == 5:
#      print(True)


# user_data = int(input('Введите число'))

#  if user_data > 5:
     # print('Number is the bigger then 5')
# elif user_data < 5:
     # print('not correct')




"================Тернарный операторы================"

#only 'IF' and 'ELSE'
# telo1 if uslovlie else telo2

# a = 2
# res = a ** 2 if a > 0 else a - 2
# print(res)
# a = int(input())
# if a>0:
#     res = a**2
# else:
#     a-2
# print(res) 

# это для логики



'++++++++++++++++++++++++++++++++Логический тип данных (Таски с практики)++++++++++++++++++++++++++++++++++++++++'

# mark = int(input())
# if mark >= 90:
#     print('Отлично, ваша оценка 5!')
# elif mark >= 80:
#     print('Здорово, ваша оценка 4!')
# elif mark >= 70:
#     print('Хорошо, Ваша оценка 3!')
# elif mark >= 60:
#     print('Вам стоит подучить материал')
# else:
#     print('Вы не сдали экзамен')

'_____________________________________________'


# number = int(input())
# if number < 0:
#     print('negative')
# elif number > 0:
#     print('positive')
# elif number == 0:
#     print('zero')

'________________________________________________'

# x = 23
# y = 23
# z = 87
# print(min(x, y, z))

'_________________________________________________'

# x = 23
# y = 23
# z = 87
# if x == y == z:
#     print('3')
# elif y == x or y == z or z == x:
#     print('2')
# else:
#     print('0')

'___________________________________________________'


# x = int(input("Введите первое число: ")) 
# y = int(input("Введите второе число: ")) 
# if x % y == 0: 
#     print("x делится на y") 
#     print("Частное:", x // y) 
# else: 
#     print("x не делится на y") 
#     print("Частное:", x // y) 
#     print("Остаток:", x % y)

'____________________________________________________'

# year = int(input())
# if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
#     print('YES')
# else:
#     print('NO')

'___________________________________________________________________________'


# greeting = (input())
# if greeting == 'Hi':
#     print('Привет')
# else:
#     print('NO')


# count = 0 
# number = input("Введите строку как числа ") 
# if number.isdigit(): 
#     count = int(number) 
#     print(count)
# elif (number.isdigit() == int(number) and number !=0): 
#     print(conut:=number)


# count = 0
# number = input('Ввкдите строку:')
# if number.isdigit() and number == str():
#      count = int(number)
#      print(count)
# else:
#      print('Ошибка')

"_________________________________________________"

# labels = ['Honda', 'Kawasaki']
# for i in labels:
#     print('I like brand:' + i)

"___________________________________________________"

# count = 0 
# number = str(input('Введите строку с числом: ')) 
# if number.isdigit(): 
#      number = int(number) 
#      count = count + number 
#      print(count)

"_______________________________________________________"

# lang = 'ru'
# if 'ru' in lang:
#     print('Это русский' )
# elif 'en' in lang:
#     print('This is english')
# elif 'de' in lang:
#     print('Das ist Deutsch')
# elif 'kg' in lang:
#     print('Бул кыргыз тили')

"__________________________________________________________"

# string = '123456' 
# first_num = string[0] + string[1] + string[2] 
# second_num = string[3] + string[4] + string[5] 
# if int(first_num) == int(second_num): 
#      print('да') 
# else: 
#      print('нет')

"________________________________________________________________"

# a = int(input('Ведите число: '))
# b = int(input('Ведите число: '))
# c = int(input('Ведите число: '))
# if a <= b and a <= c and b <= c: 
#      print(a,b,c)
# elif a <= c and a <= b and c <= b: 
#      print(a,c,b) 
# elif b <= a and b <= c and a <= c: 
#      print(b,a,c) 
# elif b <= c and b <= a and c <= a: 
#      print(b,c,a) 
# elif c <= a and c <= b and a <= b: 
#      print(c,a,b) 
# elif c <= b and c <= a and b <= a:
#      print(c,b,a) 
# else: print(a,b,c)

"__________________________________________________________________"

# age = int(input('Введите ваш возраст: '))
# if age < 18:
#     print('Доступ запрещен')
# else:
#     print('Добро пожаловать')

"_________________________________________________________"

# month=int(input()) 
# if month>12: 
#     print("Такого месяца нет") 
# elif month<=12 and month == 12 or month == 1 or month == 2: 
#     print("зима") 
# elif month<=12 and month == 3 or month == 4 or month == 5: 
#     print("весна") 
# elif month<=12 and month == 6 or month == 7 or month == 8: 
#     print("лето") 
# elif month<=12 and month == 9 or month == 10 or month == 11: 
#     print("осень")

"_____________________________________________________________"

# user_list = input('Введите строку: ')
# if user_list.isdigit():
#     print('is digit')
# elif user_list.isalpha():
#     print('is alpha')
# else:
#     print('is ASCII')

"___________________________________________________________________"

# a = int(input()) 
# b = int(input()) 
# c = int(input()) 
# if a + b > c and a + c > b and b + c > a: 
#     print("yes") 
# else: 
#     print("no")

"___________________________________________________________________________"

# a,b,c=int(input()), int(input()), int(input()) 
# a1=min(a,b,c) 
# b1=max(a,b,c) 
# c1=sum([a,b,c])-a1-b1 
# if b1>=a1+c1: 
#     print('impossible') 
# elif b1**2==a1**2+c1**2: 
#     print('rectangular') 
# elif b1**2<a1**2+c1**2: 
#     print('acute') 
# elif b1**2>a1**2+c1**2: 
#     print('obtuse')

"_____________________________________________________________________________"

# n = int(input("Enter number below 100: ")) 
# print('На лугу пасется ',end='' ) 
# if (n > 100): 
#     print("Incorrect number") 
# elif((n > 10 and n < 20) or (n % 10 >= 5) or (n % 10 == 0)): 
#     print(n,"коров") 
# elif(n % 10 == 1): 
#     print(n, "корова") 
# elif(n%10 in range(2, 5)): 
#     print(n, "коровы")

"_________________________________________________________________________________"

# x1=int(input()) 
# y1=int(input()) 
# x2=int(input()) 
# y2=int(input()) 
# if x1==x2 or y1==y2: 
#      print('YES') 
# else: 
#      print('NO')

"______________________________________________________________________"

# x1=int(input()) 
# y1=int(input()) 
# x2=int(input()) 
# y2=int(input())
# if x2-x1 == y2-y1: 
#     print('YES') 
# else: 
#     print('NO')

"_____________________________________________________________________________"

# num = chr(int(input())) 
# if num.isalpha(): 
#      print(f'Это буква "{num}"') 
# else: 
#      print(f'Это не буква, а символ "{num}"')

"________________________________________________________________________"


list_ = [
10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
a = []
b = {}
for i in list_:
    if i in b:
        a.append(i)
    else:
        b[i] = 1

print(b)
