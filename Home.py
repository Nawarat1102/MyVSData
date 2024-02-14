import json
import time
import requests

import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_hello = "https://lottie.host/a6ba2cb1-4445-4e24-b0c0-29c910e30d35/siFuTj6Dck.json"
lottie_hello = load_lottieurl(lottie_url_hello)

st.header("การพยากรณ์ข้อมูล....ด้วยเทคนิค Linear Regression")
st.header("by Kairung Hengpraprohm")

#การเรียกใช้งาาน lottie file
st_lottie(lottie_hello, key="hello")
st.balloons()