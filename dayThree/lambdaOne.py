'''
    lambda function or expression used as anonymous functions
    When do we use lambda
        lambda expression can be created on the 
        fly(when you require a function) put a expression 
        when passing functions as arguments
'''

fun = lambda a, b: a + b
print(fun(10,20))

def funDemo(fun, a, b):
    return fun(a,b)

print(funDemo(lambda x, y: x * y, 10, 20))

