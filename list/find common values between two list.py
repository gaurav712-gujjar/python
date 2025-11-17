list=[1,2,3,5,7]
list1=[1,2,4,7,8,4,5]
com=[]

for i in range(0,len(list)):
    for j in range(0,len(list1)):

        if(list[i]==list1[j]):
            com.append(list1[j])

print(com)

