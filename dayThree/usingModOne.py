'''
    data, functions defined in one Python file 
    can be used in another Python file.

    Modules in Python:
        Python files containing data, functions and classes.
'''

import moduleOne

if __name__ == '__main__':
    print(moduleOne.data)
    moduleOne.funOne()
    moduleOne.funTwo()
    moduleOne.funThree()

