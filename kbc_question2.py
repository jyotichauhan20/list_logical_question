question=["how many continent are there?","what is the capital of india?","Ng me kaun sa course padhaya jata hai?"]
option=["four","nine","seven","eigth"],["chandigarah","bhopal","channai","delhi"],["software engineering","counsling tourism","agricalture"]
i=0
while i<len(question):
    print("apka option hai")
    print()
    print(question[i])
    print("ques.",question[i])
    j=0
    while j<len(option[i]):
    print(i+j,option[i][j])
    j=j+1
i=i+1