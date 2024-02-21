'===============JSON================'
# JavaScript Object Notation - универсальный формат, в котором мы можем хранить данные в типах данных, понятных для почти всех языков

import json
python_data = None
json_data = json.dumps(python_data)
print(json_data) 

with open ('test.json','w') as file:
    json.dump(json_data, file)
print(python_data)



# десерализация - перервод с json строки в python обьекты
#loads - метод для десериализации json строки
# load - метод для десериализации с json файла


#ссериализация - перевод python обьектов в json
# import json
# json_data = '[1, 2, 3, 4, 5]'
# python_data = json.loads(json_data)
# print(python_data) 

# with open ('test.json','r') as file:
#     python_data = json.load(file)
# print(python_data)



