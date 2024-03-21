import plotly.express as px
import pandas as pd
import streamlit as st

st.image("./img/ti.jpg")

# สร้าง DataFrame ของคุณ
# เช่น
df = pd.read_csv("./data/app1.csv")

# สร้างแผนภูมิเส้น
fig_line = px.line(df, x="Weight", y="Sex")

# สร้างแผนภูมิแท่ง
fig_bar = px.bar(df, x="Age", y="BMI")

# สร้างแผนภูมิเปรียบเทียบ
fig_box = px.box(df, x='Sex', y='BMI')

# สร้างแผนภูมิแผ่น
fig_pie = px.pie(df, names='Length_of_Stay')

# แสดงแผนภูมิโดยใช้คำสั่ง st.plotly_chart()
st.plotly_chart(fig_pie)

# แสดงแผนภูมิโดยใช้คำสั่ง st.plotly_chart()
st.plotly_chart(fig_box)

# แสดงกราฟโดยใช้คำสั่ง st.plotly_chart()
st.plotly_chart(fig_line)
st.plotly_chart(fig_bar)
