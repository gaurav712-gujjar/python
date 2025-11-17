from operator import truediv

n=int(input("enter input :"))
i=2
a=False

while(i<n):
    if(n%i==0):
        a=True
        break
    i+=1

if(a==False):
    print("not prime")

else:
    print("prime")