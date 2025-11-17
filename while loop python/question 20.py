m=int(input("Enter the 1 Number : "))

i=1
sum=0
temp=m
while( i<=m ):

    if( m%i==0 ):
        m=m//i
        sum=sum+i
    i += 1

if(sum==temp):
    print("Perfect Number")

else:
    print("Not Perfect Number")


