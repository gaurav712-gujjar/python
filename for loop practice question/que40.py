n=6
sum=0
for i in range(1,n):
    if(n%i==0):
        print(i)
        sum=sum+i

if(sum==n):
    print(n,": Is Perfect Number")

else:
    print(n,": Is Not Perfect")