num=5
list=[]
for i in range(0,num):
    temp=[]
    for j in range(0,num-i):
        print("-",end="")

    for k in range(0,i+1):
        if(k==0 or i==k ):
            print(1,end=" ")
            temp.append(1)
        else:
            a=list[i-1][k]+list[i-1][k-1]
            print( a,end=" ")
            temp.append(a)

    list.append(temp)
    print(" ")
    print(list)

