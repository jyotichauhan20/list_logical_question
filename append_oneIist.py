list=[[1,2,3],[4,5,6],[7,8,9,10]]
i=0
empty=[]
while i<len(list):
    j=0
    while j<len(list[i]):
        if list[i][j]==list[i][j]:
            empty.append(list[i][j])
        j=j+1
    i=i+1
print(empty)