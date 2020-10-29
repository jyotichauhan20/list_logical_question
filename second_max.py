num=[12,45,33,19,20,23]
i=0
first_max=0
second_max=0
while i<len(num):
    if num[i]>first_max:
        first_max=num[i]
    i=i+1
    j=0
    while j<len(num):
        if first_max>num[j] and second_max<num[j]:
            second_max=num[j]
        j=j+1
print(first_max)
print(second_max)