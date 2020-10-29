char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i=0
list1=[]
while i<len(char_list):
    j=0
    list2=[]
    count=0
    while j<len(char_list):
        if char_list[i]==char_list[j]:
            count=count+1
        j=j+1
    list2.append(char_list[i])
    list2.append(count)
    if list2 not in list1:
        list1.append(list2)
    i=i+1
print(list1)