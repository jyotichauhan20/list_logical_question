elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
count1=0
count2=0
count3=0
sum1=0
sum2=0
sum3=0
average1=0
average2=0
average3=0
while i<len(elements):
    if elements[i]%2==0:
        count1=count1+1
        sum1=sum1+elements[i]
        average1=sum1//count1
    else:
        count2=count2+1
        sum2=sum2+elements[i]
        average2=sum2//count2
    sum3=sum1+sum2
    count3=count1+count2
    average3=sum3//count3
    i=i+1
print("even number is",count1,"and sum of even is",sum1)
print("odd number is",count2,"and the sum of odd is",sum2)
print("all even/odd number of sum is",sum3)
print("all even/odd number of count3",count3)
print("odd average is",average1)
print("even average is",average2)
print("and all nuber of average",average3)