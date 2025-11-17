
n=int(input("Enter Number : "))

rev=0
digit=0
temp=n
while(n>0):

    digit=n%10
    rev=(rev*10)+digit
    n=n//10

print(temp==rev and n==0)

