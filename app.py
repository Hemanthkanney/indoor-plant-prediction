import pickle
from flask import Flask, render_template, request, redirect, url_for
import numpy as np

# Initialize the Flask application
app = Flask(__name__)

# Load the trained model (assuming it's saved as a .pkl file)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the form
    region = request.form.get('region')
    country = request.form.get('country')
    sunlight = float(request.form.get('sunlight'))
    temperature = float(request.form.get('temperature'))
    soil_type = request.form.get('soil')

    # Example of encoding categorical features (basic hashing method)
    region_encoded = hash(region) % 10  # Simplified encoding
    country_encoded = hash(country) % 10
    soil_type_encoded = hash(soil_type) % 10

    # Create the feature array with 5 values
    input_data = np.array([[sunlight, temperature, soil_type_encoded, region_encoded, country_encoded]])

    # Perform prediction using the trained model
    prediction = model.predict(input_data)

    # Redirect to the result page with inputs and prediction
    return redirect(url_for('result', region=region, country=country, sunlight=sunlight,
                            temperature=temperature, soil=soil_type, prediction=prediction[0]))

@app.route('/result')
def result():
    # Retrieve the data passed from the /predict route
    region = request.args.get('region')
    country = request.args.get('country')
    sunlight = request.args.get('sunlight')
    temperature = request.args.get('temperature')
    soil = request.args.get('soil')
    prediction = request.args.get('prediction')

    # Display the result page with the inputs and prediction
    return render_template('result.html', region=region, country=country, sunlight=sunlight,
                           temperature=temperature, soil=soil, prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
