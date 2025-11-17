n=int(input("enter the number :"))

sum=0
digit=0
len=len(str(n))
temp=n

while( n>0 ):
    digit=n%10
    sum=sum+digit**len
    n=n//10

if( sum==temp ):
    print( " Aramstrong Number ")

else:
    print( " Not Aramstrong Number ")