'===========================Области видимости=============================='
#LEGB - local enclosed global build - in

'====================Build-in====================='
#встроенное пространство имен (list, print, dict, len)

'=====================Global===================='
#все переменные, которые мы создали внутри файла
#чтобы посмотреть все глобальные переменные, можно использовать функцию globals
a = 10
b = 'hello'
#print(globals())  

'==================Enclosed=================='
#замкнутое пространство имен - этоо локальное пространство, у которого есть внутреннее локальное пространство 

# var = 'global' #хранится в глобальном пространстве

# def func():
#     var = 'enclosed' #замкнутое пространство
#     def inner_func():
#         var = 'local' #локальное ппространство
#         print(var) #local
#     print(var) # enclosed
#     inner_func()
# print(var) #global 
# func()  

'================Local====================='
# локальное пространство имен - это пространство, которое находится внутри функции
# a = 10
# def func(a, b):
#     res = a + b
#     print(res)
#     print(locals())
#     print(globals)

# func(10, 5)



# global - для изменения переменной глобального пространства в локальной 
# a = 10
# def func():
#     global a
#     a = 20
#     print(a)
# print(a)
# func()
# print(a)



# count = 0 
# def count_():
#     global count
#     count += 1
#     print(count)

#     while True:
#         count()
    

# x = 'Я глобальная переменная!'
# print(x)
# def my_func():
#     global x
#     x = 'Я могу изменяться'

#     print(x)
# my_func()




# num = 3
# def mul():
#     global num
#     num = num ** 2
    
# mul()
# mul()
# mul()
# print(num) 


    

# balance = 0 

# def get_salary(amount): 
#     global balance 
#     balance += amount 

# def pay_bills(amount, log_name): 
#     global balance 
#     balance -= amount 
#     print(f'Вы заплатили {amount} сом за {log_name}') 

# def get_balance(): 
#     print(f'У вас на счету {balance} сом') 
        
# get_salary(1000) 
# get_balance() 
# pay_bills(400, 'кабельное тв') 
# get_balance()


# def pow(x,y,z):
#     print(x**y % z)

# def hello(name):
#     print(locals('makers'))
    
#     hello()
#     print(hello()

name = 'Sandy'
def func_one():
    name = 'Andy'
    def func_two():
        name = 'Mandy'
        print(name)
        print(locals())
    func_two()
func_one()