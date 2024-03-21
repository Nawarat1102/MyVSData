import plotly.express as px
import pandas as pd
import streamlit as st

df = pd.read_csv("./data/app1.csv")


# สร้างแผนภูมิแท่ง
fig_bar = px.bar(df['Sex'].value_counts(), title='กราฟแผนภูมิแท่ง : อัตราการเกิดในเพศ')
st.plotly_chart(fig_bar)

fig_box_bmi = px.box(df, y="Age", title="Box plot : อัตราการเกิดในช่วงอายุ")
st.plotly_chart(fig_box_Agw)

# สร้างกราฟแบบแท่ง
fig_box_bmi = px.box(df, y="BMI", title="Box plot : ดัชนีมวลกาย")
st.plotly_chart(fig_box_bmi)

# สร้างกราฟแบบแท่ง
fig_box_bmi = px.box(df, y="Length_of_Stay", title="Box plot : ดัชนีมวลกาย")
st.plotly_chart(fig_box_Length_of_Stay)

# สร้างกราฟวงกลม
management_counts = df['Management'].value_counts()
fig_pie = px.pie(values=management_counts.values, names=management_counts.index, title='Plotly Express : อัตราการรักษาในแต่ละแบบ')
st.plotly_chart(fig_pie)

# สร้างกราฟวงกลม
management_counts = df['Severity'].value_counts()
fig_pie = px.pie(values=management_counts.values, names=management_counts.index, title='Plotly Express : อัตราความรุนแรงของการเกกิด')
st.plotly_chart(fig_pie)





# สร้างแผนภูมิแท่ง
fig_bar = px.bar(df, x="Severity", y="BMI", color="Sex", barmode="group",
                 title="Bar Plot: Average BMI by Severity and Sex")
st.plotly_chart(fig_bar)
