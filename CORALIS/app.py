from flask import Flask, request, jsonify, render_template
from model import predict_coral_health

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image_file = request.files['image']
    if image_file.filename == '':
        return jsonify({'error': 'Empty filename'}), 400

    # Call your model's prediction function
    prediction = predict_coral_health(image_file)

    return jsonify({'result': prediction})

if __name__ == '__main__':
    app.run(debug=True)
