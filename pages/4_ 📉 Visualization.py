import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./data/app1.csv")

st.bar_chart(df, x='Sex', y='BMI')

BMI = df['BMI']
Severity = df['Severity']

plt.scatter(BMI, Severity)
plt.xlabel('BMI')
plt.ylabel('Severity')
plt.title('กราฟกระจายแสดงความสัมพันธ์ระหว่าง BMI กับความรุนแรง')
plt.show()
