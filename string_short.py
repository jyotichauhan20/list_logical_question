string=["b","a","c","d","f","e","h","g"]
i=0
empty=[]
while i<len(string):
    j=i+1
    while j<len(string):
        if string[i]>string[j]:
            swap=string[i]
            string[i]=string[j]
            string[j]=swap
        j=j+1
    empty.append(string[i])
    i=i+1
print(empty)