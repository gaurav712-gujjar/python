n=int(input("Enter a number: "))

i=1

while(i<=n):

    j = 1
    count = 0

    while(j<=n):
        if(i%j==0):
            count += 1
        j += 1

    if(count==2):
        print(i)

    i += 1