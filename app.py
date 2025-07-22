from flask import Flask, request, render_template
from predict import predict_deficiency
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']
    if file.filename == '':
        return "No selected file"

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    result, advice = predict_deficiency(filepath)
    return render_template('result.html', result=result, advice=advice, image_path=filepath)

if __name__ == '__main__':
    app.run(debug=True)
