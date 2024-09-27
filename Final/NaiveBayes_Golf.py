# Supervised learning classification task code

import pandas as pd  # Read Data from CSV file
from sklearn.preprocessing import LabelEncoder  # Preprocess the data
# Split the Data Set: Training Set(<=70%), Test Set(>=30%)
from sklearn.model_selection import train_test_split
# Train The Model using Training Set and a Machine Learning   Algorithm (Ex: Naïve Bayes)
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics


# Import Data
data = pd.read_csv('golf.csv')
print(data)


# Preprocess Data
number = LabelEncoder()
data['Outlook'] = number.fit_transform(data['Outlook'])
data['Temperature'] = number.fit_transform(data['Temperature'])
data['Humidity'] = number.fit_transform(data['Humidity'])
data['Windy'] = number.fit_transform(data['Windy'])
data['Play'] = number.fit_transform(data['Play'])

print("\n\nAfter Preprocessing: ")
print(data)


# Split Data
feature = ['Outlook', 'Temperature', 'Humidity', 'Windy']
target = 'Play'
X_train, X_test, Y_train, Y_test = train_test_split(
    data[feature], data[target], test_size=0.3, random_state=1)


# Train the model
model = GaussianNB()
model.fit(X_train, Y_train)


# Test the model
Y_pred = model.predict(X_test)
print("Y_test")
print(Y_test)
print("Y_Pred")
print(Y_pred)
print("\nAccuracy: ", metrics.accuracy_score(Y_test, Y_pred))
