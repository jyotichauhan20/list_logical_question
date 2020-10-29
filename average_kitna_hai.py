elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
count1=0
count2=0
sum1=0
sum2=0
average1=0
average2=0
while i<len(elements):
    if elements[i]%2==0:
        count1=count1+1
        sum1=sum1+i
        average1=sum1//count1
    else:
        count2=count2+1
        sum2=sum2+i
        average2=sum2//count2
    i=i+1
print("even number",count1,"sum of",sum1)
print("odd number",count2,"sum of",sum2)
print("average1",average1)
print("average2",average2)