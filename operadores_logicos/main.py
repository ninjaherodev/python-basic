print('AND')
print('True and True =>', True and True)
print('True and False =>', True and False)
print('False and True =>', False and True)
print('False and False =>', False and False)

print(10 > 5 and 5 < 10) # True
print(10 > 5 and 5 > 10) # False

stock = int(input("Ingrese el numero de stock:"))
print(stock >= 100 and stock <=1000)
print('OR')
print('True or True =>', True or True)
print('True or False =>', True or False)
print('False or True =>', False or True)
print('False or False =>', False or False)


role = input('Digita el rol:')
print(role == 'admin' or role =='seller')

print('not')
print('not True =>', not True)
print('not False =>', not False)

print('not True and True =>', not (True and True))
print('not True and False =>',not (True and False))
print('not False and True =>',not(False and True))
print('not False and False =>',not(False and False))

stock = int(input("Ingrese el numero de stock:"))
print(not (stock >= 100 and stock <=1000))