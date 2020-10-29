num=[[1,2,3],[4,5,6],[10,11,12],[7,8,9]]
i=0
list1=[]
while i<len(num):
    j=0
    s1=0
    while j<len(num[i]):
        s1=s1+num[i][j]
        j=j+1
    list1.append(s1)
    i=i+1
print(list1)
k=0
while k<len(list1):
    if list1[k]>s1:
        # print(list1[k])
        print(num[k])
    k=k+1


