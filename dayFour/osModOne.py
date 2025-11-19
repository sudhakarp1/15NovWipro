'''
here Path is a class from pathlib 

from pathlib import Path
import os 

pathVar = Path('.')
print(pathVar)
print(pathVar.absolute())
print(pathVar.is_file())
print(pathVar.is_dir())
print(pathVar.exists())

print(os.listdir(pathVar))

from pathlib import Path
import os 
pathNew = Path('/nameone/nametwo/dirThree/fileOne.txt')

print(pathNew.exists())
print(pathNew.name)
print(pathNew.suffix)
print(pathNew.stem)
print(pathNew.parent)
'''

import os 
print(os.path.join('home','hello','world','fileOne.txt'))
