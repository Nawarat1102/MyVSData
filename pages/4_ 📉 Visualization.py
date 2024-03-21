import plotly.express as px
import pandas as pd
import streamlit as st

st.image("./img/ti.jpg")
# สร้าง DataFrame ของคุณ
# เช่น
df=pd.read_csv("./data/app1.csv")

# สร้างแผนภูมิเส้น
fig = px.line(df, x="Age", y="BMI")
fig.show()

# สร้างแผนภูมิแท่ง
fig = px.bar(df, x="Sex", y="Severity")
fig.show()

