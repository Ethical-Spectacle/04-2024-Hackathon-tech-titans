import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib

# Example: training a random forest classifier
df = pd.read_csv("iowa.csv")

df = df[df['crop_name'] != 'Deciduous Forest']
df = df[df['crop_name'] != 'Developed/Open Space']

print(df.shape[0])

# Selecting features for X and y
X = df[['tmin', 'tmax', 'prcp', 'elevation_result']]
y = df['irrigation_result']

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

# # Save the model to a file
# joblib.dump(dt_clf, 'model.joblib')