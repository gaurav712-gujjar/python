data="hey rame"
d={}
for i in data:
    if( i in "aeiou" ):
        d[i]=1
        if( i in d ):
            d[i]=d[i]+1
        else:
            d[i]=1

    print(i,d)


d={10:"japan","salary":20}
print("old :",d)

if( "salary" not in d ):
    d["salary"]=20

else:
    d["salary"]+=1

print(d)
