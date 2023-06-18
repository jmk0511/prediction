import streamlit as st
import pickle

# 加载已训练好的模型
with open('decision_tree_model.pkl', 'rb') as file:
    model = pickle.load(file)

# 创建用户输入表单
st.header('Heart Disease Prediction')
age = st.number_input('Age')
sex = st.selectbox('Sex', ['Male', 'Female'])
chest_pain_type = st.selectbox('Chest Pain Type', ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'])
resting_bp = st.number_input('Resting Blood Pressure')
cholesterol = st.number_input('Cholesterol')
fasting_bs = st.selectbox('Fasting Blood Sugar', ['Lower than 120mg/dl', 'Greater than 120mg/dl'])
resting_ecg = st.selectbox('Resting ECG', ['Normal', 'ST-T wave abnormality', 'Left ventricular hypertrophy'])
max_hr = st.number_input('Maximum Heart Rate')
exercise_angina = st.selectbox('Exercise Induced Angina', ['No', 'Yes'])
old_peak = st.number_input('ST Depression induced by exercise relative to rest')
st_slope = st.selectbox('ST Slope', ['Upsloping', 'Flat', 'Downsloping'])

# 处理用户输入数据
sex = 1 if sex == 'Male' else 0
chest_pain_mapping = {'Typical Angina': 0, 'Atypical Angina': 1, 'Non-anginal Pain': 2, 'Asymptomatic': 3}
chest_pain_type = chest_pain_mapping[chest_pain_type]
fasting_bs = 1 if fasting_bs == 'Greater than 120mg/dl' else 0
resting_ecg_mapping = {'Normal': 0, 'ST-T wave abnormality': 1, 'Left ventricular hypertrophy': 2}
resting_ecg = resting_ecg_mapping[resting_ecg]
exercise_angina = 1 if exercise_angina == 'Yes' else 0
st_slope_mapping = {'Upsloping': 0, 'Flat': 1, 'Downsloping': 2}
st_slope = st_slope_mapping[st_slope]

# 进行预测
features = [[age, sex, chest_pain_type, resting_bp, cholesterol, fasting_bs, resting_ecg, max_hr, exercise_angina, old_peak, st_slope]]
prediction = model.predict(features)[0]
prediction_proba = model.predict_proba(features)[0]

# 显示预测结果
st.subheader('Prediction')
if prediction == 0:
    st.write('Congratulations! You are not at risk of heart disease.')
else:
    st.write('You are at risk of heart disease. Please consult a doctor.')

st.subheader('Prediction Probability')
st.write(f"Not at risk: {prediction_proba[0] * 100:.2f}%")
st.write(f"At risk: {prediction_proba[1] * 100:.2f}%")












