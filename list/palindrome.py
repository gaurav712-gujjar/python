list="level"
a=1

for i in range(0,len(list)):
    j=(len(list)-1)-i

    if(list[i] != list[j]):
        a=1
        break

    else:
        a=2

if(a == 2):
    print("palindrome")

else:
    print("not palindrome")