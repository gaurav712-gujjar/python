n=int(input('Enter a number: '))

ans=0
a = 0
b = 1
while(n > 0):

    ans=a+b
    print( b )
    a=b
    b=ans
    n -= 1

print(ans)
