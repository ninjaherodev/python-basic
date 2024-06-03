name = "Fabio"
lastName = "Rojas"
age = 42
print(name)
print(lastName)

fullName = name + " " + lastName

print(fullName)

quote = "I'm Fabio Rojas"
print(quote)

quote2 = 'she said "Hello"'
print(quote2)

#Format
template = "Hola, mi nombre es " + name + " y mi apellido es " + lastName + " y mi edad es " + str(age)
print('v1:',template)

template = "Hola, mi nombre es {} y mi apellido es {} y mi edad es {}".format(name, lastName, age)
print('v2:',template)

template = f"Hola, mi nombre es {name} y mi apellido es {lastName} y mi edad es {age}"
print('v3:',template)