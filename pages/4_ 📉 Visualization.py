import streamlit as st
import pandas as pd

df=pd.read_csv("./data/car_pri.csv")


plt.scatter(df['make'], df['model'])
plt.xlabel("Make")
plt.ylabel("Model")
plt.show()





























































# ตัวอย่างข้อมูล
#data = pd.DataFrame({
#    "Country": ["Thai", "Usa", "China", "Japan"],
#    "Population": [70000000, 330000000, 1400000000, 125000000],
#    "GDP": [400000000000, 25000000000000, 17000000000000, 5000000000000]
#})

# แสดงชื่อแอปพลิเคชัน
#st.title("แสดงข้อมูลประเทศ")

# เลือกประเภท chart
#chart_type = st.selectbox("เลือกประเภทกราฟ", ["bar chart", "line chart", "pie chart"])

# แสดง chart
#import matplotlib.pyplot as plt
#if chart_type == "bar chart":
 #   st.bar_chart(data, x="Country", y="Population")
#elif chart_type == "line chart":
#    st.line_chart(data, x="Country", y="Population")
#elif chart_type == "pie chart":
#    labels = "Thai", "Usa", "China", "Japan"
#    sizes = [70000000, 330000000, 1400000000, 125000000]
 #   explode = (0, 0.1,0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')
#
 #   fig1, ax1 = plt.subplots()
 #   ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
 #       shadow=True, startangle=90)
 #   st.pyplot(fig1)


# แสดงข้อมูลตาราง
# แสดงข้อมูล GDP
#st.write("ข้อมูล GDP")
#st.table(data[["Country", "GDP"]])
