s="a b c d e"
newstring=""
for ch in s:
    if(ch==" "):
        newstring=newstring+"-"

    else:
        newstring=newstring+ch
print(newstring)

