sentence = "my name is jyoti chauhan"
split_empty = []
string =" "
for i in sentence:
    if i== " ":
        split_empty.append(string)
        string = " "
    else:
        string=string+i
if string:
    split_empty.append(string)
    print(split_empty)