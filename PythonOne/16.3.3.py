import json

json_obj = r'{"name" : "tony", "age" : 30, "sex" : true, "a" : [1,3], "b":["A", "B", "C"]}'

py_dict = json.loads(json_obj)
print(type(py_dict))
print(py_dict['name'])
print(py_dict['age'])
print(py_dict['sex'])

py_lista = py_dict['a']
print(py_lista)

py_listb = py_dict['b']
print(py_listb)

with open('data/data2.json', 'r') as f:
    data = json.load(f)
    print(data)
    print(type(data))