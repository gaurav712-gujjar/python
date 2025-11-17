
n=int(input("Enter Number :"))

firstdigit=n
lastdigit=n%10
while(  firstdigit>=10 ):

    firstdigit=firstdigit//10

print(firstdigit,lastdigit)

