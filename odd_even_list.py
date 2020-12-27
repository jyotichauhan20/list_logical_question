list=[1,2,3,4,5,6,7,8,9,10]
i=0
empty1=["even"]
empty2=[]
empty3=["odd"]
empty4=[]
empty5=[]
count1=0
count2=0
while i<len(list):
    if list[i]%2==0:
        count1=count1+1
        empty2.append(list[i])
    else:
        count2=count2+1
        empty4.append(list[i])
    i=i+1
empty1.append(count1)
empty3.append(count2)
empty1.append(empty2)
empty3.append(empty4)
empty5.append(empty1)
empty5.append(empty3)
print(empty5)

