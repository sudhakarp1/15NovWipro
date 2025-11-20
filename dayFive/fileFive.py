'''
    Reading line by line

fobj = open('fileFive.py','r')
allLines = fobj.readlines()
print(allLines)
fobj.close()
'''

fobj = open('fileFive.py','r')
for line in fobj:
    print(line,end='')
fobj.close()

