numWords = {'one':1, 'two':2, 'three':3,'four':4, 'five':5, 'six':6, 
            'seven':7, 'eight':8, 'nine':9, 'ten':10, 'hundred':100, 
            'thousand':1000, 'lakhs': 100000, 'crore':10000000}

print(numWords)

lstOne = list(numWords)
lstTwo = list(numWords.keys())
lstThree = list(numWords.values())
listFour = list(numWords.items())

print(f'List 1: {lstOne}')
print(f'List 2: {lstTwo}')
print(f'List 3: {lstThree}')
print(f'List 4: {listFour}')