import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

melbourne_file_path = 'C:/Users/USER/Desktop/Coding/VS Code Projects/Learning ML/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path)
print(melbourne_data.columns)
y = melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = melbourne_data[melbourne_features]
print(X.describe())
print(X.head())

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)
melbourne_model= DecisionTreeRegressor()
melbourne_housing.fit(train_X, train_y)

val_predictions = melbourne_model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))