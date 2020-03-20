import numpy as np
"""
arr1 = np.array( [ list( range(1, 11, 3) )
                 , list( range(11, 21, 3) )
                 , list( range(21, 31, 3) ) ] )

print( arr1 )
print()
arr1 = np.array( [ list( range(1, 11, 3) )
                 , list( range(11, 21, 3) )
                 , list( range(21, 31, 3) ) ], dtype = np.float64 )
print( arr1 )
print()
arr2 = np.array( [ [6.2, 5.9, 1.9, 2.2]
                 , [8.8, 1.1, 9.6, 2.9]
                 , [ 1, 3.45, 5.43, 4.35 ] ]
                 , dtype = np.int32 )

print( arr2 )
print()
print( arr1 + arr2 )
print()
print( arr1.dtype )
arr1.dtype = np.float16
print()
print( arr1.dtype )
"""

arr1 = np.array( [ list( range(1, 11, 3) )
                 , list( range(11, 21, 3) )
                 , list( range(21, 31, 3) ) ] )

print( arr1 )
print()
print( np.mean( arr1 ) )

mean = np.mean( arr1, axis = 1 )   #Finding mean by row
print( mean )
print()
mean = np.mean( arr1, axis = 0 )   #Finding mean by col
print( mean )
print()
print()
print( np.median( arr1 ) )
print()
print( np.median( arr1, axis= 1 ) )
print()
print( np.median( arr1, axis= 0 ) )
print()
print( np.sum( arr1) )
print()
print( np.sum( arr1, axis = 1 ) )
print()
print( np.sum( arr1, axis = 0 ) )