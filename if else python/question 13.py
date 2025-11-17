'''Q13 Write a program that simulates a simple ATM. The user should be able to:
Check balance
Deposit money
Withdraw money (ensure the balance doesn't go negative) Use an if-else structure to handle the user's'''


blance=10000

print("Welcome to the ATM ")
print(" 1. check blance ")
print(" 2. deposit ")
print(" 3. withdraw ")

user=str(input("Enter your choice: "))

if( user == "1" ):
    print("your blance is",blance)

elif( user == "2" ):
    deposit=float(input("Enter your deposit: "))
    blance += deposit
    print("deposit succesfully",deposit)
    print("your available blance is",blance)

elif( user == "3" ):
    withdraw=float(input("Enter your withdraw: "))

    if( withdraw<=blance ):
        blance-=withdraw
        print("withdraw succesfully",withdraw)
        print("remaning blance is",blance)

    else:
       print("insufficient balance")


else:
    print("invalid choice")