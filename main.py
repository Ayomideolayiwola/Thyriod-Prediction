import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="Thyroid Recurrence Predictor")

# Load trained model
with open("thyroid_pred_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🧠 Thyroid Disease Recurrence Predictor")
st.markdown("Enter the patient data to predict **recurrent thyroid disease**.")

with st.form("Thyroid_Form"):
    Age = st.number_input("Age", min_value=15, max_value=82, value=None, placeholder="Enter age")

    gender_map = {"Select": None, "Female": 0, "Male": 1}
    Gender = gender_map[st.selectbox("Gender", list(gender_map.keys()))]

    smoking_map = {"Select": None, "No": 0, "Yes": 1}
    Smoking = smoking_map[st.selectbox("Smoking", list(smoking_map.keys()))]

    Hx_Smoking = smoking_map[st.selectbox("History of Smoking", list(smoking_map.keys()))]

    Hx_Radiothreapy = smoking_map[st.selectbox("History of Radiotherapy", list(smoking_map.keys()))]

    thyroid_map = {
        "Select": None,
        "Clinical Hyperthyroidism": 0,
        "Clinical Hypothyroidism": 1,
        "Euthyroid": 2,
        "Subclinical Hyperthyroidism": 3,
        "Subclinical Hypothyroidism": 4
    }
    Thyroid_Function = thyroid_map[st.selectbox("Thyroid Function", list(thyroid_map.keys()))]

    physical_map = {
        "Select": None,
        "Diffuse Goiter": 0,
        "Multinodular Goiter": 1,
        "Normal": 2,
        "Single Nodular Goiter - Left": 3,
        "Single Nodular Goiter - Right": 4
    }
    Physical_Examination = physical_map[st.selectbox("Physical Examination", list(physical_map.keys()))]

    pathology_map = {
        "Select": None,
        "Follicular": 0,
        "Hurthle Cell": 1,
        "Micropapillary": 2,
        "Papillary": 3
    }
    Pathology = pathology_map[st.selectbox("Pathology", list(pathology_map.keys()))]

    adenopathy_map = {
        "Select": None,
        "Bilateral": 0,
        "Extensive": 1,
        "Left": 2,
        "No": 3,
        "Posterior": 4,
        "Right": 5
    }
    Adenopathy = adenopathy_map[st.selectbox("Adenopathy", list(adenopathy_map.keys()))]

    focality_map = {"Select": None, "Multi-Focal": 0, "Uni-Focal": 1}
    Focality = focality_map[st.selectbox("Focality", list(focality_map.keys()))]

    t_stage_map = {"Select": None, "T1a": 0, "T1b": 1, "T2": 2, "T3a": 3, "T3b": 4, "T4a": 5, "T4b": 6}
    T_Stage = t_stage_map[st.selectbox("T Stage", list(t_stage_map.keys()))]

    n_stage_map = {"Select": None, "N0": 0, "N1a": 1, "N1b": 2}
    N_Stage = n_stage_map[st.selectbox("N Stage", list(n_stage_map.keys()))]

    m_stage_map = {"Select": None, "M0": 0, "M1": 1}
    M_Stage = m_stage_map[st.selectbox("M Stage", list(m_stage_map.keys()))]

    stage_map = {"Select": None, "I": 0, "II": 1, "III": 2, "IVA": 3, "IVB": 4}
    Stage = stage_map[st.selectbox("Stage", list(stage_map.keys()))]

    response_map = {
        "Select": None,
        "Biochemical Incomplete": 0,
        "Excellent": 1,
        "Indeterminate": 2,
        "Structural Incomplete": 3
    }
    Response = response_map[st.selectbox("Response", list(response_map.keys()))]

    risk_map = {"Select": None, "High": 0, "Intermediate": 1, "Low": 2}
    Risk = risk_map[st.selectbox("Risk", list(risk_map.keys()))]

    submitted = st.form_submit_button("Predict")

# Make prediction
if submitted:
    # Check if any field is left blank
    fields = {
        "Age": Age, "Gender": Gender, "Smoking": Smoking,
        "History of Smoking": Hx_Smoking, "History of Radiotherapy": Hx_Radiothreapy,
        "Thyroid Function": Thyroid_Function, "Physical Examination": Physical_Examination,
        "Pathology": Pathology, "Adenopathy": Adenopathy, "Focality": Focality,
        "T Stage": T_Stage, "N Stage": N_Stage, "M Stage": M_Stage,
        "Stage": Stage, "Response": Response, "Risk": Risk
    }

    missing = [key for key, val in fields.items() if val is None]

    if missing:
        st.warning(f"⚠️ Please fill in the following fields: {', '.join(missing)}")
    else:
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
