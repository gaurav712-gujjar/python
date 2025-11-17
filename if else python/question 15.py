'''Q15 Write a program that takes an integer (1-7) as input and prints the corresponding day of the week (1
for Monday, 2 for Tuesday, etc.).'''


n=int(input("Enter a number: "))

if( n==1 ):
    print("Monday")

elif( n==2 ):
    print("Tuesday")

elif( n==3 ):
    print("Wednesday")

elif( n==4 ):
    print("Thursday")

elif( n==5 ):
    print("Friday")

elif( n==6 ):
    print("Saturday")

elif( n==7 ):
    print("Sunday")

else:
    print("Invalid input")