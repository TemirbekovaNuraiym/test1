'====================Функция высшего порядка====================='
# функция высшего порядка - это функция котороая принимает в аргумент другую функыию, создает внутри себю друную функцию и возвращает функцию
# def func1():
#     return 'hi'

# def func2(func_):
#     print(func_()) #функция высшего порядка

# func2(func1)


'===============Декораторы==================='
# декораторы - это функции высшего порядка, которая нужна для расширения функционала другой функции не изменяя ее (функция оберток)

# def decorator_glushitel(func):
#     def wrapper(*args, **kwargs):
#         text = func(*args, **kwargs)
#         res = 'тихо ' + text
#         print(res)
#     return wrapper

# def gun():
#     return 'стрелять'

# wrapper = decorator_glushitel(gun)
# wrapper() # способ вызвать декоратор в ручную

# '--------------------------------------------'

# def decorator_glushitel(func):
#     def wrapper(*args, **kwargs):
#         text = func(*args, **kwargs)
#         res = 'тихо ' + text
#         print(res)
#     return wrapper

# @decorator_glushitel
# def gun():
#     return 'стрелять'

# gun() # способ вызова функции при помощьи синтаксического сахара 



'------------------------------------------------'

from datetime import datetime

# def decorator(func):
#     def wrapper():
#         print('start:')







'-------------------------------------------------------'

# def func_starta_time(func):
#     def wrapper(*args, **kwargs):
#         print('strart:', datetime.now())
#         func(*args, **kwargs)
#     return wrapper

# @func_starta_time
# def sum_(a, b):
#     print(a + b)

# sum_(20, 10)

'-----------------------------------------------------------'

def decorator(num):
    def inner_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num):
                func(*args, **kwargs)
        return wrapper
    return inner_decorator

@decorator(10)
def hello():
    print('hello world')

hello()


'------------------------tasks------------------------------'
#1

# def call_function(func):
#     def wrapper(*args, **kwargs):
#         print('Вызываю функцию', func.__name__)
#         func()
#         print('Вызов функции', func.__name__, 'прошел успешно')
#     return wrapper


# @call_function
# def first():
#     print("hello world")
#     return "hello world"
# first()

#2
# from datetime import datetime

# def func_start_time(func):
#     def wrapper(*args, **kwargs):
#         print('Функция запущена ', datetime.now())
#         func(*args, **kwargs)
#     return wrapper
    
# @func_start_time
# def func():
#     print('Hello world')
# func()


# def make_bold(func):
#     def wrapper(*args, **kwargs):
#         return f"<b>{func()}</b>"
        
#     return wrapper

# def make_italic(func):
#     def wrapper(*args, **kwargs):
#         return f"<i>{func()}</i>"
        
#     return wrapper


# def make_underline(func):
#     def wrapper(*args, **kwargs):
#         return f"<u>{func()}</u>"
        
#     return wrapper




# @make_bold
# @make_italic
# @make_underline
# def hello():
#     return 'Hello world'
 
# print(hello())
