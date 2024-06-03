numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers)
print(type(numbers))

task = ['make a dishes','play video game']
print(task)

types = [1, True, 'Hola']
print(types)

print(numbers[0])
print(task[0])

task[0] = 'watch platzi coourses'
print(task)

print(numbers[:3])

print(True in types)
print('Hola' in types)

# Crud Create, Read, Update & Delete
numbers.append(700)
numbers.insert(0, 1000)
for numero in numbers:
    print(numero)

personas = [
    {"name": "Fabio", "edad": 12},
    {"name": "Ana", "edad": 30}
]

print(personas)

new_list= numbers + personas

print(new_list)

print(new_list.index(1000))
new_list.remove(1000)
new_list.pop()
new_list.pop(0)
new_list.reverse()
print(new_list)

numbersa = [2,3,4,1,5,10,6,7,8,9]
print(numbersa)
numbersa.sort(reverse=True)
print(numbersa)