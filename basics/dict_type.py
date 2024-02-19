'============================Словари==============================='
# dict - изменяемый, итрируемый , неупорядочный, неиндексируемый тип данных для хранения данных, для хранения данных в парах (ключ значение)

user = {'name':'sultan', 'age': 20, 'nick': 'katana'}

# print(user['age']) # 20
# print(user['nick']) # 
# print(user['name']) #

#изменяемые типы данных недьзя использовать как клюлч, уникальный(названия ключей не могут повторяться)
# значения - могыт быть любые: изменяемые и не изменяемые типы данных(могут повторяться)
# {ключ: значение, ключ: значение........}

'============================Создание======================================'

# dict1 = {'a': 1, 'b': 5}
# dict2 = dict([('a', 1), ('b', 2)])
# dict3 = dict(['a1','b2'])
# dict4 = {}
# dict4 ['name'] = 'tima'
# dict4 ['nick'] = 'Nick'
# dict4 ['age'] = 23

'=================================Методы словорей==================================='
# get - метод, который возвращает значение по ключу,если нет такого ключа нет то возвращает дефолтное значение, чаще всего None
# user = {
#     'name':'Nick',
#     'age': 23,
#     'tel_number': '+8847598399'
# }
# print(user['kjgkfk']) # KeyError
# print(user.get('nickname', 'no this key'))
# print(user.get('name')) # Nick
# print(user.get('id')) # None

#pop - удаляет пару по кдючу и возвращает значение
# dict_ = {'a': 1, 'b':2, 'c': 3}
# popped_values = dict_.pop('a')
# print(popped_values)
# print(dict_) #{'b':2, 'c':3}

#popitem - уладяет последнюю пару и возвращает ее

# dict_ = {'a': 1, 'b':2, 'c': 3}
# popped_values = dict_.popitem
# print(popped_values)


# update - расширяет словарь парами из второго словаря 

# dict1 = {1:'a',2:'b'}
# dict2 = {3:'c',4:'d'}
# dict1.update(dict2)
# print(dict1)


# clear - очищает
# dict_ = {1:1, 2:2, 3:3}
# dict_.clear()
# print(dict_)

#fromkeys - для создания нового словаря используя список ключей

# dict_ = dict.fromkeys([1,2], text)
# print(dict_) # {1: None, 2: None} 

# setdefault

'==============================Циклы с dict========================='
# dict_ = {'a':1, 'b':2, 'c':3}
# for i in dict_.items():
#     print(i)


# dict_ = {'a':1, 'b':2, 'c':3}
# dict_2 = {}
# for k, v in dict_.items():
#     dict_2[v] = k
#     print(dict_2)

"______________________________________________"

#1
# a = {'x': 1, 'y': 2, 'z': 1}
# print(a.get(1))

#2
# a = {'a': 1, 'b': 2, 'c': 1}
# b = a.popitem()
# print(a)

#3
# a = {'a': 1, 'b': 2, 'c': 1}
# a.update({'f': 55})
# b = a.popitem()
# print(b)

#4
# a = {'a': 1, 'b': 2, 'c': 1}
# a.clear()
# print(a)

#5




#6
# a = {'a': 1, 'b': 2, 'c': 1}
# b = a.copy()
# print(b)

#7
# a = {'a': 1, 'b': 2, 'c': 1}
# for k in a: 
#      print(k)  


#8
# a = {'a': 1, 'b': 2, 'c': 1}
# b = a.items()
# print(a.get('a'))
# print(a.get('b'))
# print(a.get('c'))



# a = {'a': 1, 'b': 2, 'c': 1}
# for k, v in a.items():
#     print(v)


#9
# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6} 
# b = {} 
# for key, value in a.items(): 
#     if value % 2 == 0: 
#         b[key] = 2 
#     else: b[key] = value 
# print(b)


#10
# a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# b = a.pop('a')
# print(b)


#11
# a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25} 
# b = {k: v / 5 for k, v in a.items()} 
# print(b)


#12
# a = {'apple': 2, 'orange': 5, 'banana': 10} 
# for k, v in a.items():
#     if v % 2 == 0:
#         b = a.pop('apple')
#     print(a)

#13
# a = {'apple': 2, 'orange': 5, 'banana': 10} 
# b = {v: k for k, v in a.items()}
# print(b)


#14




#15
# a1 = {'a': 1, 'b': 2}
# print(a1)

# a2 = dict([('a', 1), ('b', 2)])
# print(a2)

# a3 = {}
# a3 ['name'] = 'tima'
# a3 ['nick'] = 'Nick'
# a3 ['age'] = 23
# print(a3)


#16
# dict_ = {'x': 1, 'y': 2, 'z': 1}
# print(dict_.get('x'))

#17
# dict_ = {'a': 1, 'b': 2, 'c': 1}
# del dict_['b']
# print(dict_)


#18
# dict_ = {'a': 1, 'b': 2, 'c': 1}
# for k, v in dict_.items():
#     print(dict_)

#19
# dict_ = {'a': 32, 'b': 56, 'c': 37, 'd': 21}
# dict_1 = max(dict_.values())
# print(dict_1)

20
dict_ = {'a': 32, 'b': 56, 'c': 37, 'd': 21}
dict_1 = min(dict_.values())
print(dict_1)

21 (спросить)
dict1 = {'a': 3, 'b': 4, 'c': 9, 'd': 5, 'e': 6} 
dict2 = {}
dict3 = 1
for key in dict1:
    if dict1[key] % 2 != 0:
        dict1[key] = dict3
    

print(dict1)


22
dict_ = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
b = dict_.pop('b')
c = dict_.pop('c')
d = dict_.pop('e')
print(b)
print(c)
print(d)

23
dict1 = {25: 'apple', 26: 'orange', 27: 'banana'} 
dict2 = {}
for k, v in dict1.items:
    if v * 3:
        dict1 = dict2
        print(dict2)

