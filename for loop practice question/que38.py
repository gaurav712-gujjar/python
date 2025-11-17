list=[4,9,16,25,36]
newlist=[]
for n in list:
    i=1
    while(i*i!=n):
        i+=1

    newlist=newlist+[i]

print(newlist)
