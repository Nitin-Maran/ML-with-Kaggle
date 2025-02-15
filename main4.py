import pandas as pd

melbourne_file_path = 'C:/Users/USER/Desktop/Coding/VS Code Projects/Learning ML/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path) 

melbourne_data = melbourne_data.dropna(axis=0)

y = melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 
                        'YearBuilt', 'Lattitude', 'Longtitude']
X = melbourne_data[melbourne_features]

from sklearn.model_selection import train_test_split
train_X, val_X, train_y, val_y = train_test_split(X, y,random_state = 0)

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

forest_model =RandomForestRegressor(random_state=1)
forest_model.fit(train_X,train_y)
melb_predics = forest_model.predict(val_X)
print(mean_absolute_error(val_y, melb_predics))