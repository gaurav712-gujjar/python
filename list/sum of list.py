list=[1,2,3,4,5]
sum=0
list2=[]

for i in range(0,len(list)):
    sum=sum+list[i]
    list2.append(sum)

print(list2)