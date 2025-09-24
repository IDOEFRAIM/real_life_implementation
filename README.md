
## Diabetes Risk Assessment Project

# Description

This project allows users to assess their risk of diabetes through an interactive test. It uses Flask to create a simple web interface where users can fill out a questionnaire and receive an estimation of their diabetes risk.



# Features

Web form to input personal information (age, weight, physical activity, family history, etc.).

Automatic calculation of diabetes risk based on submitted data.

Immediate feedback to the user with general recommendations.

User-friendly interface accessible via any web browser.





# Installation

1. Clone the repository:



git clone <YOUR_PROJECT_URL>
cd <PROJECT_FOLDER>

2. Create and activate a virtual environment:



python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

3. Install dependencies:



pip install -r requirements.txt

4. Run the Flask application:



flask run

5. Open your browser and go to: http://127.0.0.1:5000/


# Project Structure

project/
│
├── app.py          # Main Flask application
├── templates/      # HTML templates
│   └── index.html
├── static/         # CSS and JavaScript files
├── model.py        # Diabetes prediction logic
├── requirements.txt
└── README.md




# How to Use

1. Open the main page in your browser.


2. Fill in your personal information in the form.


3. Click "Assess My Risk".


4. View the result and suggested recommendations.




# Technologies

Python 3.x

Flask for the web server

HTML / Bootstrap for the front-end

Diabetes prediction model (based on health data) trained with XGBOOST 



Disclaimer

This project is for educational purposes only. The results are not a substitute for medical diagnosis. If you have concerns about diabetes, consult a healthcare professional.



