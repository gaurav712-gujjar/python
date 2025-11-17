list = [1, 7, 12, 15,5]
target = 19

for i in range( 0,len(list) ):

    for j in range( i + 1, len(list) ):

        if( list[i] + list[j] == target ):

            print( list[i], list[j] )
