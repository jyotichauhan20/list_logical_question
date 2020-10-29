num=[13,15,100,97,34,65,29]
i=0
first_max=num[0]
second_max=num[0]
third_max=num[0]
while i<len(num):
    if num[i]>first_max:
        first_max=num[i]
    i=i+1
    j=0
    while j<len(num):
        if first_max>num[j] and second_max<num[j]:
            second_max=num[j]
        j=j+1
        k=0
        while k<len(num):
            if second_max>num[k] and third_max<num[k]:
                third_max=num[k]
            k=k+1
print(first_max)
print(second_max)
print(third_max)