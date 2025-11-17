'''Q5 Write a program that checks if a given letter is a vowel (a, e, i, o, u) or a consonant.'''

n=str(input("Enter Your Letter :"))

if( n in "aeiou"):
    print("vowel")

else:
    print("consonant")