
n=int(input("Enter a number: "))
sum=0
temp=n
while( n  > 0):
     i=1
     fac=1
     r=n%10

     while( i<=r ):
         fac=fac*i
         i += 1

     sum=sum+fac
     n=n//10
print(sum)
if( sum==temp ):
    print( "Strong Number")

else:
    print( "Not Strong Number")
