import os
import cv2
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib
from preprocess import extract_features

data_dir = 'dataset'

class_map = {
    'Healthy': 0,
    'Nitrogen_Deficiency': 1,
    'Phosphorus_Deficiency': 2,
    'Potassium_Deficiency': 3
}

features = []
labels = []

for label in class_map:
    folder_path = os.path.join(data_dir, label)
    for file in os.listdir(folder_path):
        img_path = os.path.join(folder_path, file)
        try:
            feat = extract_features(img_path)
            features.append(feat)
            labels.append(class_map[label])
        except:
            print(f"⚠️ Skipped: {img_path}")

X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

os.makedirs('model', exist_ok=True)
joblib.dump(model, 'model/rf_model.pkl')
print("✅ Model saved as 'model/rf_model.pkl'")
