list1=[12,23,11,33,34]
list2=[23,12,10,14,11]
i=0
s1=0
s2=0
while i<len(list1):
    s1=s1+list1[i]
    j=0
    while j<len(list2):
        s2=s2+list2[j]
        j=j+1
    i=i+1
    print(s1)
    print(s2)