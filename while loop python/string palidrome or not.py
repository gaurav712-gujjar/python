n=(input("Enter Character :"))
a=False
i=0
j=len(n)-1
while( i<len(n) ):
    if( n[i]!=n[j] ):
        a=True
        break
    i += 1
    j -= 1

if( a==True ):
    print("Not palidrome")
else:
    print("Palindrome")

