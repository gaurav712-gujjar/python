list=[10,20,30,40,50]
count=len(list)
average=0
sum=0
for i in range(0,len(list)):
    sum=sum+list[i]
    average=sum//count

print(average)

