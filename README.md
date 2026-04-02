# Healthcare Premium Prediction

This project is a Streamlit web app that predicts annual health insurance premiums from user profile details such as age, dependants, income, smoking habits, BMI category, medical history, and insurance plan.

The app uses two pre-trained models stored in the `artifacts/` directory:

- A `LinearRegression` model for younger applicants (`age <= 25`)
- An `XGBRegressor` model for all other applicants

## Features

- Interactive Streamlit interface with a modern styled layout
- Annual premium prediction based on personal and medical profile inputs
- Automatic preprocessing for categorical and numeric features
- Separate scaling and model selection logic based on applicant age
- Ready-to-run serialized model and scaler artifacts included in the repository

## Project Structure

```text
healthcare-premium-prediction/
|-- artifacts/
|   |-- model_rest.joblib
|   |-- model_young.joblib
|   |-- scaler_rest.joblib
|   `-- scaler_young.joblib
|-- main.py
|-- prediction_helper.py
|-- README.md
|-- requirements.txt
`-- LICENSE
```

## Tech Stack

- Python
- Streamlit
- Pandas
- Joblib
- Scikit-learn
- XGBoost

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/healthcare-premium-prediction.git
cd healthcare-premium-prediction
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the App

Start the Streamlit app with:

```bash
streamlit run main.py
```

After the server starts, open the local URL shown in the terminal, usually:

```text
http://localhost:8501
```

## Input Fields

The app expects the following user inputs:

- Age
- Number of Dependants
- Income in Lakhs
- Genetical Risk
- Insurance Plan
- Employment Status
- Gender
- Marital Status
- BMI Category
- Smoking Status
- Region
- Medical History

## How Prediction Works

1. The Streamlit form collects profile information from the user.
2. `prediction_helper.py` converts the inputs into the expected model feature format.
3. Medical history is transformed into a normalized risk score.
4. The appropriate scaler is chosen based on age.
5. The app selects the young-age model or the general model and returns the predicted annual premium.

## Model Artifacts

The repository already includes the trained artifacts required for inference:

- `artifacts/model_young.joblib`
- `artifacts/model_rest.joblib`
- `artifacts/scaler_young.joblib`
- `artifacts/scaler_rest.joblib`

No retraining step is required to run the application.

## Notes

- Premium values are displayed in INR.
- This project is intended for educational and portfolio use.
- Predictions depend on the quality and training scope of the saved models.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
