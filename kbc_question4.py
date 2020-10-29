question=["how many continent are there?","what is the capital of india?","Ng me kaun sa course padhaya jata hai?"]
option=[["four","nine","seven","eigth"],["chandigarah","bhopal","channai","delhi"],["software engineering","counsling tourism","agricalture"]]
ans=[2,1,4]
i=0
while i<len(question):
    print(question[i])
    j=0
    while j<len(option[i]):
        j=j+1
    user=int(input("enter the number="))
    if user==ans[i]:
        print("correct",user)
    else:
        print("exite")
        break
        # print("wrong",user)
    i=i+1