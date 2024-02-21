#1
# def num(a, b):
#     return a + b
# print(num(19,6))

#3

a = [1, 2, 3, 4]
import functools
def func():
    s = (functools.reduce(lambda a, b : a * b, a)) 
    return s

print(func())



#6
# num = 3
# def mul():
#     global num
#     num = num ** 2
    
# mul()
# mul()
# mul()
# print(num) 


#8
# list_ = [1, 2, 3, 4, 5, 6]
# list1 = list(map(lambda i:i ** 2, list_))
# print(list1)


#2
def type_func(a, s):
    return type(a)
    return type(s)

print(type_func(12, 98))
print(type_func('fjkj', 'dkj'))


