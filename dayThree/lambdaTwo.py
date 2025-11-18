def funDemo(fun, a, b):
    return fun(a,b)

print(funDemo(lambda x, y: x + y, 10, 20))#add
print(funDemo(lambda x, y: x - y, 100, 20))#sub
print(funDemo(lambda x, y: x * y, 10, 20))#multi
print(funDemo(lambda x, y: x // y, 1020, 20))#divi
