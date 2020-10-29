num=[12,10,8,9,5,20,4]
i=0
first_min=num[0]
while i<len(num):
    if num[i]<first_min:
        first_min=num[i]
    i=i+1
print(first_min)