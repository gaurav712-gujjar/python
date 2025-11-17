list=[5,2,9,1,5,6]
temp=0
for i in range(0,len(list)):
    for j in range(i+1,len(list)):
        if( list[i]>list[j] ):
            temp=list[i]
            list[i]=list[j]
            list[j]=temp
print("sortted list :",list)
