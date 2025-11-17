list = [10,20,4,6,12,24]

for i in range(0,len(list)):

    for j in range(i+1,len(list)):
       #print(j,list[j])

       if( list[i]>list[j] ):
           temp = list[i]
           list[i] = list[j]
           list[j] = temp
print("swapping value:",list)




