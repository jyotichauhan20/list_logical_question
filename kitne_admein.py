elements=[23,14,56,12,19,9,15,25,31,42,43]
i=0
even=0
odd=0
while i<len(elements):
    if elements[i]%2==0:
        even=even+1
    else:
        odd=odd+1
    i=i+1
print(even)
print(odd)