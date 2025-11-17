'''Q10 Write a program that calculates the Body Mass Index (BMI) based on user input for weight (in
kilograms) and height (in meters). Then categorize the BMI into:
Underweight (BMI < 18.5)
Normal weight (18.5 <= BMI < 24.9)
Overweight (25 <= BMI < 29.9)
Obesity (BMI >= 30)'''

weight=float(input("Enter weight in kilograms:"))
height=float(input("Enter height in meters:"))
bmi= weight/(height**2)

if( bmi>=30 ):
    print(" OBESITY ")

elif( bmi<=25 and bmi<29.9 ):
    print("OVERWEIGHT")

elif( bmi<=18.5 and bmi<24.9 ):
    print("NORMAL WEIGHT")

else:
    print("Underweight")
