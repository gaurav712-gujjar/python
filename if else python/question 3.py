'''Q3 Write a program to check if a given year is a leap year. A leap year is divisible by 4 but not by 100
unless it is also divisible by 400.'''

n=int(input("Enter Your Year :"))

if(n%4==0 and n%100!=0 or n%400==0):
    print("Leap Year")

else:
    print("Not Leap Year")