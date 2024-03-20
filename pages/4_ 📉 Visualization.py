import streamlit as st
import pandas as pd

df=pd.read_csv("./data/car_pri.csv")

st.bar_chart(df, x='year', y='make')

