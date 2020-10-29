# name=["n","i","t","i","n"]
num=[1,2,3,2,1]
a=len(num)
i=a-1
b=[]
while i>=0:
    b.append(num[i])
    i=i-1
if num==b:
    print("it is palimdrome")
else:
    print("it is not palidrome")