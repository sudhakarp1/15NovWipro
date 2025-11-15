'''
    Adjustment of month and Year as per disparate variation 
    formula using conditional expression
'''

d, m, Y = 15, 11, 2025 #month is January
c= Y // 100
am, y = (m + 10, (Y-1)%100) if m <= 2 else (m - 2, Y%100)

#Disparate Variation Formula for finding out Day of the Week
w = int(d + (2.6 *am - 0.2) + y + y // 4 + c // 4 - 2 * c) % 7 
#print(f'm is {m} after adjustment m is {am} and y {y}')
print(f'W for: {d}/{m}/{Y} is {w}')



