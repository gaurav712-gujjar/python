list=[10,20,30,50,20,10]
start=0
end=len(list)-1

while( start < end ):
    print(list[start],list[end])
    end -= 1

    if(list[end]==list[start]):
        end=len(list)-1
        start+=1

if(list[start]==list[end]):
    print("duplicat",list[start],list[end])















