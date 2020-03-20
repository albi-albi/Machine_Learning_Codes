import pandas as pd

data = pd.read_csv(r'C:\Users\gauta\PycharmProjects\MachineLearning\Un-SuperVised Learning\Topic 18 - Apriori\Market_Basket_Optimisation.csv', header = None)
print( data.head() )

print( f"len( data.index ) = { len( data.index ) }" )
print( f"len( data.columns ) = { len( data.columns ) }" )

transactions = []

for i in range( len( data.index ) ):          #row 0 to 7500\n
    temp = []
    for j in range( len(data.columns) ):  # For each row, all columns."
        temp.append( str(data[j][i]) )      #Appending [col][row] -> Select any row and then, append all col. data for that row.

    transactions.append( temp )

print( f"len( transactions ) = { len( transactions ) }" )
print( f"transactions[10] = { transactions[10] }" )

import sys
sys.path.append( r'C:\Users\gauta\PycharmProjects\MachineLearning\Un-SuperVised Learning\Topic 18 - Apriori\apyori_Algorithm' )

from apyori_Algorithm import apriori

"""
So, Min_support = least total product sold/ Total no. of given days
5*7/7500 : Any product which is on sale 5 times per day. 
So, we are calculating the least total product sold in a week.

Confidence is the desired accuracy rate. If 0.3 then, The prediction must be 30%,
min_lift must be 3 or more . min_lift = min_confidence/ min_support. Then, min_confidence should be high,
min_length is minimum product threshold value -> how many product is max to max allowed in the apriori.
"""
ap = apriori( transactions, min_support = 0.004666666666666667, min_confidence = 0.2, min_lift = 3, min_length = 3 )

print( ap )

result = list(ap)

print( f"result = { result }" )

for i in result:
    print(f"i = {i} and len(i) = { len(i) }" )
    print()

for i in result:
    for j in i:
        print( j, end=' -> ' )

    print()

for i in result:
    print( i[2] )
    print()
