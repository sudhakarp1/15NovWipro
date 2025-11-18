def Add(a, b):
    return a + b

def Sub(a, b):
    return a - b

def Divi(a, b):
    return a // b

def Multi(a, b):
    return a * b

def funDemo(fun, a, b):
    return fun(a,b)

print(funDemo(Add, 10, 20))#add
print(funDemo(Sub, 100, 20))#sub
print(funDemo(Multi, 10, 20))#multi
print(funDemo(Divi, 1020, 20))#divi