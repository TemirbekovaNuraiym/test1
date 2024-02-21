'===================Встроенные функции==================='
# map, filter, reduce, zip, enumerate

'ZIP'
#соеденяет несколько последовательностей (получаем генератор, в котором элементы - tuple) (zip object)

# list_1 = [1,2,3,4]
# list_2 = ['a', 'b', 'c']
# list_3 = [10.3, 43.9, 1.2, 0,3]
# zipped = zip(list_1, list_2, list_3)
# print(zipped) #<zip object at 0x7f263f6f80>
# print(list(zipped)) # [(1, 'a', 10.3), (2, 'b', 43.9), (3, 'c', 1.2)]
# print(tuple(zipped))
# print(dict(zipped)) # в словарях можно соеденять только два листа в zip() (первый лист ключи второе значения)

'ENUMERAT'
# нумерует последовательность (по дефолту с 0), (тоже возвращает генератор)
# enumerate = enumerate('hello world', 100) # можно после итерируемого обекта обозначить со скольки считать
# print(enumerate) #<enumirate object at 0x7f263f6f80>
# #print(list(enumerate)) #[(0, 'h), (1, 'e'), (2, 'l'), (3, 'l')..........] нумерует пока не закончится
# for elem in enumerate:
#     print(elem)


'MAP'
# прнинимает функцию и последовательность 
# записывает в новую последовательность результат функции, применив ее на каждый элемент последовательности <map object at 0x7f263f6f80>
# list_ = ['1jdj', '2', '3kf', '4']
# mapped = map(int, list_)
# print(list(mapped))

# mapped2 = map(str.isdigit, list_)
# print(list(mapped2))

# list_ = [21, 34, 6, 8, 9]
# def pow_(x):
#     return x ** 2
# print(list(map(pow_, list_)))
                  #одно и тоже
# print(list(map(lambda x:x**2, list_)))


# str_ = 'hello world'
# mapped = map(str.upper, str_)
# print(''.join(list(mapped)))

# print(''.join(list(map(str.upper,str_))))



'FILTER'
# возвращает генератор c элементами, прошедшими фильтрацию (какое то условие), принемает функцию и последовательность <filter object at 0x7f263f6f80>

# list_ = [12, 3, 4, -23, 0, -1, 4]
# filtered = filter(lambda x: x >= 0, list_)
# print(list(filtered))

'-------------------------------------------------------'

# users = [
#     {'name':'makers', 'age':21},
#     {'name':'anonym', 'age':12},
#     {'name':'sem', 'age':23}
# ]
# # filtered = filter(lambda x: x['age'] > 18, users)
# # print(list(filtered))

'-------------------------------------------------------'

# filtered = filter(lambda x: x['name'].startswith('a'), users)
# print(list(filtered))



'REDUCE'
# принемает функцию и последовательность, возвращает 1 элемент (передаваемая функция должна принимать 2 аргумента)
# импортируется из functools

# from functools import reduce

# list_ = [1, 23, 4, 1, 56, 10]
# res = (lambda x, y: x*y, list_)
# print(res)

# from functools import reduce
# users = [
#     {'name':'makers', 'age':21},
#     {'name':'anonym', 'age':12},
#     {'name':'sem', 'age':23}
# ]

# def func(x, y):
#     if x['age'] < y['age']:
#         return x
#     else:
#         return y

# print(reduce(func, users))


# from functools import reduce

# list_ = [12, 3, 4, -23, 0, -1, 4]
# res = reduce(lambda x, y: x if x < y else y, list_)
# print(res)




























'------------------------------Tasks--------------------------'
# from functools import reduce

# list_ = [1, 2, 3, 4]  
# result = reduce(lambda x, y: x + y, list_)
# print(result)


# list_ = [1, 5, -9, 6, -4] 
# result = map(lambda x: x > 3, list_)
# print(list(result))

# list_ = [1, 5, -9, 6, -4] 
# result = all(i > 3 for i in list_)
# print(result)

# # list_ = [5, 8, 4, 6, 7]
# # result = any(i < 0 for i in list_)
# # print(result)


# list_ = [1, 2, 3, 4]  
# result = list(map(lambda x:x ** 2, list_))
# print(result)


# list_ = [1, 2, 3, 4] 
# result = list(filter(lambda x: x % 2 == 0, list_))
# print(result)


# from functools import reduce
# list_ = [5, 6, 7, 8] 
# result = reduce(lambda x, y: x * y, list_)
# print(result)



# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ] 
# list2 = len(list(filter(lambda x: x % 2 == 0, list_)))
# list3 = len(list(filter(lambda x: x % 2 != 0, list_)))
# result = (f'even: {list2}, odd: {list3}')
# print(result)


# list_ = [-1, 2, 3, 5, -3, 7] 
# result = list(filter(lambda x: False if x < 0 else True, list_))

# print(result)




# list_ = [1, -2, 3, -4, 5, -6]
# result = list(filter([lambda i: False if i < 0 else True for i in list_]))
# print(result)


# list_ = ['inheritance', 'solid', 'polymorphism', 'dry', 'yagni',] 
# result = list(filter(lambda x: len(x) > 7, list_))
# print(result)


list_ = [-1, 2, 3, 5, -3, 7] 
result = list(map(False if i < 0 else True for i in list_))
print(result)