import numpy as np

l = [ [5, 6, 9, 10, 11], [ 1, 2, 3, 5, 6 ] ]

print( l, type(l), len(l) )
arr = np.array( l )
print( f"arr = { arr }", type( arr ), len( arr ), arr.shape )
print( f"arr[0] = { arr[0] }" )
print()
print( "Printing Numpy Array in the loop" )
for i in arr:
    print( f"i : { i }", end=' and j : ' )
    for j in i:
        print( j, end=' -> ' )
    print()

arr[1] = 9
print( "Checking Mutability, " )
print( f"arr = { arr }" )
arr[1][3] = 5
print( f"arr = { arr }" )
print()

counter = 0

print( '[', end = '')
for i in range( len( l ) ):
    print( '[', end=' ' )
    for j in l[i]:
        print( j, end=' ' )

    if( i == ( len(l) - 1 ) ):
        print(']', end=']')
    else:
        print( ']' )