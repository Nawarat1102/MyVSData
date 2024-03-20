import streamlit as st
import pandas as pd

df = pd.read_csv("./data/app1.csv")

grouped_data = df.groupby('Sex')['BMI'].mean()
st.bar_chart(grouped_data, color=["#FF0000", "#0000FF"])

