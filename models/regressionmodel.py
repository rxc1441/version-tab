#!/usr/bin/env python
# coding: utf-8

# # Tabular Regression Prototype – California Housing
#
# # variant of basemodel
#
# ![version project](../src/projects/version/prototypesubmission.png)

# In[1]:

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Set seeds
np.random.seed(578)
tf.random.set_seed(578)

# In[2]:

# Load California Housing dataset
data = fetch_california_housing()
X, y = data.data, data.target

print("Feature names:", data.feature_names)
print("Input shape:", X.shape)
print("Target shape:", y.shape)

# In[3]:

# Train-test split and standardization
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# In[4]:

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

# Define regression model
regressionmodel = Sequential([
    Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
    Dropout(0.3),
    Dense(64, activation='relu'),
    Dropout(0.2),
    Dense(1)  # Linear output for regression
])

regressionmodel.compile(
    optimizer='adam',
    loss='mse',
    metrics=['mae']
)

# In[5]:

# Train
history = regressionmodel.fit(
    X_train, y_train,
    epochs=30,
    batch_size=32,
    validation_split=0.1,
    verbose=1
)

# In[6]:

# Evaluate
loss, mae = regressionmodel.evaluate(X_test, y_test, verbose=0)
print(f"\nTest MSE: {loss:.4f}")
print(f"Test MAE: {mae:.4f}")

# In[7]:

# Predictions and plot
y_pred = regressionmodel.predict(X_test).flatten()

plt.figure(figsize=(6, 6))
sns.scatterplot(x=y_test, y=y_pred, alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], '--', color='red')
plt.xlabel("Actual Median House Value")
plt.ylabel("Predicted Median House Value")
plt.title("True vs. Predicted Values")
plt.grid(True)
plt.tight_layout()
plt.show()

# In[8]:

# Training curve
plt.figure(figsize=(8, 4))
plt.plot(history.history['mae'], label='Train MAE')
plt.plot(history.history['val_mae'], label='Val MAE')
plt.title("Training and Validation MAE")
plt.xlabel("Epoch")
plt.ylabel("Mean Absolute Error")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# In[9]:

# Save model summary
with open("regressionmodel_summary.txt", "w") as f:
    regressionmodel.summary(print_fn=lambda line: f.write(line + "\n"))

print("Model summary saved to regressionmodel_summary.txt")

# In[10]:

# Sanity check on filesystem
import os
from glob import glob

print("Working directory:", os.getcwd())
print("Top-level items:", os.listdir("."))

matches = glob("**/*", recursive=True)
print("All files and folders:")
for item in matches:
    print("  ", item)

# End of regressionmodel demo