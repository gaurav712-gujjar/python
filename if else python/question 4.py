'''Q4 Write a program that takes a percentage (integer) as input and prints the corresponding grade based
on the following criteria:
>= 90: Grade A
>= 80: Grade B
>= 70: Grade C
>= 60: Grade D
< 60: Grade F'''
from traceback import print_tb

n=int(input("Enter the percentage: "))

if( n>=90 ):
    print("Grade A")

elif( n>=80 ):
    print("Grade B")

elif( n>=70 ):
    print("Grade C")

elif( n>=60 ):
    print("Grade D")

else:
    print("Grade F")