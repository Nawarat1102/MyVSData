import plotly.express as px
import pandas as pd
import streamlit as st

st.image("./img/ti.jpg")

# สร้าง DataFrame ของคุณ
# เช่น
df = pd.read_csv("./data/app1.csv")

# สร้างแผนภูมิเส้น
fig_line = px.line(df, x="Sex", y="Weight")

# สร้างแผนภูมิแท่ง
fig_bar = px.bar(df, x="Age", y="BMI")

# แสดงกราฟโดยใช้คำสั่ง st.plotly_chart()
st.plotly_chart(fig_line)
st.plotly_chart(fig_bar)
