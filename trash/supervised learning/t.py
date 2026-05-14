import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Data (hours vs marks)
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([30, 40, 50, 65, 80])

# Model
model = LinearRegression()
model.fit(X, y)

# Prediction
pred = model.predict([[6]])
print("Predicted Marks for 6 hours:", pred[0])

# Visualization
plt.scatter(X, y)
plt.plot(X, model.predict(X))
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()