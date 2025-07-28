import numpy as np
import pandas as pd
# from sklearn.base import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

df=pd.read_csv('sai.csv')

df_clean=df.dropna(subset=['Calories'])

x=df_clean[['Duration', 'Pulse', 'Maxpulse' ]].values
y=df_clean['Calories'].values

np.random.seed(42)
indices=np.arange(len(x))
np.random.shuffle(indices)
x=x[indices]
y=y[indices]

split_index=int(0.8*len(x))
x_train, x_test = x[:split_index], x[split_index:]
y_train, y_test = y[:split_index], y[split_index:]

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

model = LinearRegression()
model.fit(x_train_scaled, y_train)

y_pred = model.predict(x_test_scaled)
mse = mean_squared_error(y_test, y_pred)
r2=r2_score(y_test, y_pred)
print("Mean Squared Error:", mse)
print("r2 score:", r2)


duration = float(input("Enter Duration in minutes: "))
pulse = float(input("Enter Pulse: "))
max_pulse = float(input("Enter Max Pulse: "))

input_data = np.array([[duration, pulse, max_pulse]])
input_data_scaled = scaler.transform(input_data)

predicted_calories = model.predict(input_data_scaled)
print("Predicted Calories Burned:", predicted_calories[0])

