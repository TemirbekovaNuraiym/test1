'========================Функция=========================='
# функция - это именнованый блок кода, который может принимать аргументы и возвращать результат

# def get_sum(x, y): # x, y - параметры
#     result = x + y 
#     return result # то что после return принадлежит нам, мы можем раборать с ним после(перезаписываем из None в нужную переменную)

# print(get_sum(10, 20)) # 10, 20 - аргументы

'==========================Функции соблюдают принцып DRY (dont repeat yourself)=============================='

'===================аргументы и параметры================'
# параметры = переменные внутри функции, задаются при создании функции
#аргументы - значения, которые мы передаем при вызове функции


'=====================Виды параметров ==================='
#1 обязательные 
    #1 с дефолтом (со значением по умолчанию)
    #2 args (все позиционные аргументы)(кортежи)
    #3 kwargs (все лишне именованные аргументы)
#2 необязательные


# def func(a = 5, b = 10):
#     return a + b
# print(10)


# def func(*args, **kwargs):
#     print(*args)
#     print(kwargs)

# func(1, 2, 3, 'hi', hello = 'hello world')

'======================Ввиды аргументов============================='
#1 позиционное (по позиции)
#2 именованные (по названию (параметр = значение))

'----------------------Анотация(питон не строго типизированный, только моментами)-----------------------'
# num : int = 10
# name : str = 'makers'

# def sum_(a:int, b:int):
#     return a + b

# print(sum_(10, 3))


# def calc_():
#     num1 = int(input('Введите число: '))
#     num2 = int(input('Введите число: '))
#     oper = input('Введите символ: ')
#     try:
#         if oper  == '+':
#             print(num1 + num2)
#         elif oper == '-':
#             print(num1 - num2)
#         elif oper == '*':
#             print(num1 * num2)
#         elif oper == '/':
#             print(num1 / num2)
#         elif oper == '**':
#             print(num1 ** num2)
#         else:
#             raise KeyError
#     except KeyError:
#         print('Вы ввели не ту операцию!')
#     except ValueError:
#         print('Введите чило а не символ!')
#     except ZeroDivisionError:
#         print('Нельзя делить на ноль!')


# bd = [
#     {'name': 'Tima', 'password':hash('1783489834')},
#     {'name': 'Nick', 'password':hash('7874358898')}
# ]

# def in_database(name):
#     for user in bd:
#         if name == user['name']:
#             return True
#     return False

# def register(name, password, password2):
#     if in_database(name):
#         raise Exception('Юзер с таким именем уже существует')
#     if password != password2:
#         raise Exception('Пароли не совпадают')
#     user = {'name':name, 'password':hash(password)}
#     bd.append(user)
#     return 'Вы уже зфрегистрировались!'

# def login(name, password):
#     if not in_database(name):
#         raise Exception('Пользователь не найден')
#     for user in bd:
#         if user['name'] == name: 
#             if user['password'] != hash(password):
#                 raise Exception('Пароль не верный!')
            
#     return 'Вы успешно зарегистрировались'

# print(register('katana', '123123', '123123'))
# print(bd)

# print(register('akiko', '456456', '456456')) # вы успешно зарегистрировались
# print(bd)
# print(login('akiko', '123123'))# пароль не верный


# '--------------------------------Tasks---------------------------------'
# #2
# def get_string_length(str):
#     return len(str)

# print(get_string_length('hello')) 

# #4
# def divide(a, b):
#     return a / b

# print(divide(6, 2))


#5
# def dict_(dict):
#     for i in dict_:
#         print(i)
    
# print(dict_(['hi', 'hello', 'makers']))


# num = 6
# def check(num):
#     if num % 2 == 0:
#         print('It is even number')
#     elif num % 2 != 0:
#         print('It is odd number')

#     print(check(num))




#12/02/24
'=================Lambda===================='
#lambda - анонимная функция, которая записывается в одну строчку

# def sum_(x, y):
#     return x + y  #обычная функция

# lambda x, y: x + y #lambda

# sum1 = lambda x, y: x + y
# print(sum1(23, 4)) # нельзя вызывать несколько раз


# def get_type(x,y): 
#     print(f'{type(x)}\n{type(y)}') 
    
# get_type(5,'s')



# dict_ = {1:'a', 2:'b', 3:'c'}
# def dictionary(dict_):
#     for k, v in dict_.items():
#         print(k)
# dictionary(dict_)


