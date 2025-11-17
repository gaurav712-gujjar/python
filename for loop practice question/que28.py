list=[2,-3,5,1,0,-7,-1,-1,-2]
count=0
for i in range(0,len(list)):
    if(list[i]<0):
        count=count+1
print(count)