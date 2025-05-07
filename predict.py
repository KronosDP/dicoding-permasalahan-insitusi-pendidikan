import joblib
import pandas as pd

# Load the model
loaded_model = joblib.load('decision_tree_model.pkl')

col = ['Marital_status', 'Application_mode', 'Application_order', 'Course',
       'Daytime_evening_attendance', 'Previous_qualification',
       'Previous_qualification_grade', 'Nacionality', 'Mothers_qualification',
       'Fathers_qualification', 'Mothers_occupation', 'Fathers_occupation',
       'Admission_grade', 'Displaced', 'Educational_special_needs', 'Debtor',
       'Tuition_fees_up_to_date', 'Gender', 'Scholarship_holder',
       'Age_at_enrollment', 'International',
       'Curricular_units_1st_sem_credited',
       'Curricular_units_1st_sem_enrolled',
       'Curricular_units_1st_sem_evaluations',
       'Curricular_units_1st_sem_approved', 'Curricular_units_1st_sem_grade',
       'Curricular_units_1st_sem_without_evaluations',
       'Curricular_units_2nd_sem_credited',
       'Curricular_units_2nd_sem_enrolled',
       'Curricular_units_2nd_sem_evaluations',
       'Curricular_units_2nd_sem_approved', 'Curricular_units_2nd_sem_grade',
       'Curricular_units_2nd_sem_without_evaluations', 'Unemployment_rate',
       'Inflation_rate', 'GDP']

data = [-0.29482874863473196, 1.3345143571599094, -0.5540677512436588, 0.13969299706341817, 0.3500824566660891, -0.3502304870527489, -0.14064630444850384, -0.12629815810852282, 0.8524937365289073, 0.6900772949871098, 3.3070396411434353, 3.4554341886015005, -1.1328660960323853, 0.755070201429751, -0.10799293622248544, -0.11918532942853668, -2.7163924382879365, 1.3576404754825118, -0.5749141812387947, 0.0450459801869993, -0.15968211351302047, -0.30081305824983723, -1.2882410830545294, -1.2499750586658513, -1.5212573894487618, -2.1971023927998017, -0.19927303148411477, -0.2824423108896146, -1.8238139179678985, -1.478326580961879, -1.471526880526303, -1.963488622985818, -0.199440991148615, -1.3437844510165071, 1.0527041239481851, 0.07260378207802262]

# make col and data into a dataframe

data = pd.DataFrame([data], columns=col)

# Make predictions with the loaded model
loaded_y_pred = loaded_model.predict(data)

dict = {'Dropout': 0, 'Enrolled': 1, 'Graduate': 2}

# Convert the prediction to a string
loaded_y_pred = [list(dict.keys())[list(dict.values()).index(i)] for i in loaded_y_pred]

print("Your data prediction is", loaded_y_pred[0])