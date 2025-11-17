num = int(input('Enter a num: '))

cnt = 0
while cnt<25:
    if num > 1:
        for div in range(2, num):
            if num % div == 0:
                break
        else:
            print(f'{num}', end=' ') 
            cnt+=1

    num+=1
