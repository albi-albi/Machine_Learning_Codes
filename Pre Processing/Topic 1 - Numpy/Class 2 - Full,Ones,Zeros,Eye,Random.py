import numpy as np


#Syntax :- np.full( shape, value )
arr = np.full( ( 2, 5 ), 3 )
print( arr )

print()
#Syntax :- np.zeros( shape )
arr = np.zeros( ( 2, 5 ) )
print( f"arr = { arr }, type( arr) = { type( arr ) } and arr.dtype = { arr.dtype }" )

print()
#Syntax :- np.ones( shape )
arr = np.ones( ( 2, 5 ) )
print( f"arr = { arr }, type( arr) = { type( arr ) } and arr.dtype = { arr.dtype }" )

print()
#Syntax :- np.ones( shape1, shape2 )
arr = np.eye( 5, 5 )
print( f"{ arr }, type( arr) = { type( arr ) } and arr.dtype = { arr.dtype }" )

print()
#Syntax :- np.random.random( shape )
arrrandom = np.random.random( (2, 4, 3) )
print( arrrandom )

#Syntax :- np.random.randint( start, end, shape )
n1 = np.random.randint( 2, 10, 4 )
n2 = np.random.randint( 12, 20, 4 )
n3 = np.random.randint( 12, 20, ( 2, 5 ) )

print( f"n1 = { n1 }" )
print( f"n2 = { n2 }" )
print( f"n3 = { n3 }" )