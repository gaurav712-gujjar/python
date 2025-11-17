
n=int(input("Enter a number: "))
sum=0
first=n
while( first>=10 ):
    first=first//10

last=n%10
sum=first+last
print( first, last ,sum)