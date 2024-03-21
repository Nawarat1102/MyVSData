import streamlit as st
import pandas as pd

df=pd.read_csv("./data/app1.csv")

st.bar_chart(df, x='Sex', y='BMI')

plt.scatter(BMI, Severity)
plt.xlabel('BMI')
plt.ylabel('Severity')
plt.title('กราฟกระจายแสดงความสัมพันธ์ระหว่าง BMI กับความรุนแรง')
plt.show()