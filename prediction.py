import streamlit as st
import pickle

# 加载已训练好的模型
with open('prediction.pkl', 'rb') as file:
    model = pickle.load(file)

# 创建用户输入表单
st.header('Heart Disease Prediction')
age = st.number_input('Age（年龄）')
sex = st.selectbox('Sex（性别）', ['Male（男）', 'Female（女）'])
chest_pain_type = st.selectbox('Chest Pain Type（胸痛类型）', ['Typical Angina（典型心绞痛）', 'Atypical Angina（非典型心绞痛）', 'Non-anginal Pain（非神经疼痛）', 'Asymptomatic（无症状）'])
resting_bp = st.number_input('Resting Blood Pressure（休息血压）')
cholesterol = st.number_input('Cholesterol（血清胆固醇）')
fasting_bs = st.selectbox('Fasting Blood Sugar（禁食血糖）', ['Lower than 120mg/dl（低于 120mg/dl）', 'Greater than 120mg/dl（高于 120mg/dl）'])
resting_ecg = st.selectbox('Resting ECG（静息心电图结果）', ['Normal（正常）', 'ST-T wave abnormality（有ST-T波异常）', 'Left ventricular hypertrophy（左心室肥大）'])
max_hr = st.number_input('Maximum Heart Rate（最大心率）')
exercise_angina = st.selectbox('Exercise Induced Angina（运动引起心绞痛）', ['No（无）', 'Yes（是）'])
old_peak = st.number_input('ST Depression induced by exercise relative to rest（相对于休息来说运动引起的ST段抑制）')
st_slope = st.selectbox('ST Slope（峰运动ST段的坡度）', ['Upsloping（向上倾斜）', 'Flat（平）', 'Downsloping（向下倾斜）'])

# 处理用户输入数据
sex = 0 if sex == 'Male（男）' else 1
chest_pain_mapping = {'Typical Angina（典型心绞痛）': 4, 'Atypical Angina（非典型心绞痛）': 3, 'Non-anginal Pain（非神经疼痛）': 2, 'Asymptomatic（无症状）': 1}
chest_pain_type = chest_pain_mapping[chest_pain_type]
resting_ecg_mapping = {'Normal（正常）': 0, 'ST-T wave abnormality（有ST-T波异常）': 2, 'Left ventricular hypertrophy（左心室肥大）': 1}
resting_ecg = resting_ecg_mapping[resting_ecg]
exercise_angina = 1 if exercise_angina == 'Yes（是）' else 0
st_slope_mapping = {'Upsloping（向上倾斜）': 1, 'Flat（平）': 0, 'Downsloping（向下倾斜）': 2}
st_slope = st_slope_mapping[st_slope]
fasting_bs = 1 if fasting_bs == 'Greater than 120mg/dl' else 0

def divide_Age(age):
    if age<=35:
        return 0
    elif age>35 and age<=65:
        return 1
    else:
        return 2
age=age.apply(divide_Age)

def divide_RestingBP(resting_bp):
    if resting_bp<90:
        return 0
    elif resting_bp>140:
        return 2
    else:
        return 1
resting_bp=resting_bp.apply(divide_RestingBP)

#小于110，返回0，大于230，返回2，中间为1
def divide_Cholesterol(cholesterol):
    if cholesterol<110:
        return 0
    elif cholesterol>230:
        return 2
    else:
        return 1
cholesterol=cholesterol.apply(divide_Cholesterol)

#小于110，返回0，大于180，返回2，中间为1
def divide_MaxHR(max_hr):
    if max_hr<110:
        return 0
    elif max_hr>180:
        return 2
    else:
        return 1
max_hr=max_hr.apply(divide_MaxHR)

#1及以下为0，1到2之间为1，2到3之间为2,其他为3
def divide_Oldpeak(old_peak):
    if old_peak<=1:
        return 0
    elif old_peak>1 and old_peak:
        return 1
    elif old_peak>2 and old_peak<=3:
        return 2
    else: return 3
old_peak=old_peak.apply(divide_Oldpeak)





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












