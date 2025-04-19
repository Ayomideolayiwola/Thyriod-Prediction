import streamlit as st
import pandas as pd
import pickle
import sklearn

# Load trained model
with open("thyroid_pred_model.pkl", "rb") as file:
    model = pickle.load(file)


st.set_page_config(page_title="Thyroid Recurrence Predictor")
st.title("🧠 Thyroid Disease Recurrence Predictor")
st.markdown("Enter the encoded patient data to predict **recurrent thyroid disease**.")


# Input fields for all features
with st.form("Thyroid_Form"):
    Age = st.number_input("Age (choose between 15 to 85)", min_value=15, max_value=82)
    Gender = st.selectbox("gender (0 = Female, 1 = Male)", [0, 1])
    Smoking = st.selectbox("smoking (0 = No, 1 = Yes)", [0, 1])
    Hx_Smoking = st.selectbox("Hx_Smoking (0 = No, 1 = Yes)", [0, 1])
    Hx_Radiothreapy = st.selectbox("Hx_Radiothreapy (0 = No, 1 = Yes)", [0, 1])
    Thyroid_Function = st.selectbox("Thyroid_Function (0 = Clinical Hyperthyrodism, 1 = Clinical Hypothyrodism ,"
                                    " 2 = Euthyroid, 3 = Subclinical Hyperthyrodism, 4 = Subclinical Hypothyrodism) ",
                                    [0, 1, 2, 3, 4])
    Physical_Examination = st.selectbox("Physical_Examination (0 = Diffuse goiter, 1 = Multinodular goiter,  "
                                        "2 = Normal, 3 = Single nodular goiter-left, 4 = Single nodular goiter-right)",
                                        [0, 1, 2, 3, 4])
    Pathology = st.selectbox("pathology (0 = Follicular, 1 = Hurthel cell, 2 = Micropapillary, 3 = Papillary)",
                             [0, 1, 2, 3])
    Adenopathy = st.selectbox("adenopathy (0 = Bilateral, 1 = Extensive, 2 = Left, 3 = No, 4 = Posterior,  5 = Right)",
                              [0, 1, 2, 3, 4, 5])
    Focality = st.selectbox("focality (0 = Multi-Focal, 1 = Uni-Focal )", [0, 1])
    T_Stage = st.selectbox("T_stage (0 = T1a, 1 = T1b, 2 = T2, 3 = T3a, 4 = T3b, 5 = T4a, 6 = T4b)", [0, 1, 2, 3, 4, 5, 6])
    N_Stage = st.selectbox("N_stage (0 = N0, 1 = N1a, 2 = N1b )", [0, 1, 2])
    M_Stage = st.selectbox("M_stage (0 = M0, 1 = M1)", [0, 1])
    Stage = st.selectbox("stage (0 = I, 2 = IVA, 3 = III, 4 = IVB, 5 = II)", [0, 1, 2, 3, 4])
    Response = st.selectbox("response (0 = Biochemical Incomplete, 1 = Excellent, 2 = Indeterminate,"
                            "  3 = Structural Incomplete)", [0, 1, 2, 3])
    Risk = st.selectbox("risk (0 = High, 1 = Intermediate, 2 = Low)", [0, 1, 2])

    submitted = st.form_submit_button("Predict")

# Make prediction
if submitted:
    input_data = {
        "Age": [Age],
        "gender": [Gender],
        "smoking": [Smoking],
        "Hx_Smoking": [Hx_Smoking],
        "Hx_Radiothreapy": [Hx_Radiothreapy],
        "Thyroid_Function": [Thyroid_Function],
        "Physical_Examination": [Physical_Examination],
        "pathology": [Pathology],
        "adenopathy": [Adenopathy],
        "focality": [Focality],
        "T_stage": [T_Stage],
        "N_stage": [N_Stage],
        "M_stage": [M_Stage],
        "stage": [Stage],
        "response": [Response],
        "risk": [Risk]
    }

    input_df = pd.DataFrame(input_data)

    prediction = model.predict(input_df)[0]

    if prediction == 1:
        st.error("🚨 The patient is likely to experience a recurrence of thyroid disease.")
    else:
        st.success("✅ The patient is NOT likely to have a recurrence.")


