magic_square = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]
i=0
sum_row=0
sum_column=0
while i<len(magic_square):
    j=0
    sum_column=sum_column+magic_square[i][j]
    sum_row=sum_row+magic_square[j][i]
    i=i+1
print(sum_row)
print(sum_column)
k=0
sum_diagonal=0
while k<len(magic_square):
    n=0
    while n<len(magic_square[k]):
        if k==n:
            sum_diagonal=sum_diagonal+magic_square[k][n]
        n=n+1
    k=k+1
print(sum_diagonal)
if sum_column==sum_row==sum_diagonal:
    print("magic_square")
else:
    print("not magic_square")
               