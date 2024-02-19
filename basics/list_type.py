'=============================Список(list)===================================='

#Список - изменяемый тип данных

# string = 'hello'
# res = list(string)
# print(string.split())
# print(res)


# list_ = []
# list_ = list()
# list_ = [2]*10
# print(list_)

'=========================================Методы списков=========================================='
#append - добавление элементы в конец
# list_=[]
# list_.append(True)
# list_.append('subwey serfers')
# list_.append(123)
# list_.append([1,2,3])
# # print(list_)

# #pop - удаляется элементы из списка по индексу и возвращает удаленный элемент, если не передать индекс в скобки, то удалит последний элемент
# list1 = ['asdf',5,5,5,True,5,5,5,None,5,5]
# re_elem = list1.pop(6)
# # print(re_elem)
# # print(list1)

# # remove - удаление элемента из списка по значению 
# list2 = [123,23,3426,7543, 'kutman', True, False]
# list2.remove(23)
# # print(list2)

# # count - метод, который считает количество элементов в списке
# list3=[1, 2, False, 3, 'Clown', 4, 5, 6, True, None,0,0,0,0,0]
# # print(list3.count(0))


# # index - возвращает индекс первого вхождения указанного элемента
# list3 = [12,3,3,3,'hi',None]
# index_=list3.index('hi')
# # print(index_)

# # insert - добавляет элемент в список по указанному индексу
# list4 = [123,234,1234,45,543,'dfg',True, False]
# list4.insert(2, 'makers')#2 это инедекс
# # print(list4)

# # extend - добавляет элементЫ списка в другой список
# list0 = [0,0,0]
# listSec = [1,2,3]
# list0.append(listSec)
# list0.extend(listSec)
# # print(list0)

# # reverse - расставляет элементы в обратоном порядке 
# list10 = [123,2134,435,[1233,'erwwer',True],4563,4152]
# # print(list10)
# list10.reverse()
# # print(list10)

# # sort - сортирует список состоящий из элементов одного типа данных
# list_sort = [2,3434,52,34223,1231,2,523]
# list_sort.sort()
# # print(list_sort)

# list_sort2 = ['hi', 'makers', 'asd', 'qwerty']
# list_sort2.sort(key = len,reverse=True)#['makers', 'qwerty', 'asd', 'hi']
# # print(list_sort2)

# # COPY AND DEEPCOPY what is that?
'=====================================================Tuple=================================='

# # Кортеж - это упорядочный, неизменяемый, итерируемый тип данных, литерлы это (,) (ТОЛЬКО ДВА МЕТОДА)

# tuple_ = (1, 2, 3, 4, 5,True, False, None)# Только два метода
# tuple_.count(1)
# tuple_.index(2)
# # print(tuple_.count(1))


# nums = [9, 5, 5, 7, 3.5, 'hello' False]

# nums[0] = 90




# print(nums)

# name_of_friends = ['hello', 'world', 'python', 'makers', 'bootcamp']

# i = 0 
# while i < len(name_of_friends):
    #print(name_of_friends)

# labels = ['audi', 'bmw']
# labels.insert(0, 'I like brand audi')
# labels.insert(1, 'I like brand bmw')

# numbers = list(range(15))
# print(numbers)

# numbers = list(range(1, 12))

# print(numbers)


'+++++++++++++++++++++++++++++++Списки и циклы(таски)+++++++++++++++++++++++++++++++++++++'

# nums = [1, 3, 4, 5, 7, 8, 9, 5]
# res = []
# for i in nums:
#     if i < 5:
#        res.append(i)
# print(res)

# ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg

# new_list = []
# list_ = [1, 2, 3, 4, 5]
# for i in list_:
#     if i % 2 == 0:
#         new_list.append('четное')
#     else:
#         new_list.append('нечетное')   
            
# print(new_list)

"-----------------------------------------------"

# list_ = []
# for i in range(0, 20):
#     list_.append(i)

# print(list_)

"----------------------------------------------"

# list_ = []
# for i in range(0, 101, 2):
#     list_.append(i)

# print(list_)

# list1 = [43, 2, 6,]
# list2 = [8, 12, 34]
# for i in list1 + list2:
#     print(i)


"_________________________________________________"

# n = input('Введите число: ')
# list_ = []

# i = 0
# while i < n:
#     list_.append(input('введите элемент #' 'i' ':'))
#     i += 1
# print(list_)

"________________________________________________"

# list_ = [5, 5, 7]
# if list_:
#     print('yes')
# else:
#     print('ERROR')

"____________________________________________"

# list_ = []
# for i in range(54, 9184):
#     if i % 5 == 0:
#         list_.append(i)
    
# print(list(list_))

"___________________________________________"

# list_ = [20, 10, 20, 1, 100] 
# list_.sort() 
# min_number = list_[0] 
# print(min_number)

"__________________________________________________"

# tuples = [(), ('ram','15','8'), (), ('laxman', 'sita')]
# tuples = [a for a in tuples if a]
# print(tuples)

"_______________________________________________________"


# a = []
# for i in range(5):
#     user_str = input('Введите строку: ')
#     name = user_str.split()
#     if name:
#         a.append(name)
#         a.sort()

#     print('Фио: ', a)


"__________________________________________________________"

#3
# name_of_list = ['Helloworld!']
# str_ = hello_world = name_of_list[0]
# index_middle_elem = len(str_) // 2
# if len(name_of_list[0]) % 2:
#     res = str_[index_middle_elem + 1:] + str_[:index_middle_elem + 1]
# else:
#     res = str_[index_middle_elem:] + str_[: index_middle_elem]
# new_list = list(res)
# print(new_list)
    
