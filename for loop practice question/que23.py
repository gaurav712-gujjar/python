list=[3,1,4,1,5,9,2,8]
max=0
secondmax=0
for i in range (len(list)):
    if(list[i]>max):
        secondmax=max
        max=list[i]
    elif(list[i]>secondmax and list[i]!=max):
        secondmax=list[i]

print(secondmax)
