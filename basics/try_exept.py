'=========================Exeptions=========================='
# исключения это обьекты, которые перерабатывают работу кода, если не были обработанны

'SyntaxError'
#это исключение кодгда в коде допущен синтаксическая ошибка

'NameError'
# это исключение которое выходит, когда мы обращаемся к несуществующей переменной

'IndexError'
#исключение, которое выходит при обращении к несуществующему индексу
'''
list_ = [1,2,3,4]
list_[1000000]
'''

'KeyError'
# исключение которое выходит когда обращяемся к несуществующему ключу
'''
dict_ = []'a': 1, 'b': 2]
print(dict_['c'])
'''

'ValueError'
#1 когда мы передаем в функцию некоректный для нее тип данных
#2 когда мы распаковываем итерируемый обьект на несколько переменных и кол-во переменных не совпадает с кол-во значений


'TypeError'
#1 когда мы пытаемся использовать методы не свойственные какому то типу данных
#2 когда мы пытаемся передать в функцию больше или меньше аргументов чем принимает функция
'''
for i in1:
    '''

'''
{[1,2,3]: 'a}
    '''

'ZeroDivisionError'
#выходит когда делим что то на 0
'''
44 / // % 0 
'''

'ArithmeticError'
#выходит когда мы обращяемся к несуществуему аттрибуту или методу обьект или тип данных

'IndentationError'
# выходит когда мы не правильно используем отступы

'''
        a = 5
'''

Exception
# исключение которое создали что бы его вызывать(для проверки любых ошибок)


'====================================Вызов исключений========================================'

#raise NameError('Я вызвал')


'=========================Try except========================='
# конструкция котороая помогает обрабатывать исключения

# try: # конструкция try используют если разработчик не уверен или знает что в коде есть ошибка и хочет обработать в except
#     num = int(input('Введите число: '))
# except ValueError: # конструкция except нужна для обработки исключения 
#     print('Введите число а не символ: ')
# else: # срабатывает когда не вышло ошибки исключения (когда не сработал except)
#     print('Вы ввели число {num}')
# finally: # работает в любом случае
#     print('до свидания')


# try:
#     print(number)
# except (NameError, ValueError, TypeError):
#     print('Нет такой переменной, Проверил вот такие исключения:NameError, ValueError, TypeError')
# except ZeroDivisionError:
#     print('Обработанно')


# try:
#     raise Exception
# except: # отлавливается любая ошибка
#     print('отловленна любая ошибка')

# try:
#     raise NameError
# except Exception: # отловливаются все ошибки
#    print('отловленна любая ошибка') 


#2
# b = 10
# c = 11

# try:
#     print(a)
# except NameError:
#     print('ошибка обработанна')
# except:
#     print('Такой переменной не существует!')
 

# try:
    # Получаем числа от пользователя
#     num1 = float(input("Введите первое число: "))
#     num2 = float(input("Введите второе число: "))
    
#     # Проверка деления на 0
#     if num2 == 0:
#         raise ZeroDivisionError("Деление на ноль недопустимо")

#     # Выполняем деление и выводим результат
#     result = num1 / num2
#     print(f"Результат деления {num1} на {num2} равен: {result}")

# except (ValueError, ZeroDivisionError):
#     print(f"Ошибка:")
# except Exception:
#     print(f"Произошла ошибка:")


""" #синтаксис try ecxcept
try:
    print('some code 1')
except:
    print('some code 2')
else:
    print('some code 3')
finally:
    print('some code 4')
"""

# try:
#     num1 = int(input('Введите число:'))
# except:
#     print('Введите число:')


# try:
#     num1 = int(input('Введите первое число: '))
#     num2 = int(input('Введите второе число: '))
#     res = num1 / num2
# except ZeroDivisionError:
#     print('На ноль делить нельзя!')
# except ValueError:
#     print('Вы вели не число!')
# else:
#     print(res)
# finally:
#     print('Программа завершенна')


#4
# try:
#     num1 = int(input('Введите первое число: '))
#     num2 = int(input('Введите второе число: '))
#     res = num1 + num2
# except ValueError:
#     print('Введите число!')
# else:
#     print(res)
# finally:
#     print('Программа завершенна')


#5
# try:
#     dict_ = {'key1': 'value1', 'key2': 'value2'} 
#     dict_.fromkeys('key1')
# except KeyError:
#     print('Нет такого ключа!')


#3
# try:
#     num1 = int(input('Введите первое число: '))
#     num2 = int(input('Введите второе число: '))
#     res = num1 / num2
# except ZeroDivisionError:
#     print('На ноль делить нельзя')
# else:
#     print(res)

#7
# try:
#     age = int(input())
#     if age < 18:
#         raise ValueError("Доступ запрещён")
# except ValueError:
#     print('Введён некорректный возраст')
# else:
#     print('Спасибо')
# finally:
#     print('До свидания!')

#8
# try:
#     num1 = int(input())
#     num2 = int(input())
#     res = num1 / num2
# except (ValueError, ZeroDivisionError):
#     print('Произошла ошибка!')


#9
# cash = int(input())
# if cash < 0:
#     raise ValueError('Сумма не может быть отрицательной!')
# else:
#     print(cash)

#10
# try:
#     list_ = [1, 2, 3]
#     list_.get(1)
# except AttributeError:
#     print('Ошибка')

#11
# string = str()
# num = int()

# try:
#     res = string + num    
# except (ValueError, TypeError):
#     print('Unsupported option')

#13
# list_ = [1, 2, 3, 4]
# try:
#     for i in range(0, len(list_) + 1):
#         print(list_[i])
# except IndexError:
#     print('ошибка')

#15
# warehouse = [['B', 's'], ['e', 'u'], ['O', 'o', 'x'], ['K', 'T'], [], [], [], [], [], []] 
# for i in warehouse: 
#     if len(warehouse)>10 or len(i)>3: 
#         raise ValueError()



#14
# try:
#     password = input()
#     if len(password) < 6:
#         raise ValueError
#     else:
#         print(password)


#16
# def to_fahrenheit(k:int) -> float: 
#     assert k >= 0,'Холоднее абсолютного нуля!' 
#     res = (k-273.15)*9/5+32 
#     return res 
#     print(to_fahrenheit(3))


#17
# def filter_comment(comment: str, banlist=[]) -> None
#     if filter_comment == 'hello' or 'hi':
#         raise ValueError("Ваш комментарий отправлен на перепроверку, так как, возможно, содержит неблагоприятный контекст")
#     elif filter_comment == ',' or '!':
#         remove.filter_comment


#12
# try:
#     list_.extend(range(0,10))
# except NameError:
#     print('no')
    

#14

# password = 'shrt'

# if len(password) < 6:
#     raise ValueError('пароль не должен быть менее 6 символов')


#17

# from lamabimgo import
# raise SyntaxError('Такого модуля нет')

#21
# try:
#     inp1 = input()
#     inp2 = input()
#     if inp1.isdigit() and inp2.isdigit():
#         a = int(inp1)
#         b = int(inp2)
#         print(a+b)
#     else:
#         print(inp1+inp2)
# except ValueError:
#     print('no')

#22
# try: 
#     inp1 = input() 
#     res = inp1.split(' ') 
#     list_ = [int(x) for x in res] 
# except ValueError: 
#     raise ValueError('Данный элемент не является числом!')


#17
# try:
#     import lamabimgo
# except ModuleNotFoundError: 
#     print('Такого модуля нет')


