my_dict = {}

print(type(my_dict))

my_dict = {
    "id": 1,
    "name": "fabio",
    "lastName":"rojas",
    "age": 42
}
print(len(my_dict))
print(my_dict['age'])
print(my_dict['name'])
print(my_dict.get('name'))

print('avion' in my_dict)
print('age' in my_dict)

my_dict['age']= 44
my_dict['name']= 'neyla'
my_dict['langs']=['python', 'javascript']
my_dict['langs'].append('rust')
del my_dict['lastName']
my_dict.pop('age')
print(my_dict)
print('items:',my_dict.items())
print('keys:',my_dict.keys())
print('values:',my_dict.values())