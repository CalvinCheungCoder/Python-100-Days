import json

py_dict = {'name' : 'tony', 'age' : 30, 'sex' : True}
py_list = [1,3]
py_tuple = ('A', 'B', 'C')

py_dict['a'] = py_list
py_dict['b'] = py_tuple

print(py_dict)
print(type(py_dict))

json_obj = json.dumps(py_dict)
print(json_obj)
print(type(json_obj))

json_obj = json.dumps(py_dict, indent=4)
print(json_obj)

with open('data/data1.json', 'w') as f:
    json.dump(py_dict, f)

with open('data/data2.json','w') as f:
    json.dump(py_dict, f, indent=4)