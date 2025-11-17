'''Q11 Write a program that calculates the discount for a product based on its price:
If price is greater than 1000, discount is 10%
If price is between 500 and 1000, discount is 5%
Otherwise, no discount
Print the final price after applying the discount.'''

n=int(input("Enter the price of product: "))

if( n>1000 ):
    print("The discount is 10%")
    print("The Final price is :",n-(n*(10/100)))

elif( n>=500 or n==1000):
    print("The discount is 5%")
    print("The Final price is :",n-(n*(5/100)))

else:
    print("No discount")
