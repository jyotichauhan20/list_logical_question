list=[1,2,3,4,5,6,7,8]
i=-1
count=0
while True:
    if list[0]==list[i]:
        break
    count=count+1
    i=i-1
print(count)