
### **README.md**

```markdown
# Indoor Plant Prediction Web Application

This Flask web application predicts the most suitable indoor plant based on user-provided environmental factors such as sunlight hours, temperature, region, country, and soil type. The model is built using machine learning techniques and can be used to provide personalized plant recommendations based on these inputs.

## Features
- Predicts the most suitable indoor plant based on various environmental factors.
- Takes user input for sunlight, temperature, soil type, region, and country.
- Displays prediction results on a separate results page.
- Uses a pre-trained machine learning model to make predictions.

## Technologies Used
- Python
- Flask (Web Framework)
- scikit-learn (for machine learning model)
- HTML/CSS (Frontend)
- NumPy (for data handling)

## Installation

Follow these steps to run the application locally:

### 1. Clone the repository

```bash
git clone https://github.com/your-username/indoor-plant-prediction.git
cd indoor-plant-prediction
```

### 2. Install dependencies

Create a virtual environment (optional but recommended) and install the required libraries:

```bash
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate  # For Windows
pip install -r requirements.txt
```

### 3. Prepare the model

Ensure you have a pre-trained machine learning model saved as `model.pkl` in the root directory of the project. If you do not have a model, you can train one based on your dataset and save it using the following code:

```python
import pickle
from sklearn.neighbors import KNeighborsClassifier

# Sample model training code
X = # Your feature data here
y = # Your target data here
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

# Save the model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
```

### 4. Run the application

Once the dependencies are installed and the model is in place, run the Flask application:

```bash
python app.py
```

The application will start running on `http://127.0.0.1:5000/` by default.

### 5. Access the application

Open your web browser and navigate to `http://127.0.0.1:5000/`. You will see a form where you can enter details like sunlight, temperature, soil type, region, and country. After submitting the form, you will be redirected to a page displaying the prediction.

## Project Structure

```
indoor-plant-prediction/
├── app.py                  # Flask application code
├── model.pkl               # Trained machine learning model
├── templates/
│   ├── index.html          # Input form template
│   └── result.html         # Result display template
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## Requirements

- Python 3.x
- Flask
- scikit-learn
- NumPy

You can install the required dependencies by running:

```bash
pip install -r requirements.txt
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- **Kanney Sai Hemanth**  
  [Hemanthkanney](https://github.com/Hemanthkanney)



