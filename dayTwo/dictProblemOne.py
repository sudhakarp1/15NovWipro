inputStr = 'fifty three crore ninety eight lakhs ' \
'twenty four thousand eighty one'

#Output: 539824081
Words = {'one':1, 'two': 2, 'three':3,'four':4, 'five':5,
        'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten':10,
        'eleven':11,'twelve': 12, 'thirteen': 13, 'fourteen':14,
        'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18,
        'nineteen': 19, 'twenty': 20, 'thirty':30, 'forty': 40, 
        'fifty':50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90,          
        'hundred':100,  'thousand':1000, 'lakhs': 100000,
        'crore': 10000000 }

#print(len(nums))
#if less than hundred add the values else multiply the values.
temp, res = 0, 0

for num in inputStr.split():
    if num in Words:
        if Words[num]<100:
            temp += Words[num]
        else:
            res = res + temp * Words[num]
            temp = 0

res += temp
print(f'Output: {res}')


