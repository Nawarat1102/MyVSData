import streamlit as st
import pandas as pd

df=pd.read_csv("./data/car_pri.csv")

st.scatter(df['make'], df['model'], x_label="Make", y_label="Model")




