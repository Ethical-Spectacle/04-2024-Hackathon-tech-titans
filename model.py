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

    iowa_agriculture_data = {
    '50301': { 'irrigation': 'drip', 'suggested_crop': 'corn', 'estimated_costs': 500 },
    '50302': { 'irrigation': 'sprinkler', 'suggested_crop': 'soybeans', 'estimated_costs': 450 },
    '50303': { 'irrigation': 'flood', 'suggested_crop': 'alfalfa', 'estimated_costs': 600 },
    '50304': { 'irrigation': 'center pivot', 'suggested_crop': 'wheat', 'estimated_costs': 550 },
    '50305': { 'irrigation': 'subsurface', 'suggested_crop': 'oats', 'estimated_costs': 400 },
    # Add more pin codes and data as needed
    }

    pin_data = iowa_agriculture_data[location]
    irrigation_type = pin_data['irrigation']
    suggested_crop = pin_data['suggested_crop']
    estimated_costs = int(pin_data['estimated_costs']) * int(landsize)
    print(int(pin_data['estimated_costs']) * landsize)


    return irrigation_type, suggested_crop, estimated_costs

