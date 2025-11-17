n=int(input('emter n : '))

count=0
digit=0
sum=0
temp=n

while( n> 0):
    n=n//10
    count=count+1

n=temp

while( temp>0 ):
    digit=temp%10
    sum=sum+digit**count
    temp=temp//10

if( sum==n ):
    print( " Armstrong Number ")

else:
    print( " Not Armstrong Number ")


