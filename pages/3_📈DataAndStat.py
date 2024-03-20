import streamlit as st
import pandas as pd

st.header("Show Data Index Price")

df=pd.read_csv("./data/car_pri.csv")
st.write(df.head(10))

st.header("Show Chart")
statistics = df.describe()

print("\nค่าสถิติของข้อมูล:")
print(statistics)