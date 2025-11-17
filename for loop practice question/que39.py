list=["red","blue","green","red","blue"]
for i in range(len(list)):
    a=0
    for j in range(len(list)):
        if list[i]==list[j]:
            a+=1

    if(a==1):
        print(list[i])
