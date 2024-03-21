import plotly.express as px
import pandas as pd
import streamlit as st

# โหลดข้อมูล
df = pd.read_csv("./data/ข้อมูลอักเสบในเด็ก.csv")

# Scatter Plot
fig_scatter = px.scatter(df, x="Age", y="BMI", color="Severity", hover_data=["Sex", "Height", "Weight", "Length_of_Stay"],
                          title="Scatter Plot: Age vs BMI")
st.plotly_chart(fig_scatter)
