import plotly.express as px
import pandas as pd
import streamlit as st

st.image("./img/ti.jpg")

# สร้าง DataFrame ของคุณ
# เช่น
df = pd.read_csv("./data/app1.csv")


fig_scatter = px.scatter(df, x='Age', y='BMI', title='Scatter Plot: การเปรียบเทียบการเกิดระหว่างดัชนีมวลกายและอายุ')
st.plotly_chart(fig_scatter)


fig_scatter = px.scatter(df, x="Age", y="BMI", color="Severity", hover_data=["Sex", "Height", "Weight", "Length_of_Stay"],
                title="Scatter Plot: จากกราฟด้านบนนำมาแสดงการเปรียบเทียบความรุนของการเกิดเพิ่มเติมได้")
st.plotly_chart(fig_scatter)


fig_bar = px.bar(df, x="Management", y="BMI", color="Sex", barmode="group",
                 title="Bar Plot: เปรียบเทียบดัชนีมวลกายและความรุนแกรงระหว่างเพศ")
st.plotly_chart(fig_bar)



fig_bar = px.bar(df, x="Severity", y="BMI", color="Sex", barmode="group",
                 title="Bar Plot: เปรียบเทียบดัชนีมวลกายและความรุนแกรงระหว่างเพศ")
st.plotly_chart(fig_bar)



