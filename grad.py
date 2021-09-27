numofrange=int(input("enter the number="))
nameslis=[]
scorelist=[]
students=[]
i=0
while i<=numofrange:
        emptylist=[]
        name_of_students=input("enter the name of students=")
        score_of_students=float(input("enter the score="))
        emptylist.append(name_of_students)
        emptylist.append(score_of_students)
        scorelist.append(score_of_students)
        nameslis.append(name_of_students)
        students.append(emptylist)
        i=i+1
j=0
largest = scorelist[0] 
lowest = scorelist[0] 
largest2 = None
lowest2 = None
for k in scorelist[1:]:     
        if k > largest: 
                largest2 = largest
                largest = k
        elif largest2 == None or largest2 < k: 
                largest2 = k
        if k< lowest: 
                lowest2 = lowest
                lowest = k
        elif lowest2 == None or lowest2 > k: 
                lowest2 = k
              
        print("Second Smallest element is:", lowest2) 
print(lowest2)
list2=[]
for i  in students:
        if lowest2 in i:
                list2.append(i)
# for k in list2:
#     print()
# list2.sort(key=None, reverse=False)

print(sorted(list2))