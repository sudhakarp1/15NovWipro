lstOne = [10, 20,[1, 2, 3], 30, 40, 50]

lstTwo = lstOne.copy() 
lstOne[2].append(5)
lstOne.append(60)
lstTwo.append(70)

print(f'lstOne: {lstOne} id: {id(lstOne)}')
print(f'lstTwo: {lstTwo} id: {id(lstTwo)}')
