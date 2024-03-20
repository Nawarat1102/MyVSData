import streamlit as st
import pandas as pd

st.header("Show Data Index Price")

df=pd.read_csv("./data/car_pri.csv")
st.write(df.head(10))

#st.header("Show Chart")
#statistics = df.describe()

st.write("ค่าสถิติของข้อมูล:")
st.write(statistics)
