mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
subStr = "over"
replacestr="on"
list1=mainStr.split()
output=""
i=0
for  word in list1:
    if word==subStr:
        output=output+replacestr
        output=output+" "
    else:
        output=output+word
        output=output+" "
print(output)

# main_str= "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
# sub_str="over"
# text =''
# i=0
# last_i = 0
# while i <  len(main_str):
#     if main_str[i:i+len(sub_str)] == sub_str:
#         text +=main_str[last_i:i]
#         last_i=i+len(sub_str)
#         i=i+len(sub_str)
#     else:
#         i+=1
# text+= main_str[last_i:i]

# print(text)