import numpy as np

# Read CSV file
f = open("C:/python/cholesterol_data.csv")
h = f.readline()
lines = f.readlines()

# Prepare lists
age, gender, bmi, smoking, activity = [], [], [], [], []
fatintake, alcohol, familyhistory, diabetes, cholesterol = [], [], [], [], []

# Read each line
for line in lines:
    w = line.strip().split(',')
    age.append(int(w[0]))
    gender.append(int(w[1]))
    bmi.append(float(w[2]))
    smoking.append(int(w[3]))
    activity.append(int(w[4]))
    fatintake.append(float(w[5]))
    alcohol.append(float(w[6]))
    familyhistory.append(int(w[7]))
    diabetes.append(float(w[8]))
    cholesterol.append(float(w[9]))

# Prepare feature matrix (X) and target (y)
ones = np.ones(len(lines))
x = np.c_[ones, age, gender, bmi, smoking, activity, fatintake, alcohol, familyhistory, diabetes]
y = np.array(cholesterol).reshape(len(lines), 1)

# Linear regression using normal equation
xt = x.T
xtx = np.dot(xt, x)
xtxinv = np.linalg.inv(xtx)
xty = np.dot(xt, y)
beta = xtxinv.dot(xty)

# Coefficients
b0, b1, b2, b3, b4, b5, b6, b7, b8, b9 = beta.flatten()

# Predictions and accuracy
ycap = []
for v in x:
    pred = (b0 + b1*v[1] + b2*v[2] + b3*v[3] + b4*v[4] + b5*v[5] +
            b6*v[6] + b7*v[7] + b8*v[8] + b9*v[9])
    ycap.append(pred)

# Accuracy calculation
pcnt = 0
for actual, predicted in zip(cholesterol, ycap):
    diff_percent = ((actual - predicted) * 100) / actual
    if -5 <= diff_percent <= 5:
        pcnt += 1

n = len(cholesterol)
accuracy = (pcnt * 100) / n
print(f"The accuracy of the model: {accuracy:.2f}%")
