list1=[]
num1=int(input("enter the number="))
i=0
while i<num1:
    num2=int(input("enter the number="))
    list1.append(num2)
    i=i+1
print(list1)
j=0
count=0
max1=list1
max2=0
while j<len(max1):
    if max1[j]>max2:
        count=count+1
        max2=max1[j]
    j=j+1
print(max2)
k=0
count=0
while k<len(list1):
    if list1[k]==max2:
        count=count+1
    k=k+1
print(count)