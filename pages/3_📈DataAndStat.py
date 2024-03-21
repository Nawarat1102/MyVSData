import plotly.express as px
import pandas as pd
import streamlit as st

df = pd.read_csv("./data/app1.csv")



fig_bar = px.bar(df['Sex'].value_counts(), title='กราฟแผนภูมิแท่ง : อัตราการเกิดในเพศ')
st.plotly_chart(fig_bar)


age = px.box(df, y="Age", title="Box plot : อัตราการเกิดในช่วงอายุ")
st.plotly_chart(age)


hei = px.box(df, y="Height", title="Box plot : อัตราการเกิดในช่วงส่วนสูง")
st.plotly_chart(hei)


wei = px.box(df, y="Weight", title="Box plot : อัตราการเกิดในช่วงน้ำหนัก")
st.plotly_chart(wei)


bmi = px.box(df, y="BMI", title="Box plot : ดัชนีมวลกาย")
st.plotly_chart(bmi)


day = px.box(df, y="Length_of_Stay", title="Box plot : ระยะเวลาในการพักฟื้น")
st.plotly_chart(day)


management_counts = df['Management'].value_counts()
fig_pie = px.pie(values=management_counts.values, names=management_counts.index, title='Plotly Express : อัตราการรักษาในแต่ละแบบ')
st.plotly_chart(fig_pie)


management_counts = df['Severity'].value_counts()
fig_pie = px.pie(values=management_counts.values, names=management_counts.index, title='Plotly Express : อัตราความรุนแรงของการเกิด')
st.plotly_chart(fig_pie)






