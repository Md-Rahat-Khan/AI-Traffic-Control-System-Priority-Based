import pandas as pd
from sklearn import tree
from sklearn import preprocessing
import numpy as np

#le = preprocessing.LabelEncoder()
df = pd.read_csv('RFID.csv')
#df.head()
print(df)
x = df.drop(columns=['Result'])
#print(x)
inputs = x.drop(columns=['Case No.'])
#inputx = inputs.to_numpy()
#inputy = np.asarray(inputs)
#print(inputy)
#print(inputx)
print(inputs)
#target = df['Result']
target = df['Result']
#targetx =target.to_numpy()
#targety = np.asarray(target)
#print(targety)
#print(targetx)
print(target)

model = tree.DecisionTreeClassifier()
model.fit(inputs, target)

scores = model.score(inputs, target)
print('score:'+str(scores))

a = input('enter 1st roads density between 0-3: ')
b = input('enter 2nd roads density between 0-3: ')
c = input('enter 3rd roads density between 0-3: ')
d = input('enter 4th roads density between 0-3: ')
e = input('Enter RFID number between 0-4: ')

pre = model.predict([[a, b, c, d, e]])
print('output='+str(pre))


