import streamlit as st
import pandas as pd


st.image("./img/bmw.png")

st.header("Show Data Index Price")

df=pd.read_csv("./data/car_pri.csv")
st.write(df.head(10))

st.header("ค่าสถิติของข้อมูล:")
statistics = df.describe()

if(st.button("แสดงข้อมูลตัวอย่าง")):
    st.write(statistics)
    st.button("ไม่แสดงข้อมูลตัวอย่าง")
else:
    st.button("ไม่แสดงข้อมูลตัวอย่าง")
