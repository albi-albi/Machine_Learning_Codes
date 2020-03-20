import pandas as pd

data = pd.read_csv(r'C:\Users\gauta\PycharmProjects\MachineLearning\SuperVised Learning\Topic 17 - XGBoost\Churn_Modelling.csv')

print( data.head() )
print( f"\ndata.columns = { data.columns }" )

x = data.loc[ :, "CreditScore" : "EstimatedSalary" ]
y = data.loc[ :, 'Exited' ]

print()
print( f"x.shape = { x.shape }" )
print()
print( f"\nx.isnull().sum() :- \n{ x.isnull().sum() }" )
print( f"\ny.isnull().sum() :- \n{ y.isnull().sum() }" )

print( f"\nBefore Label Encoder, x.dtypes :- \n{ x.dtypes }" )
print( f"Before Label Encoder, x['Geography'].unique() = { x['Geography'].unique() }" )
print( f"Before Label Encoder, x['Gender'].unique() = { x['Gender'].unique() }" )

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

x['Geography'] = le.fit_transform( x['Geography'] )
x['Gender'] = le.fit_transform( x['Gender'] )

print( f"\nAfter Label Encoder, x.dtypes :- \n{ x.dtypes }" )
print( f"Before Label Encoder, x['Geography'].unique() = { x['Geography'].unique() }" )
print( f"Before Label Encoder, x['Gender'].unique() = { x['Gender'].unique() }" )

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

print( f"\nBefore Standard Scaler, x.head() :- \n{ x.head() }" )
x = sc.fit_transform( x )
print( f"\nAfter Standard Scaler, x :- \n{ x }" )

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split( x, y, test_size = 0.2 )

from xgboost import XGBRFClassifier
xgboost = XGBRFClassifier()

xgboost.fit( x_train, y_train )
y_pred = xgboost.predict( x_test )

print( f"xgboost.score( x_test, y_test ) = { xgboost.score( x_test, y_test ) * 100 }%" )

import matplotlib.pyplot as plt

plt.plot( x_test, y_test, label = 'Actual', marker = '*', color = 'blue', linestyle = '' )
plt.plot( x_test, y_pred, label = 'Prediction', marker = '+', color = 'red', linestyle = '' )
plt.legend()
plt.xlabel( 'x_test' )
plt.ylabel( 'y_test V/s y_pred' )
plt.title( 'XGBOOST' )
plt.show()