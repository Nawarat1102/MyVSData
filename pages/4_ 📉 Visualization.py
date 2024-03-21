import plotly.express as px
import pandas as pd
import streamlit as st

st.image("./img/ti.jpg")

# สร้าง DataFrame ของคุณ
# เช่น
df = pd.read_csv("./data/app1.csv")

st.header("การเปรียบเทียบการเกิดระหว่างดัชนีมวลกายและอายุ")
fig_scatter = px.scatter(df, x='Age', y='BMI', title='Scatter Plot : ดัชนีมวลกายและอายุ')
st.plotly_chart(fig_scatter)


st.header("จากกราฟด้านบนนำมาแสดงการเปรียบเทียบความรุนของการเกิดเพิ่มเติมได้")
fig_scatter = px.scatter(df, x="Age", y="BMI", color="Severity", hover_data=["Sex", "Height", "Weight", "Length_of_Stay"],
                title="Scatter Plot : แสดงการเปรียบเทียบความรุนของการเกิด")
st.plotly_chart(fig_scatter)


st.header("การเปรียบเทียบการเกิดระหว่างดัชนีมวลกายและอายุ")
fig_scatter = px.scatter(df, x='Height', y='Weight', title='Scatter Plot : ดัชนีมวลกายและอายุ')
st.plotly_chart(fig_scatter)


st.header("เปรียบเทียบดัชนีมวลกายและการรักษาระหว่างเพศ")
fig_bar = px.bar(df, x="Management", y="BMI", color="Sex", barmode="group",
                 title="Bar Plot: การรักษาแบบอนุรัษณ์นิยม ")
st.plotly_chart(fig_bar)


st.header("เปรียบเทียบดัชนีมวลกายและความรุนแกรงระหว่างเพศ")
fig_bar = px.bar(df, x="Severity", y="BMI", color="Sex", barmode="group",
                 title="Bar Plot: ความรุนแรง อักเสบ รุนแรง")
st.plotly_chart(fig_bar)



