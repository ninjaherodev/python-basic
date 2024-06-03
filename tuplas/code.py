numbers = (1,2,3,5)
strings= ('nico','zule','santi','nico')
print(numbers)
print(strings)
print(type(numbers))
print(type(strings))

print('0 =>', numbers[0])
print('-1 =>', numbers[-1])


print(strings)
print(strings.index('zule'))
print(strings.count('nico'))

my_list= list(strings)
print(my_list)
print(type(my_list))
my_list[1] = 'juli'
print(my_list)
my_tuple = tuple(my_list)
print(my_tuple)