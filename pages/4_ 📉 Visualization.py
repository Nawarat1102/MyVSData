import plotly.express as px
import pandas as pd
import streamlit as st

st.image("./img/ti.jpg")

# สร้าง DataFrame ของคุณ
# เช่น
df = pd.read_csv("./data/app1.csv")


fig_scatter = px.scatter(df, x='Age', y='BMI', title='Scatter Plot: Age vs BMI')
st.plotly_chart(fig_scatter)






fig_scatter = px.scatter(df, x="Age", y="BMI", color="Severity", hover_data=["Sex", "Height", "Weight", "Length_of_Stay"],
                title="Scatter Plot: การเปรียบเทียบความรุนของของการเกิดระหว่างดัชนีมวลกายและอายุ")
st.plotly_chart(fig_scatter)





# สร้างแผนภูมิแท่ง
fig_bar = px.bar(df, x="Severity", y="BMI", color="Sex", barmode="group",
                 title="Bar Plot: Average BMI by Severity and Sex")
st.plotly_chart(fig_bar)