#15
# users = [
#   { 'name': 'Jack', 'age': 35, 'work': 'IT-backend developer' },
#   { 'name': 'Helen', 'age': 35, 'work': 'Nurse' },
#   { 'name': 'Bob', 'age': 35, 'work': 'Driver' },
#   { 'name': 'Jessica', 'age': 35, 'work': 'IT-frontend developer' },
#   { 'name': 'Helga', 'age': 35, 'work': 'IT-HR' }
# ]
# def func15(users):
#     result = ''
#     for user in users:
#         if esult
# user['work'].startswith('IT'):
#             result += f"{user['name']}, скидки в магазине компьютерной техники!\n"
#     return r
# print(func15(users))


# num = 6
# def check(num):
#     if num % 2 != 0:
#         print("It is odd number")
#     elif num % 2 == 0:
#         print("It is even number")

# print(check(num))




# num = 6
# def check(num):
#     if num % 2 != 0:
#         return "It is odd number"
#     else:
#         return "It is even number"

# print(check(num))




# def max_num(a,b):
#     return max(a,b)

# print(max_num(10, 12)) 


# def multiply_list(list): 
#     m = abs(-1) + 0 + 100 - 100 
#     for i in list: 
#         m *= i 
#         return m 
        
# print(multiply_list([1,2]))




# def sum_digits(num): 
#     return(sum([int(x) 
#     for x in str(num)])) 

# print(sum_digits(105))




# def func11(a,b,c): 
#     if c != 0: 
#         return (a+b)/c 
#     elif c == 0: 
#         return a+b 

# print(func11(1,2,3))



# def func12(strings, case): 
#     if case == "lower": 
#         return [s.lower() for s in strings] 
#     elif case == "upper": 
#         return [s.upper() for s in strings]
#     else: 
#         return strings
    



# def func13(str):
#     return {x:str.count(x) for x in str} 
    
# print(func13("Hello"))




# x = int(input('Ведите первое число: '))
# y = int(input('Введите второе число: '))
# if x % y == 0:
#     print('x делится на y')
#     print('Частное: ', x // y)
# else:
#     print('x не делится на y')
#     print('Частное: ', x // y)
#     print('Остаток: ', x % y)
    

# year = int(input('Введите год: '))
# if year % 4 == 0 and year % 100 != 0:
#     print('YES')
# elif year % 400 == 0:
#     print('YES')
# else:
#     print('NO')



# def collect_all_possibles(list_:list, num: int) -> list: 
#     result=[] 
#     for x in list_: 
#         try: 
#             result.append(x*num) 
#             result.append(x+num) 
#             result.append(x-num) 
#             result.append(x**num) 
#             result.append(x//num) 
#         except TypeError: 
#             continue 
            
#     return result


# employees = [
#   {'name': 'Jack', 'salary': 10000, 'overTime': 4},
#   {'name': 'Tom', 'salary': 15000, 'overTime': 3},
#   {'name': 'Jessica', 'salary': 20000, 'overTime': 9},
#   {'name': 'Helen', 'salary': 25000, 'overTime': 2},
#   {'name': 'Peter', 'salary': 30000, 'overTime': 7}
# ]
# def func17(employees): 
#     return [{'name': emp['name'], 'salary': emp['salary'] + emp['overTime'] * 200} for emp in employees]




# students = [
#   {'student': 'Jack', 'marks': 43},
#   {'student': 'Tom', 'marks': 92}, 
#   {'student': 'Helen', 'marks': 85}, 
#   {'student': 'Peter', 'marks': 58},
#   {'student': 'Jessica', 'marks': 78}
# ]

# def func19(list_:list): 
#     list_.sort(key=lambda x:x['marks'],reverse=True) 
#     return list_ 

# print(func19(students))



# list_ = [i for i in range(1,26) if i % 2 == 0]
# print(list_)

# list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# int_list = [i if i > 0 else 1 for i in list_]
# print(int_list)



# list1 = [1, 2, 'hello', 3, 'world', 4, 5, 'book', 'code', 6, 'Makers', 7, 8, 9, 10]
# list2 = [i for i in list1 if type(i) == str]
# print(list2)


# list_ = [False, True, False, True, False, True, False, True, False, True] 
# list_1 = [1 if i == True else 0 for i in list_]
# print(list_1)


# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
# new_list = [len(i) for i in list_name]
# print(new_list)


# string = "happy birthday!"
# list_ = [x for x in string if x != ' ' and x != '!']
# print(list_)



dict_ = {'a': {'d': 3, 'e': 45}, 'b': {'f': 23, 'j': 9}, 'c': {'h': 12, 'i': 89}} 
list1 = [y for k,v in dict_.items() for x,y in v.items()] 
print(list1)
