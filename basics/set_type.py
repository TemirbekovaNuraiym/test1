'=============================Set============================='
# множества - это изменыяемый, неупорядеченный, итерируемфй, неиндексируемый тип данных, предназначеннный для хранения уникальных значений.
# множества могут хранить в себе только неизменяемые типы данных, если же в set использовать tuple то внутри tuple не должны быть изменяемого типа данных

set1 = {1, 2, 5, 9, 3, 'hello', None}
print(set1)

set2 = {2,4,5, }

'========================FIFO / LIFO========================'
#FIFO - first in first out
#LIFO - last in first out

'===============================Методы Set==============================='
print(dir(set))

#pop - удаляет случайный эллемент из set
# set1 = {2, 4, 6}
# popped = set1.pop()
# print(popped)
# print(set1) 


# #add - добавляет элемент в set
# set2 = {1, 2, 3}
# set2.add(4)
# print(set2)

# #remove - удаляет элемент по значению
# set3 = {1, 2, 3}
# set3.remove(1)
# print(set3)

# # discard - метод удаления который не выдает ошибку
# a = {1, 2, 3} 
# a.discard(4) 
# print(a)


# #9
# a = {2, 4, 6, 50, -45, -6} 
# b = {4, 3, 5, -5, -6}
# print(a - b)

# #10
# a = {2, 4, 6, 50, -45, -6} 
# b = {4, 3, 5, -5, -6}
# c = a.union(b)
# print(c)


# #11
# a = {1, 2, 3, 4, 5} 
# b = {2,3,4}
# if a.issubset(b):
#     print('Подмножество!')

#14
# tilek = {'Dodo', 'imperiaPizza', 'FreshBox'}
# timur = {'OchakKebab', 'FreshBox'}
# alexander = {'FreshBox', 'KFC'}
# elina = {'Dodo','ImperiaPizza','FreshBox','OchakKebab','KFC'}

# if tilek.intersection(elina) and timur.intersection(elina) and alexander.intersection(elina): 
#     print(elina.intersection(timur,tilek,alexander)) 
# else: 
#     print(elina.intersection(timur,tilek,alexander))


#15
# ingredients = {"cыр чеддар","грибы", "соус","шпинат"} 
# ingredients.add('помидор')
# ingredients.discard('колбаса')
# ingredients.remove('шпинат')
# ingredients.add('базилик')
# ingredients.discard('сыр чеддар')
# ingredients.add('сыр моцарелла')
# print(ingredients)


#13
# robert = {5, 7, 11, 10, 28} 
# kail = {1, 5, 14, 8, 22} 
# merri = {19, 20, 3, 11, 10} 
# if robert.intersection(kail) and robert.intersection(merri): 
#     print('kail merri') 
# elif robert.intersection(kail): 
#     print('kail') 
# elif robert.intersection(merri): 
#     print('merri') 
# else: 
#     print('no one')


#16
# a = [set(), set(), set()]
# inp1 = input()
# inp2 = int(input())
# d = 'default value'

# for i in a:
#     if a.index(i) == inp2 - 1:
#         i.add(inp1)
#     else:
#         i.add(d)
# print(a)
