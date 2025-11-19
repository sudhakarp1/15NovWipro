'''
#method #1 of import statement
import moduleOne

if __name__ == '__main__':
    moduleOne.funOne()
    moduleOne.funThree()
    moduleOne.funTwo()


#method #2 of import statement
import moduleOne as mo #here mo is an alias for moduleOne

if __name__ == '__main__':
    mo.funOne()
    mo.funThree()
    mo.funTwo()

'''

from moduleOne import funOne, funTwo
import moduleOne

if __name__ =='__main__':
    funOne()
    funTwo()
    moduleOne.funThree()
