import numpy as np

"""
arr1 = np.array( [ list( range(1, 11) )
                 , list( range(11, 21) )
                 , list( range(21, 31) ) ] )

arr2 = np.array( [ list( range(1, 11) )
                 , list( range(31, 41) )
                 , list( range(41, 51) ) ] )

print( arr1 )
print()
print( arr2 )
print()
print( f"arr1.ravel() = { arr1.ravel() }" )
print()
print( "np.intersect1d( arr1, arr2 )," )
print( np.intersect1d( arr1, arr2 ) )
print()
print( "np.union1d( arr1, arr2 )," )
print( np.union1d( arr1, arr2 ) )
print()
print( "np.setdiff1d( arr1 , arr2 )," )
print( np.setdiff1d( arr1, arr2 ) )
print()
print( "np.setdiff1d( arr2 , arr1 )," )
print( np.setdiff1d( arr2, arr1 ) )
print()
print( np.in1d( arr2, arr1 ) )
print()
print( arr2[ np.in1d( arr2, arr1 ) ] )
"""

"""
arr1 = np.array( [ list( range(1, 11) )
                 , list( range(11, 21) )
                 , list( range(21, 31) ) ] )

arr2 = np.array( [ list( range(1, 11) )
                 , list( range(31, 41) )
                 , list( range(41, 51) ) ] )

def individual_mean( arr1, arr2 ):
    row, col = arr1.shape

    arr3 = []
    for i in range( row ):
        temp = []
        for j in range( col ):
            temp.append( (arr1[i][j] + arr2[i][j] ) / 2 )

        arr3.append( temp )

    arr3 = np.array( arr3 )
    return arr3

print( individual_mean( arr1, arr2 ) )
"""

arr1 = np.array( [ [ list( range( 1, 6 ) ) ,list( range( 6, 11 ) ) ,list( range( 11, 16 ) ) ]
                  ,[ list( range( 16, 21 ) ) ,list( range( 21, 26 ) ) ,list( range( 26, 31 ) ) ]
                 ] )

print( arr1 )
print()
print( arr1.shape )