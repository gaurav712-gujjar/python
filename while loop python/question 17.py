m=int(input("Enter the 1 Number : "))

i=1
while( i<=m ):

    if( m%i==0 ):
        m=m//i
        print( i )

    i += 1


