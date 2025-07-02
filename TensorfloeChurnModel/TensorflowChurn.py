import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

# 1. Load the dataset
df = pd.read_csv('C:/Users/j/Desktop/Churn.csv')

# 2. Preprocessing
# Drop customerID (if exists)
if 'customerID' in df.columns:
    df = df.drop('customerID', axis=1)

# Convert target column 'Churn' to 0 and 1
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})
print("Available columns:", df.columns.tolist())


# Handle total charges which may be object due to missing values
df['Total Charges'] = pd.to_numeric(df['Total Charges'], errors='coerce')
df['Total Charges'].fillna(df['Total Charges'].mean(), inplace=True)

# Label encode categorical features
cat_cols = df.select_dtypes(include='object').columns
df[cat_cols] = df[cat_cols].apply(LabelEncoder().fit_transform)

# Separate features and target
X = df.drop('Churn', axis=1)
y = df['Churn']

# Normalize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 3. Build the TensorFlow model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(32, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')  # binary classification
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# 4. Train the model
model.fit(X_train, y_train, epochs=20, batch_size=32, validation_split=0.1)

# 5. Evaluate on test data
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f"\nTest Accuracy: {test_acc:.2f}")

# 6. Save the model
model.save('/mnt/data/churn_model.h5')

# 7. Load the model back
reloaded_model = tf.keras.models.load_model('/mnt/data/churn_model.h5')

# 8. Predict on new samples (optional example using X_test)
predictions = (reloaded_model.predict(X_test) > 0.5).astype(int)
print("Sample Predictions:", predictions[:10].ravel())
