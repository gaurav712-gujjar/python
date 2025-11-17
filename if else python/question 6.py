'''8. Write a program to find the first and last digit of a number.'''

n=int(input("enter the number :"))

rev = 0
for i in range(n):

    n = int(n) // 10
    rev=int(n)%10


print( rev )
