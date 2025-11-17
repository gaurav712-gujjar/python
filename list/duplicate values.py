list=[1,2,1,3,3,1]
newlist=[]

for i in range(0,len(list)):
    for j in range(i+1,len(list)):

        if( list[i]==list[j]):
            newlist.append(list[i])

print(newlist)
