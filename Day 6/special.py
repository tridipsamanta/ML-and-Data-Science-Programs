# ===== IMPORT LIBRARIES =====
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# ===== NUMPY SECTION =====
# Create data using numpy
hours_studied = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
marks = np.array([35, 40, 50, 60, 75])

print("NumPy Mean Marks:", np.mean(marks))
print("NumPy Max Marks:", np.max(marks))

# ===== PANDAS SECTION =====
# Create DataFrame
data = pd.DataFrame({
    "Hours_Studied": hours_studied.flatten(),
    "Marks": marks
})

print("\nPandas DataFrame:")
print(data)

# ===== MATPLOTLIB SECTION =====
plt.figure()
plt.scatter(hours_studied, marks)
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.show()

# ===== SCIKIT-LEARN SECTION =====
# Train Linear Regression Model
model = LinearRegression()
model.fit(hours_studied, marks)

# Prediction
predicted_marks = model.predict(hours_studied)

print("\nPredicted Marks:", predicted_marks)

# ===== VISUALIZE MODEL =====
plt.figure()
plt.scatter(hours_studied, marks)
plt.plot(hours_studied, predicted_marks)
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.title("Linear Regression Model")
plt.show()
