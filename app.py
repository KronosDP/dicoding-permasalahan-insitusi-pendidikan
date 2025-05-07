import joblib
import numpy as np
import streamlit as st

# Load the trained model
model = joblib.load('decision_tree_model.pkl')
scaler = joblib.load('scaler.pkl')

# Function to make predictions
def predict_status(inputs):
    # Convert inputs to numpy array and reshape
    input_array = np.array(inputs).reshape(1, -1)
    input_array = scaler.transform(input_array)
    prediction = model.predict_proba(input_array)  # Changed to predict_proba
    return prediction

# Streamlit UI
st.title('Student Dropout Prediction')

# Input fields for user to input data
# Order based on 'col' from predict.py
st.header("Student Profile Data")
marital_status = st.number_input('Marital Status (e.g., 1-Single, 2-Married, etc.)', min_value=1, value=1) # Placeholder
application_mode = st.number_input('Application Mode (e.g., 1-Online, 2-Offline, etc.)', min_value=1, value=1) # Placeholder
application_order = st.number_input('Application Order (0-First choice, 1-Second choice, etc.)', min_value=0, value=0) # Placeholder
course = st.number_input('Course (Course Code)', min_value=1, value=1) # Placeholder
daytime_evening_attendance = st.selectbox('Daytime/Evening Attendance (1-Daytime, 0-Evening)', [1, 0], format_func=lambda x: 'Daytime' if x == 1 else 'Evening')
previous_qualification = st.number_input('Previous Qualification (Code)', min_value=1, value=1) # Placeholder
previous_qualification_grade = st.number_input('Previous Qualification Grade', min_value=0.0, max_value=200.0, value=100.0, step=0.1)
nacionality = st.number_input('Nacionality (e.g., 1-Portuguese, etc.)', min_value=1, value=1) # Placeholder
mothers_qualification = st.number_input('Mother\'s Qualification (Code)', min_value=1, value=1) # Placeholder
fathers_qualification = st.number_input('Father\'s Qualification (Code)', min_value=1, value=1) # Placeholder
mothers_occupation = st.number_input('Mother\'s Occupation (Code)', min_value=0, value=1) # Placeholder
fathers_occupation = st.number_input('Father\'s Occupation (Code)', min_value=0, value=1) # Placeholder
admission_grade = st.slider('Admission Grade', min_value=0.0, max_value=200.0, value=120.0, step=0.1) # Existing
displaced = st.selectbox('Displaced', [1, 0], format_func=lambda x: 'Yes' if x == 1 else 'No') # Existing, ensure 1 for Yes, 0 for No
educational_special_needs = st.selectbox('Educational Special Needs', [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
debtor = st.selectbox('Debtor', [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
tuition_fees_up_to_date = st.selectbox('Tuition Fees Up to Date', [1, 0], format_func=lambda x: 'Yes' if x == 1 else 'No') # Existing, ensure 1 for Yes, 0 for No
gender = st.selectbox('Gender (1-Male, 0-Female)', [1, 0], format_func=lambda x: 'Male' if x == 1 else 'Female')
scholarship_holder = st.selectbox('Scholarship Holder', [1, 0], format_func=lambda x: 'Yes' if x == 1 else 'No') # Existing, ensure 1 for Yes, 0 for No
age_at_enrollment = st.number_input('Age at Enrollment', min_value=17, value=20)
international = st.selectbox('International Student', [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')

st.header("Curricular Units - 1st Semester")
curricular_units_1st_sem_credited = st.number_input('Curricular Units 1st Sem Credited', min_value=0, value=0)
curricular_units_1st_sem_enrolled = st.number_input('Curricular Units 1st Sem Enrolled', min_value=0, max_value=30, value=6) # Existing
curricular_units_1st_sem_evaluations = st.number_input('Curricular Units 1st Sem Evaluations', min_value=0, value=6)
curricular_units_1st_sem_approved = st.number_input('Curricular Units 1st Sem Approved', min_value=0, max_value=30, value=6) # Existing
curricular_units_1st_sem_grade = st.number_input('Curricular Units 1st Sem Grade', min_value=0.0, max_value=20.0, value=12.0, step=0.1) # Existing
curricular_units_1st_sem_without_evaluations = st.number_input('Curricular Units 1st Sem Without Evaluations', min_value=0, value=0)

st.header("Curricular Units - 2nd Semester")
curricular_units_2nd_sem_credited = st.number_input('Curricular Units 2nd Sem Credited', min_value=0, value=0)
curricular_units_2nd_sem_enrolled = st.number_input('Curricular Units 2nd Sem Enrolled', min_value=0, max_value=30, value=6) # Existing
curricular_units_2nd_sem_evaluations = st.number_input('Curricular Units 2nd Sem Evaluations', min_value=0, value=6)
curricular_units_2nd_sem_approved = st.number_input('Curricular Units 2nd Sem Approved', min_value=0, max_value=30, value=6) # Existing
curricular_units_2nd_sem_grade = st.number_input('Curricular Units 2nd Sem Grade', min_value=0.0, max_value=20.0, value=12.0, step=0.1) # Existing
curricular_units_2nd_sem_without_evaluations = st.number_input('Curricular Units 2nd Sem Without Evaluations', min_value=0, value=0)

st.header("Socio-Economic Data")
unemployment_rate = st.number_input('Unemployment Rate (%)', min_value=0.0, value=10.0, step=0.1)
inflation_rate = st.number_input('Inflation Rate (%)', min_value=-5.0, value=1.0, step=0.1)
gdp = st.number_input('GDP (Growth Rate %)', min_value=-10.0, value=1.0, step=0.1)


# Map the inputs to the format expected by the model, in the correct order
input_data = [
    marital_status,
    application_mode,
    application_order,
    course,
    daytime_evening_attendance,
    previous_qualification,
    previous_qualification_grade,
    nacionality,
    mothers_qualification,
    fathers_qualification,
    mothers_occupation,
    fathers_occupation,
    admission_grade,
    displaced,
    educational_special_needs,
    debtor,
    tuition_fees_up_to_date,
    gender,
    scholarship_holder,
    age_at_enrollment,
    international,
    curricular_units_1st_sem_credited,
    curricular_units_1st_sem_enrolled,
    curricular_units_1st_sem_evaluations,
    curricular_units_1st_sem_approved,
    curricular_units_1st_sem_grade,
    curricular_units_1st_sem_without_evaluations,
    curricular_units_2nd_sem_credited,
    curricular_units_2nd_sem_enrolled,
    curricular_units_2nd_sem_evaluations,
    curricular_units_2nd_sem_approved,
    curricular_units_2nd_sem_grade,
    curricular_units_2nd_sem_without_evaluations,
    unemployment_rate,
    inflation_rate,
    gdp
]

# Button for prediction
if st.button('Predict'):
    prediction = predict_status(input_data)

    # The prediction will be a 2D array where each column corresponds to one of the classes
    status_dict = {
        0: 'Dropout',
        1: 'Enrolled',
        2: 'Graduate'
    }
    # Find the index of the maximum predicted value
    predicted_status_index = np.argmax(prediction, axis=1)[0]
    predicted_status = status_dict[predicted_status_index]

    st.write(f"The model predicts that the student is likely to be: **{predicted_status}**")