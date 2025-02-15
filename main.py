import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split

melbourne_file_path = 'C:/Users/USER/Desktop/Coding/VS Code Projects/Learning ML/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path)
print(melbourne_data.columns)
y = melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = melbourne_data[melbourne_features]
print(X.describe())
print(X.head())

train_X, val_X, train_y, val_y = train_test_split(X, y random_state=0)
melbourne_model= DecisionTreeRegressor(random_state=1)
melbourne_housing.fit(X,y)
print(X.head())
print(melbourne_model.predict(X.head())) 