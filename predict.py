import joblib
from preprocess import extract_features
from send_sms import send_sms  # ✅ Make sure this matches exactly


model = joblib.load('model/rf_model.pkl')

class_labels = ['Healthy', 'Nitrogen Deficiency', 'Phosphorus Deficiency', 'Potassium Deficiency']

prediction =['Healthy', 'Nitrogen Deficiency', 'Phosphorus Deficiency', 'Potassium Deficiency']


fertilizer_advice = {
    'Healthy': 'No deficiency detected. Keep monitoring regularly.',
    'Nitrogen Deficiency': 'Apply Urea or Ammonium Nitrate.',
    'Phosphorus Deficiency': 'Use Single Super Phosphate or DAP.',
    'Potassium Deficiency': 'Apply Muriate of Potash (MOP).'
}

from send_sms import send_sms

def predict_deficiency(image_path):
    features = extract_features(image_path)
    prediction = model.predict([features])[0]
    label = class_labels[prediction]
    advice = fertilizer_advice[label]

    # Compose SMS message
    sms_message = f"Leaf Diagnosis:\nStatus: {label}\nAdvice: {advice}"
    
    # Farmer's phone number (add +91 for India)
    send_sms(sms_message, "9787406985,9655253703")  # Replace with real number

    return label, advice
