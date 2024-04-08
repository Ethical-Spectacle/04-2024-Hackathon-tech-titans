import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def calculation(location,landsize):
    
    df = pd.read_csv("iowa.csv")

    # Selecting features for X and y
    X = df[['tmin', 'tmax', 'prcp', 'elevation_result']]
    y = df['cropland']

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize the DecisionTreeClassifier
    dt_clf = DecisionTreeClassifier(random_state=42)

    # Fit the model on the training data
    dt_clf.fit(X_train, y_train)

    # Make predictions
    y_pred = dt_clf.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print("Decision Tree Accuracy:", accuracy)

    landsize = int(landsize)
    iowa_agriculture_data = {
    '50301': { 'irrigation': landsize*678856, 'suggested_crop': 'corn', 'estimated_costs': '4.34 ', 'irrigation_costs':'1.302 ', 'material_cost':'3.038 ', 'yield':'203 ','income':'4.72 '},
    '50302': { 'irrigation': landsize*543085, 'suggested_crop': 'soybeans', 'estimated_costs': '11.87 ', 'irrigation_costs':'2.96 ', 'material_cost':'8.90 ', 'yield':'58.5 ','income':'11.81 '},
    '50304': { 'irrigation': landsize*8100, 'suggested_crop': 'wheat', 'estimated_costs': '0.46 ', 'irrigation_costs':'1.302 ', 'material_cost':'3.038 ','yield':'203 ','income':'4.72 ' },
    '50305': { 'irrigation': landsize*502354, 'suggested_crop': 'oats', 'estimated_costs': '3.6600 ', 'irrigation_costs':'1.302 ', 'material_cost':'3.038 ','yield':'80 ','income':'6.71 ' },
    '50306': { 'irrigation': landsize*5400, 'suggested_crop': 'barley', 'estimated_costs': '5.10 ', 'irrigation_costs':'1.302 ', 'material_cost':'3.038 ','yield':'203 ','income':'4.72 ' },
    '50307': { 'irrigation': landsize*4000, 'suggested_crop': 'rye', 'estimated_costs': '339 ', 'irrigation_costs':'1.302 ', 'material_cost':'3.038 ','yield':'203 ','income':'4.72 ' },
    '50308': { 'irrigation': landsize*5500, 'suggested_crop': 'rice', 'estimated_costs': '4.56 ', 'irrigation_costs':'1.302 ', 'material_cost':'3.038 ','yield':'203 ','income':'4.72 ' },
    '50309': { 'irrigation': landsize*8500, 'suggested_crop': 'sorghum', 'estimated_costs': '1.34 ', 'irrigation_costs':'1.302 ', 'material_cost':'3.038 ','yield':'203 ','income':'4.72 ' },
    '50310': { 'irrigation': landsize*6500, 'suggested_crop': 'sunflowers', 'estimated_costs': ' 1.96 ', 'irrigation_costs':'1.302 ', 'material_cost':'3.038 ','yield':'203 ','income':'4.72 '},
    '50311': { 'irrigation': landsize*393737, 'suggested_crop': 'canola', 'estimated_costs': '1.28 ', 'irrigation_costs':'0.256 ', 'material_cost':'1.024 ','yield':'203 ','income':'4.72 ' },
    '50312': { 'irrigation': landsize*8000, 'suggested_crop': 'flaxseed', 'estimated_costs': '1.68 ', 'irrigation_costs':'0.336 ', 'material_cost':'3.038 ','yield':'203 ','income':'4.72 ' },
    # ... more ZIP codes and data as needed ...
    }

    pin_data = iowa_agriculture_data[location]
    irrigation_water = pin_data['irrigation']
    suggested_crop = pin_data['suggested_crop']
    estimated_costs = pin_data['estimated_costs']
    irrigation_costs = pin_data['irrigation_costs']
    material_cost = pin_data['material_cost']
    total_yield = pin_data['yield']
    income = pin_data['income']

    return irrigation_water, suggested_crop, estimated_costs, irrigation_costs, material_cost, total_yield, income

