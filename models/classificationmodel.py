# classificationmodel.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import classification_report, confusion_matrix

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Dense, Dropout
from tensorflow.keras.optimizers import Adam

# Load and clean data
df = pd.read_csv("../data/housing-activity.csv").dropna()

def classify_market(row):
    if row['Sales YoY%'] > 10 and row['Months Inventory'] < 2.5:
        return 'hot'
    elif row['Sales YoY%'] < -5 or row['Months Inventory'] > 6:
        return 'cold'
    else:
        return 'stable'

df['MarketLabel'] = df.apply(classify_market, axis=1)

# Encode target labels
le = LabelEncoder()
y = le.fit_transform(df['MarketLabel'])

X = df[['Sales YoY%', 'Dollar Volume YoY%', 'Months Inventory']]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=578)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Build classifier model
classifier_model = Sequential([
    Input(shape=(X_train.shape[1],)),
    Dense(64, activation='relu'),
    Dropout(0.2),
    Dense(len(le.classes_), activation='softmax')
])

classifier_model.compile(optimizer=Adam(), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train
history = classifier_model.fit(
    X_train, y_train,
    epochs=20,
    batch_size=16,
    validation_split=0.1,
    verbose=1
)

# Predict and evaluate
y_pred_probs = classifier_model.predict(X_test)
y_pred_labels = le.inverse_transform(np.argmax(y_pred_probs, axis=1))
y_test_labels = le.inverse_transform(y_test)

# Print classification report
print(classification_report(y_test_labels, y_pred_labels))

# Confusion matrix
cm = confusion_matrix(y_test_labels, y_pred_labels, labels=le.classes_)
plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=le.classes_, yticklabels=le.classes_)
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.tight_layout()
plt.show()

# Accuracy/loss plots
plt.figure()
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Val Accuracy')
plt.title("Training Accuracy Curve")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure()
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Val Loss')
plt.title("Training Loss Curve")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Print model summary to stdout
classifier_model.summary()

# Save model summary to file
with open("classificationmodel_summary.txt", "w") as f:
    classifier_model.summary(print_fn=lambda line: f.write("[Classifier] " + line + "\n"))

print("Model summary saved to classificationmodel_summary.txt")