#7
# number = input()
# list_ = number.split(',')
# tuple_ = tuple(number.split(','))
# print(list_)
# print(tuple_)

#20
# list_ = [1, 'abcd', 3, '1', 4, 'xyz', 5, 'pqr', 7, 5, 12]
# res = 0 
# for i in list_:
#     if type(i) == int or i.isdigit():
#         res = res + int(i)
#     print(res)


# llist_ = ['world', 'hello'] 
# a = 'hello'
# b = 'world'
# new_list = a.append(b)
# print(new_list)


#35
# chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# merge_from = input()
# merge_to = input()
# from_to = "".join(chars[chars.index(merge_from):chars.index(merge_to)+1])
# result = []

# for char in chars[:chars.index(merge_from)]:
#     result.append(char)

# result.append(from_to)

# for char in chars[chars.index(merge_to)+1:]:
#     result.append(char)

# print(result)


#12
# list1 = [11, 23, 45, 7, 9] 
# list2 = [21, 4, 16, 8, 10] 

# list3 = list1 + list2
# print(sum(list3))


#18
# last_names = []
# last_name = input().split()[-1]
# last_names.append(last_name)
# last_name = input().split()[-1]
# last_names.append(last_name)
# last_name = input().split()[-1]
# last_names.append(last_name)
# last_name = input().split()[-1]
# last_names.append(last_name)
# last_name = input().split()[-1]
# last_names.append(last_name)
# print(sorted(last_names))

#19
# list_ = [8, 6, 8, 10, 8, 20, 10, 8, 8]

#1
# a = {'x': 1, 'y': 2, 'z': 1} 
# print(list(a.keys())[0])

#3
# a = {'a': 1, 'b': 2, 'c': 1}
# a1 = {'f': 55}
# a.update(a1)
# print(a)

#5
# a = {'a': 1, 'b': 2, 'c': 1}
# print(list(a.keys()))

#12
# a = {'apple': 2, 'orange': 5, 'banana': 10} 
# b = a.copy() 
# for key, value in b.items(): 
#     if value % 2 == 0: 
#         a.pop(key) 
        
# print(a)

#14
# a = {'a': 3, 'b': 2}
# print(sum(a.values()))

#18
# dict_ = {'a': 1, 'b': 2, 'c': 1}
# print(dict_.items())

#21
# dict1 = {'a': 3, 'b': 4, 'c': 9, 'd': 5, 'e': 6} 
# dict2 = {}
# for key, value in dict1.items():
#     if value % 2 != 0:
#         dict2[key] = 1
#     else:
#         dict2[key] = value
#         print(dict2)


#22
# dict_ = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3} 
# for k, v in list(dict_.items()): 
#     if v != None: 
#         dict_.pop(k) 
#         print(dict_)
       

#23
# dict1 = {25: 'apple', 26: 'orange', 27: 'banana'} 
# dict2 = {k ** 2:v for k, v in dict1.items()}
# print(dict2)

#24
# list_ = ['Bootcamp', 'Makers', 'coding', 'hello'] 
# dict_ = {} 
# for i in list_: 
#     dict_[i] = len(i) 
#     print(dict_)


#25
# dict_ = {'Bootcamp': 8, 'Makers': 6, 'coding': 6, 'hello': 5} 
# max_ = max(dict_.values()) 
# for k in dict_.keys(): 
#     if dict_[k] == max_: 
#         print(k)

#26
# dict1 = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
# dict2 = {k: v ** 3 for k, v in dict1.items()}
# print(dict2)

#27
# dict_ = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}} 
# dict1 = dict_.copy() 
# for k, v in dict1.items(): 
#     for value in v.values(): 
#         dict_[k]=value 
#         print(dict_)


#28
# dict1 = {'a': {'d': 1, 'e': 4}, 'b': {'f': 2, 'j': 4}, 'c': {'h': 3, 'i': 9}} 
# dict2 = {} 
# for k,v in list(dict1.items()): 
#     res = 1 
#     for j in v.values(): 
#         res = res * j 
#         dict2[k] = res 
#         print(dict2)


#29
# list_ = ['hello', 23, 56, 'world', 928, 'Makers', 456, 'word', 223, 89, 'bootcamp', 'coding'] 
# ls = [x for x in list_ if type(x)==int] 
# ls2 = [x for x in list_ if type(x)==str] 
# dict_ = dict(zip(ls2, ls)) 
# print(dict_)


#30
# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0} 
# sorted_dict = {k:item for item in sorted(dict_.values()) for k,v in dict_.items() if item == v} 
# print(sorted_dict)

#31
# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0} 
# sorted_dict = {k:item for item in sorted(dict_.values(), reverse = True) for k,v in dict_.items() if item == v} 
# print(sorted_dict)

#32
# dict_ = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# key = input()
# if key in dict_:
#     print('yes')
# else:
#     print('no')


#33
# dict1 = {1:10, 2:20}
# dict2 = {3:30, 4:40}
# dict3 = {5:50, 6:60}
# dict4 = {}
# dict4.update(dict1)
# dict4.update(dict2)
# dict4.update(dict3)
# print(dict4)


#34
# list1 = [1, 2, 3, 4, 5, 6, 7]
# list2 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
# dict_ = {}
# for i in range (len (list1)): 
#     dict_[list1[i]] = list2[i] 
#     print(dict_)

#36
# a = {'a': 10, 'b': 9, 'c': 3}
# result = 1 
# for key in a: 
#     result=result * a[key] 
#     print(result)

#37
# string = "pythonist" 
# dict_={} 
# for i in list(string): 
#     dict_.setdefault(i, list(string).count(i)) 
#     print(dict_)

#10
a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3} 
a = {key:value for (key, value) in a.items() if value}
print(a)


