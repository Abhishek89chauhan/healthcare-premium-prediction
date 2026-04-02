

import streamlit as st
from prediction_helper import predict

st.set_page_config(
    page_title="Health Insurance Premium Predictor",
    layout="wide",
)

st.markdown(
    """
    <style>
        .stApp {
            background:
                radial-gradient(circle at top left, rgba(59, 130, 246, 0.22) 0%, rgba(59, 130, 246, 0) 34%),
                radial-gradient(circle at top right, rgba(6, 182, 212, 0.18) 0%, rgba(6, 182, 212, 0) 28%),
                linear-gradient(180deg, #020617 0%, #0f172a 45%, #111827 100%);
        }

        .block-container {
            padding-top: 0;
            padding-bottom: 3rem;
            max-width: 1180px;
        }

        .hero-section {
            padding: 4.5rem 2rem;
            margin: 0 0 2rem 0;
            border-radius: 0 0 28px 28px;
            background: linear-gradient(135deg, #0f766e 0%, #0ea5a4 45%, #67e8f9 100%);
            color: #ffffff;
            text-align: center;
            box-shadow: 0 24px 55px rgba(15, 118, 110, 0.20);
        }

        .hero-section h1 {
            margin: 0;
            font-size: 3rem;
            font-weight: 700;
            letter-spacing: -0.03em;
        }

        .hero-section p {
            margin: 1rem auto 0 auto;
            max-width: 760px;
            font-size: 1.08rem;
            line-height: 1.7;
            color: rgba(255, 255, 255, 0.92);
        }

        .section-shell {
            background: rgba(15, 23, 42, 0.82);
            border: 1px solid rgba(148, 163, 184, 0.18);
            border-radius: 24px;
            padding: 1.6rem;
            box-shadow: 0 20px 45px rgba(2, 6, 23, 0.35);
            backdrop-filter: blur(10px);
        }

        .section-title {
            font-size: 1.25rem;
            font-weight: 700;
            color: #f8fafc;
            margin-bottom: 0.35rem;
        }

        .section-copy {
            color: #cbd5e1;
            margin-bottom: 1.25rem;
        }

        .result-card {
            padding: 2rem;
            border-radius: 24px;
            background: linear-gradient(135deg, rgba(12, 74, 110, 0.42) 0%, rgba(15, 23, 42, 0.92) 100%);
            border: 1px solid rgba(103, 232, 249, 0.18);
            box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.06), 0 18px 40px rgba(8, 47, 73, 0.28);
        }

        .result-label {
            font-size: 0.95rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: #67e8f9;
            margin-bottom: 0.5rem;
        }

        .result-value {
            font-size: 2.7rem;
            font-weight: 800;
            color: #f8fafc;
            line-height: 1.15;
            margin: 0;
        }

        .result-help {
            margin-top: 0.85rem;
            color: #cbd5e1;
            font-size: 1rem;
        }

        div[data-testid="stForm"] {
            border: none;
            padding: 0;
            background: transparent;
        }

        div[data-testid="stNumberInput"] label,
        div[data-testid="stSelectbox"] label,
        div[data-testid="stNumberInput"] label p,
        div[data-testid="stSelectbox"] label p {
            color: #e2e8f0 !important;
            font-weight: 600 !important;
            opacity: 1 !important;
        }

        div[data-testid="stNumberInput"] input,
        div[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
            background: rgba(15, 23, 42, 0.92) !important;
            color: #f8fafc !important;
            border: 1px solid rgba(148, 163, 184, 0.28) !important;
        }

        div[data-testid="stNumberInput"] button {
            color: #f8fafc !important;
        }

        .stButton > button,
        div[data-testid="stFormSubmitButton"] > button {
            width: 100%;
            min-height: 3rem;
            border-radius: 999px;
            border: none;
            background: linear-gradient(135deg, #0f766e 0%, #14b8a6 100%);
            color: #ffffff;
            font-weight: 700;
            box-shadow: 0 16px 30px rgba(20, 184, 166, 0.25);
        }
    </style>
    """,
    unsafe_allow_html=True,
)

if "prediction_result" not in st.session_state:
    st.session_state.prediction_result = None

with st.container():
    st.markdown(
        """
        <div class="hero-section">
            <h1>Health Insurance Premium Predictor</h1>
            <p>
                Estimate your annual health insurance premium with a clean, modern interface.
                Adjust the profile details below and generate updated predictions anytime.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

categorical_options = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer', ''],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': [
        'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
        'Thyroid', 'Heart disease', 'High blood pressure & Heart disease', 'Diabetes & Thyroid',
        'Diabetes & Heart disease'
    ],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}

with st.container():
    st.markdown('<div class="section-shell">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Input Details</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-copy">Fill in the existing profile fields below and submit to view the annual premium amount.</div>',
        unsafe_allow_html=True,
    )

    with st.form("premium_prediction_form", clear_on_submit=False):
        row1 = st.columns(3)
        row2 = st.columns(3)
        row3 = st.columns(3)
        row4 = st.columns(3)

        with row1[0]:
            age = st.number_input('Age', min_value=18, step=1, max_value=100)
        with row1[1]:
            number_of_dependants = st.number_input('Number of Dependants', min_value=0, step=1, max_value=20)
        with row1[2]:
            income_lakhs = st.number_input('Income in Lakhs', step=1, min_value=0, max_value=200)

        with row2[0]:
            genetical_risk = st.number_input('Genetical Risk', step=1, min_value=0, max_value=5)
        with row2[1]:
            insurance_plan = st.selectbox('Insurance Plan', categorical_options['Insurance Plan'])
        with row2[2]:
            employment_status = st.selectbox('Employment Status', categorical_options['Employment Status'])

        with row3[0]:
            gender = st.selectbox('Gender', categorical_options['Gender'])
        with row3[1]:
            marital_status = st.selectbox('Marital Status', categorical_options['Marital Status'])
        with row3[2]:
            bmi_category = st.selectbox('BMI Category', categorical_options['BMI Category'])

        with row4[0]:
            smoking_status = st.selectbox('Smoking Status', categorical_options['Smoking Status'])
        with row4[1]:
            region = st.selectbox('Region', categorical_options['Region'])
        with row4[2]:
            medical_history = st.selectbox('Medical History', categorical_options['Medical History'])

        submitted = st.form_submit_button('Predict Premium')
    st.markdown('</div>', unsafe_allow_html=True)

# Create a dictionary for input values
input_dict = {
    'Age': age,
    'Number of Dependants': number_of_dependants,
    'Income in Lakhs': income_lakhs,
    'Genetical Risk': genetical_risk,
    'Insurance Plan': insurance_plan,
    'Employment Status': employment_status,
    'Gender': gender,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Region': region,
    'Medical History': medical_history
}

if submitted:
    st.session_state.prediction_result = predict(input_dict)

st.markdown("<div style='height: 1.5rem;'></div>", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="section-shell">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Annual Premium Amount</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-copy">Your latest prediction will appear here after you submit the form.</div>',
        unsafe_allow_html=True,
    )

    if st.session_state.prediction_result is not None:
        st.markdown(
            f"""
            <div class="result-card">
                <div class="result-label">Predicted Annual Premium</div>
                <p class="result-value">INR {st.session_state.prediction_result:,}</p>
                <div class="result-help">Update any inputs above and click Predict Premium again to refresh this amount.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <div class="result-card">
                <div class="result-label">Prediction Pending</div>
                <p class="result-value">Enter details above</p>
                <div class="result-help">The calculated annual premium amount will be displayed here once you submit the form.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown('</div>', unsafe_allow_html=True)
