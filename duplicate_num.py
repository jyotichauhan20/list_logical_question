num=[19,17,12,17,17,18,10,17,14,12,19,17,12,13,11]
i=0
list1=[]
while i<len(num):
    if num[i] not in list1:
        list1.append(num[i])
    i=i+1
print(list1)