import json
import time
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import streamlit as st
import pandas as pd

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_hello = "https://lottie.host/a1c75f38-0233-4edb-b653-502bd22dd4c6/oIWqm5yifU.json"
lottie_hello = load_lottieurl(lottie_url_hello)
st_lottie(lottie_hello, key="hello")


st.image("./img/ti.jpg")

st.header("Show Data Index Price")

df=pd.read_csv("./data/app1.csv")
st.write(df.head(10))

st.header("ค่าสถิติของข้อมูล:")
statistics = df.describe()

if(st.button("แสดงข้อมูลตัวอย่าง")):
    st.write(statistics)
    st.button("ไม่แสดงข้อมูลตัวอย่าง")
else:
    st.button("ไม่แสดงข้อมูลตัวอย่าง")