import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np

df = pd.read_csv('RFID.csv')
print(df)

x = df.drop(columns=['Result'])
inputs = x.drop(columns=['Case No.'])
print(inputs)

target = df['Result']
print(target)

# Split the data into 70% training and 30% testing
X_train, X_test, y_train, y_test = train_test_split(inputs, target, test_size=0.3, random_state=42)

# Create and train Random Forest Classifier with enhanced hyperparameters
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    min_samples_split=5,
    min_samples_leaf=2,
    random_state=42
)
model.fit(X_train, y_train)

# Calculate scores on both training and test sets
train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)

print('Training score: '+str(train_score))
print('Testing score: '+str(test_score))

a = input('enter 1st roads density between 0-3: ')
b = input('enter 2nd roads density between 0-3: ')
c = input('enter 3rd roads density between 0-3: ')
d = input('enter 4th roads density between 0-3: ')
e = input('Enter RFID number between 0-4: ')

pre = model.predict([[a, b, c, d, e]])
print('output='+str(pre))
