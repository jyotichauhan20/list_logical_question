num=[70,100,50,40,35,22]
i=0
min_no=num[0]
second_min=num[0]
third_min=num[0]
while i<len(num):
    if num[i]<min_no:
        min_no=num[i]
    i=i+1
    j=0
    while j<len(num):
        if min_no<num[j] and second_min>num[j]:
            second_min=num[j]
        j=j+1
        k=0
        while k<len(num):
            if second_min<num[k] and third_min>num[k]:
                third_min=num[k]
            k=k+1
print(min_no)
print(second_min)
print(third_min)