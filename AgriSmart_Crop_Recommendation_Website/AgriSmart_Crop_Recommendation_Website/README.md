# AgriSmart: Crop Recommendation Website

A Flask-based student project prototype for the agriculture sector. It collects soil nutrient and weather inputs and displays an illustrative crop suggestion.

## Features
- Responsive website built with HTML and CSS
- Flask routes and form handling
- Inputs for nitrogen, phosphorus, potassium, temperature, humidity, pH, and rainfall
- Basic rule-based demonstration recommendation
- About page explaining the project modules

## Important limitation
The current recommendation logic is **rule-based demonstration code**, not a trained machine-learning model. Its ranges are illustrative and are not suitable for real farming decisions. Do not present its output as a validated agricultural recommendation.

## Run locally
1. Install Python 3.10 or newer.
2. Open a terminal in this project folder.
3. Create and activate a virtual environment (recommended).
4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Start the application:

   ```bash
   python app.py
   ```

6. Open `http://127.0.0.1:5000` in your browser.

## Project structure
```text
agriculture_ai_project/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│   ├── index.html
│   └── about.html
└── static/
    ├── style.css
    └── uploads/
```

## Future work
- Obtain a trustworthy, documented crop recommendation dataset.
- Train and evaluate a classifier using a proper train/test split.
- Report accuracy, precision, recall, F1-score, and confusion matrix.
- Validate predictions with agricultural experts and local conditions.
- Add dataset citations and model limitations to the report.
