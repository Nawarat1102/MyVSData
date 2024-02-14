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
st.table(data)