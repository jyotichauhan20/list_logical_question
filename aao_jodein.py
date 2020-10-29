elements=[23,14,56,12,19,9,15,25,31,42,43]
i=0
count1=0
count2=0
s1=0
s2=0
while i<len(elements):
    if elements[i]%2==0:
        count1=count1+1
        s1=s1+i
    else:
        count2=count2+1
        s2=s2+i
    i=i+1
print(count1)
print(count2)
print(s1)
print(s2)
print("even","sum of ",count1)
print("odd","sum of",count2)