list=[11123,33,45,67,99]
max=list[0]
min=list[0]

for i in range(0,len(list)):
    curr=list[i]

    if(  curr > max ):
        max=curr

    if( curr < min ):
        min=curr

print("Maximum value :",max)
print("Minimum value :",min)