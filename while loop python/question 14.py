m=int(input("Enter the 1 Number : "))
n=int(input("Enter the 2 Number : "))

i=2
lcm=1
while( m>1 or n>1 ):
    if( m%i==0 or n%i==0 ):
        if(m%i==0):
            m=m//i
        if(n%i==0):
            n=n//i
        lcm=lcm*i

    else:
        i += 1

print(lcm)
