'''Q8 Write a program that checks if a username and password entered by the user match the pre-set values
username = "admin" and password = "1234". If both match, print "Login Successful", otherwise print
"Login Failed".'''

username=str(input("Enter your username: "))
password=str(input("Enter your password: "))

if( username in "admin" and password in "1234" ):
    print("Login Successful")

else:
    print("Login Failed")
