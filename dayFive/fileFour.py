'''
    Reading line by line
'''

fobj = open('fileFour.py','r')
firstLine = fobj.readline()
secondLine = fobj.readline()
print(firstLine)
print(secondLine)
fobj.close() 