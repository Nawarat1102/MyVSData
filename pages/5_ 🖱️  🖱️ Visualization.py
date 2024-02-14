import streamlit as st
import pandas as pd

# ตัวอย่างข้อมูล
data = pd.DataFrame({
    "Country": ["ไทย", "อเมริกา", "จีน", "ญี่ปุ่น"],
    "Population": [70000000, 330000000, 1400000000, 125000000],
    "GDP": [400000000000, 25000000000000, 17000000000000, 5000000000000]
})

# แสดงชื่อแอปพลิเคชัน
st.title("แสดงข้อมูลประเทศ")

# เลือกประเภท chart
chart_type = st.selectbox("เลือกประเภทกราฟ", ["bar chart", "line chart", "pie chart"])

# แสดง chart
if chart_type == "bar chart":
    st.bar_chart(data, x="Country", y="Population")
elif chart_type == "line chart":
    st.line_chart(data, x="Country", y="Population")
elif chart_type == "pie chart":
    st.pie_chart(data, values="Population", names="Country")

# แสดงข้อมูลตาราง
labels = 'sepal.width', 'sepal.length', 'petal.width', 'petal.length'

x1=df['sepal.width'].mean()
x2=df['sepal.length'].mean()
x3=df['petal.width'].mean()
x4=df['petal.length'].mean()

sizes = [x1, x2, x3, x4]

explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)