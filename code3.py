list=["JYOTI","rubi","CHAUHAN","yadav","mohini","MOHINI"]
i=0
count1=0
count2=0

while i<len(list):
    if (list[i].islower()):
        count1=count1+1
    elif (list[i].isupper()):
        count2=count2+1
    i=i+1
print(count1)
print(count2)
    
