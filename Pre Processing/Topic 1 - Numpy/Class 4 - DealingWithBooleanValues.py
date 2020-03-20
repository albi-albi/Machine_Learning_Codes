import numpy as np

"""
arr = np.array( [ list( range(0, 10, 3) )
                , list( range(10, 20, 3) )
                , list( range(20, 30, 3) ) ] )

print( arr )
print()

new_arr1 = arr > 15
print( new_arr1 )
print()

# new_arr1 = arr>15
# print( new_arr1 )
# print()
print()
new_arr1 = arr[ new_arr1 ]
print( new_arr1 )

temp = new_arr1 < 25
print( temp )
print()

new_arr1 = new_arr1[temp]
print( new_arr1 )
"""

arr = np.array( [ list( range(0, 10, 3) )
                , list( range(10, 20, 3) )
                , list( range(20, 30, 3) ) ] )

print( arr )
print()
new_arr1 = arr[ arr>15 ]
print( new_arr1 )
print()
print( new_arr1[ new_arr1 < 26 ] )
print()
print( arr[ arr%2 == 0 ] )
print()
print( arr + 2 )
print()
print( arr - 2 )
print()
print( arr * 2 )
print()
print( arr / 2 )
print()