list=[2,3,2,5,6,-1]
reverse_list=[]

for i in range(len(list)-1,-1,-1):
    reverse_list=reverse_list+[list[i]]
    #reverse_list.append(list[i])

print("original list :",list)
print("reverse list :",reverse_list)

