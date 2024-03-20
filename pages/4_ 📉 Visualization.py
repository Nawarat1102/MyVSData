import streamlit as st
import pandas as pd

df=pd.read_csv("./data/car_pri.csv")


plt.scatter(df['make'], df['model'])
plt.xlabel("Make")
plt.ylabel("Model")
plt.show()




