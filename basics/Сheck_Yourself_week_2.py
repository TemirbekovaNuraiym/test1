

#1
klub = {'Мурату':24, 'Эржану':21, 'Карине':24,'Алтынай':17, 'Айбеку':16}
for k, v in klub.items():
    if v < 17:
        print('no')
    else:
        print('yes')

#5
dict_ = {}
for i in range(1, 10):
    key = i
    values = i ** 2
    dict_[key] = values
    print(dict_)

#8
int1 = int(input('Введите сумму: '))
if int1 < 0:
    print("Сумма не может быть отрицательной!")


#9
list_ = [i for i in range(1,25,) if i % 2 == 0]
print(list_)

#3
dict_ = {'banana': 24, 'apple': 7}
dict_.pop('banana')
print(dict_)


#7
dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_dict = sorted(dict_)
print(sorted_dict)

