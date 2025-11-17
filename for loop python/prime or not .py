
n=int(input("Enter Your Number:"))

count=0

for i in range(n,0,-1):

    if( n%i==0 ):
        count=count+1

if( count==2 ):
    print("prime")

else:
    print("not prime")


