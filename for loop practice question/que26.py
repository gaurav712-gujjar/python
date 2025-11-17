list=[2,3,5,7,11,13,17]
count=0
for i in range(0,len(list)):

    if(list[i]%2==0):
        count=count+1

    if(count==2):
        print(list[i])

