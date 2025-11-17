list=[1,5,6,2,8,4]
even=[]
odd=[]

for i in range( 0,len(list)):
    if(list[i]%2==0):
        even.append(list[i])

    else:
        odd.append(list[i])

print("even :",even)
print("odd :",odd)