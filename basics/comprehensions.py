'============================comprehension=================================='
#генератор - с помощюд которого мы можем создавать последовательности используя цикл for в одну строку

# элемент for элемент in последовательность  
#элемент for элемент in последовательность if фильтр
# элемент if условие1 else елемент2 for елемент in последовательность

# compr_ = [i if i % 2 == 0 else 'elem' for i in range(6)]
# print(compr_)

'-------------------------------------------------------'# (одно и тоже)

# compr1 = []
# for i in range(6):
#     if i % 2 == 0:
#         compr1.append(i)
#     else:
#         compr1.append('elem')
#         print(compr1)



# list_ = [ 12, None, 'hi', 123, 1, 6, 2, True, 0, False]
# new_list = [i for i in list_ if bool(i)]
# print(new_list)

'---------------------------------------------------------'

# new_list2 = [i if bool(i) else 0 for i in list_]
# print(new_list2)

# new_list3 = []
# for i in list_:
#     if bool(i):
#         new_list3.append(i)
#     else:
#         print(new_list3)

'-----------------------------------------------------------'

# list_ = [12, 3, 0, 34, 9, 7]
# new_list = ['четное' if i % 2 == 0 else 'нечетное' for i in list_]
# print(new_list)

'-------------------------------------------------------------------------------'


'================================Виды comprehension==================================='
# list comprehension []
# dict comprehension {:}
# set comprehension {}

# comprehension генератор ()

'DICT comprehension'
# list_ = ['Bootcamp', 'Makers', 'coding', 'hello']
# dict_ = {i: i.len() for i in list_}
# print(dict_)

# dict_ = {'a':1, 'b':2, 'c':3}
# new_dict = {v:k for k,v in dict_.items()}
# print(new_dict)


'SET comprehension'
# set_ = {i for i in range(11) if i % 2 == 0}
# print(set_)

# '=================================Вложенные===================================='

# dict_ = {}
# for i in range(1, 6):
#     key = i
#     values = [j for j in range(1, i + 1)]
#     dict_[key] = values
#     print(dict_)

# dict_ = {i: [j for j in range(1, i + 1)]for i in range(1,6)}
# print(dict_)



'============================Таски====================================='
#1
# list_ = [i for i in range(1, 101)]
# print(list_)

# #2
# list_ = [i for i in range(1, 50, 2)]
# print(list_)

#3
# list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# int_list = [i for i in list_ if i % 2 == 0]

# print(int_list)

#4
# list_ = [i ** 2 for i in range(1, 26)]
# print(list_)

#5
# str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# int_list = [i for i in str_list if type(i) == int]
# print(int_list)

#6
# list_ = [i if i % 2 == 0 else i ** 2 for i in range(1, 11)]
# print(list_)

#7
# list_ = [i if i % 2 == 0 'True' else 'False' for i in range(1, 10)]
# print(list_)

# list_ = [num * 2 for num in range(1,21)]
# print(list_)

# user_list = ['adde', 'nika', 'ali']
# inv = ['периглашение для: ' + name for name in user_list]
# print(inv)

# list1 = [10, 5, -6, -8, -12, 20, 3, 14, 4]
# list2 = [num for num in list1 if num % 2 == 0 and num > 0]
# print(list2)


# string = ['213', '3435', 'hello', 'hi21']
# string1 = [year for year in string if year.isdigit()]
# print(string1)


# list_1 = ['jon', 'jksl', 'jkfklj', 'jfjs']
# list_1 = [len(name) for name in list_1]
# print(list_1)

# int_list = ['24234', '46565', '8787', '12']
# int_list = [len(num) for num in int_list]
# print(int_list)

# list_ = [5, 6, 7, -7, -4, 2, 12]
# list_ = [i if i < 0 else i ** 2 for i in list_]
# print(list_)




# list_ = [i ** 2 if i % 2 == 0 else i for i in range(1,11)]
# print(list_)



# list_ = [False if i % 2 != 0 else True for i in range(1,10)]
# print(list_)


# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ]

# new_list = ['shorter' if len(x) <= 4 else 'longer' for x in list_name] 
# print(new_list)


# dict_ = {i: i ** 2 for i in range(1,11)}
# print(dict_)


# n = int(input()) 
# dict_ = {x : x**2 for x in range (1, 501) if x % n == 0} 
# print(dict_)
 


# a = {'a': 1, 'b': 5, 'c': 4, 'd': 3} 
# dict_ = {k:list(range(v+1))[1:] for k,v in a.items()} 
# print(dict_)



# dict_ = {1:'a', 2:'b', 3:'c', 4:'d'}
# dict_ = {k: len(v) if k % 2 == 0 else len(v) ** 3 for k, v in dict_.items()}
# print(dict_)

# dict_ = {'first': 1, 'second': 2, 'third': 3} 
# a = {k: 'even' if v % 2 == 0 else 'odd' for k,v in dict_.items()}
# print(a)


# balance = 0
# amount = 2134
# def get_salary(amount):
#     print balance * amount


a = {s for s in [1, 2, 1, 0]}
print(a)