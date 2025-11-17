row = int(input('Enter the row: '))
col = int(input('Enter the col: '))

mat = []
for i in range(row):
    mat.append([])
    for j in range(col):
        mat[i].append(0)

print(mat)