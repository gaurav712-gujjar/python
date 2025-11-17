'''Q9 Write a program that takes three sides of a triangle as input and checks if those sides form a valid
triangle. A triangle is valid if the sum of any two sides is greater than the third side.
Check conditions like a + b > c, b + c > a, and a + c > b.'''

n1 = int(input("Enter the first side: "))
n2 = int(input("Enter the second side: "))
n3 = int(input("Enter the third side: "))

if( n1+n2>n3 and n2+n1>n1 and n1+n3>n2 ):
    print("The triangle is valid")

else:
    print("The Triangle is Invalid ")