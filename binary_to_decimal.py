binary_decimal=[1,0,0,0,0,1,0]
a=len(binary_decimal)-1
count=0
calculate=1
while a>=0:
    count=count+(binary_decimal[a]*calculate)
    calculate=calculate*2
    a=a-1
print(count)