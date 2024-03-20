import streamlit as st
import pandas as pd

df=pd.read_csv("./data/app1.csv")

st.bar_chart(df, x='Sex', y='BMI')

