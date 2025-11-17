text="level"
a=1
for i in range(0,len(text)):
    j=(len(text)-1)-i

    if(text[i]!=text[j]):
        a=1
        break
    else:
        a=2

if(a==2):
    print("Palindrome")

else:
    print("Not Palindrome")