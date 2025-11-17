list=[2,4,6,8,10,1,3]
list1=[]
for i in range (len(list)):
    if(list[i]%2!=0):
        list1=list1+[list[i]]

print(list1)