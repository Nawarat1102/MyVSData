import streamlit as st
import pandas as pd

st.header("Show Data Index Price")

df=pd.read_csv("./data/car_pri.csv")
st.write(df.head(10))

st.header("Show Chart")

st.line_chart(
   df, x="car_pri", y=["year", "make"], color=["#FF0000", "#0000FF"]  # Optional
)