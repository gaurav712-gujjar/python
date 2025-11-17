list1 = [1, 10, 40, 30, 20]
temp=0

for i in range(0,len(list1)):
    for j in range(i + 1, len(list1)):
        if list1[i] > list1[j]:
            temp = list1[i]
            list1[i] = list1[j]
            list1[j] = temp

print("Sorted List:", list1)