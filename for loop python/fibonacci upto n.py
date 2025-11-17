
n=int(input('Enter a number: '))
ans=0
a = 0
b = 1

for i in range(1,n+1):

    ans=a+b
    print( b )
    a=b
    b=ans

print(ans)
