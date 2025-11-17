
n=int(input("enter your number :"))

count=0
sum=0
for i in range(n):
    sum=sum+n%10
    n=n//10
    count=count+1


print("sum of  digits :",sum)