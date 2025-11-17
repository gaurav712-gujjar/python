'''Q12 Write a program that takes the name of a month as input and prints the number of days in that
month. Consider leap years for February.'''

month=str(input("Enter the month name :"))

if( month=="april" or month=="june" or month=="september" or month=="november" ):
    print("The number of days in This month is 30 ")

elif(month=="january" or month=="march" or month=="may" or month=="july" or month=="august" or month=="october" or month=="december"):
    print("The number of days in This month is 31 ")

else:
    print("Invalid Month")
