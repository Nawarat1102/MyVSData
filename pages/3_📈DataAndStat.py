import streamlit as st
import pandas as pd

st.header("Show Data Index Price")

df = pd.read_csv("./data/car_pri.csv")

st.subheader("Columns in DataFrame:")
st.write(df.columns)

st.header("Show Chart")

st.line_chart(
    df[['car_pri', 'make', 'sellingprice']]
)
