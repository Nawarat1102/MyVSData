import plotly.express as px
import pandas as pd
import streamlit as st

# โหลดข้อมูล
df = pd.read_csv("./data/app1.csv")


# สร้างแผนภูมิแท่ง
fig_bar = px.bar(df['Sex'].value_counts(), title='Gender Comparison')
st.plotly_chart(fig_bar)






# Scatter Plot
#แกน X ของกราฟนี้จะแสดงอายุของเด็ก (Age) และแกน Y จะแสดงดัชนีมวลกาย (BMI) โดยแบ่งตามระดับความรุนแรงของอาการ (Severity) 
#ซึ่งจะแสดงด้วยสีที่แตกต่างกัน นอกจากนี้ โดยที่เมื่อนำเมาส์ไปวางที่จุดบนกราฟ จะแสดงข้อมูลเพิ่มเติมเกี่ยวกับเพศ 
#(Sex), ส่วนสูง (Height), น้ำหนัก (Weight), และเวลาการรักษา (Treatment Time) ในรูปแบบของ tooltip 

fig_scatter = px.scatter(df, x="Age", y="BMI", color="Severity", hover_data=["Sex", "Height", "Weight", "Length_of_Stay"],
                title="Scatter Plot: Age vs BMI")
st.plotly_chart(fig_scatter)


# สร้างแผนภูมิแท่ง
fig_bar = px.bar(df, x="Severity", y="BMI", color="Sex", barmode="group",
                 title="Bar Plot: Average BMI by Severity and Sex")
st.plotly_chart(fig_bar)
