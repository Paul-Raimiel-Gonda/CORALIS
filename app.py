import os
from flask import Flask, request, jsonify, render_template
from model import predict_coral_health  # Make sure this function is implemented in model.py

# Explicitly tell Flask where the templates folder is
app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'CORALIS', 'templates'))


@app.route('/')
def home():
    # Renders templates/index.html
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Check if the 'image' field is in the form data
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image_file = request.files['image']

    # Check if an actual file was selected
    if image_file.filename == '':
        return jsonify({'error': 'Empty filename'}), 400

    # Call your prediction function (defined in model.py)
    prediction = predict_coral_health(image_file)

    # Return result as JSON
    return jsonify({'result': prediction})

if __name__ == '__main__':
    app.run(debug=True)
