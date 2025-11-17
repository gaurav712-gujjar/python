'''Q14 Write a program that categorizes a given age into different groups:
Infant (0-1 year)
Toddler (2-4 years)
Child (5-12 years)
Teenager (13-19 years)
Adult (20-59 years)
Senior (60 years and above)'''

age = int(input("Enter the age: "))

if( age>=60 ):
    print("Senior")

elif( age>=20 ):
    print("Adult")

elif( age>=13 ):
    print("Teenager")

elif( age>=5 ):
    print("Child")

elif( age>=2 ):
    print("Toddler")

else:
    print("Infant")