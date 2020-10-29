num=30
n=[10,11,12,13,14,17,18,19]
a=[]
i=0
while i<len(n):
    j=i
    while j<len(n):
        if n[i]+n[j]==30:
            s=[n[i],n[j]]
            a.append(s)
        j=j+1
    i=i+1
print(a)