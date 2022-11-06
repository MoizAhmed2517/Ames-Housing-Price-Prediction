import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error


df = pd.read_csv('Advertising.csv')

X = df.drop(columns='sales')
y = df['sales']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=101, test_size=0.3 )
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

model = Ridge(alpha=1)
score = cross_val_score(model, X_train, y_train, cv=5, scoring='neg_mean_squared_error')
print(abs(score.mean()))

model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(mean_squared_error(y_test, y_pred))

