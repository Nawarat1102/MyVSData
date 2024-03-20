import streamlit as st
import pandas as pd

df = pd.read_csv("./data/app1.csv")

grouped_data = df.groupby('Sex')['BMI'].mean()

