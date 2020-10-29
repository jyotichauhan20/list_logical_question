empty_list=[]
i=0
num_list=[5,3,8,4,6]
while i<len(num_list):
    j=i+1
    while j<len(num_list):
        if num_list[i]>num_list[j]:
            swap=num_list[i]
            num_list[i]=num_list[j]
            num_list[j]=swap
        j=j+1
    empty_list.append(num_list[i])
    i=i+1
print(empty_list)