import math
x = 3.3
print('x:',x)
y =1.1 + 2.2
print('y:',y)

print(x == y)

#y_str = format(y,".2g")
y_str = f"{y:.2g}"
print('y_str:',y_str)
print(y_str == str(x))

print('*' * 10)

print(abs(x- y)< 0.00001)
print(math.isclose(x, y)) 