import numbers

print(isinstance(234.34, numbers.Number))
print(isinstance(100, numbers.Number))
print(isinstance(34+56j, numbers.Number))

print(isinstance('234.34', numbers.Number))

print(isinstance(234.34, numbers.Integral))
print(isinstance(234.34, numbers.Real))

#for example
x, y = 10, 20.34

if isinstance(x, numbers.Number) and isinstance(y, numbers.Number):
    print(f'Adding : {x+y}')
