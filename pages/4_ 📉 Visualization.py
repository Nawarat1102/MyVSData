import plotly.express as px
import pandas as pd
import streamlit as st

st.image("./img/ti.jpg")

# สร้าง DataFrame ของคุณ
# เช่น
df = pd.read_csv("./data/app1.csv")

fig_scatter = px.scatter(df, x="Age", y="BMI", color="Severity", hover_data=["Sex", "Height", "Weight", "Length_of_Stay"],
                title="Scatter Plot: Age vs BMI")
st.plotly_chart(fig_scatter)





# สร้างแผนภูมิแท่ง
fig_bar = px.bar(df, x="Severity", y="BMI", color="Sex", barmode="group",
                 title="Bar Plot: Average BMI by Severity and Sex")
st.plotly_chart(fig_bar)




# สร้างแผนภูมิเส้น
fig_line = px.line(df, x="Weight", y="Sex")

# สร้างแผนภูมิแท่ง
fig_bar = px.bar(df, x="Age", y="BMI")

# สร้างแผนภูมิเปรียบเทียบ
#fig_box = px.box(df, x='Sex', y='BMI')

# สร้างแผนภูมิแผ่น
fig_pie = px.pie(df, names='Length_of_Stay')

# แสดงแผนภูมิโดยใช้คำสั่ง st.plotly_chart()
st.plotly_chart(fig_pie)

# แสดงแผนภูมิโดยใช้คำสั่ง st.plotly_chart()
st.plotly_chart(fig_box)

# แสดงกราฟโดยใช้คำสั่ง st.plotly_chart()
st.plotly_chart(fig_line)
st.plotly_chart(fig_bar)

st.image("./img/ti.jpg")
