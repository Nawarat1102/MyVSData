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

lottie_url_hello = "https://lottie.host/a1c75f38-0233-4edb-b653-502bd22dd4c6/oIWqm5yifU.json"
lottie_hello = load_lottieurl(lottie_url_hello)
st_lottie(lottie_hello, key="hello")

st.header("ทฤษฎีที่เกี่ยวข้อง")

st.subheader("1.ทฤษฎีเหมืองข้อมูล")
st.info("""
        ทฤษฎีเหมืองข้อมูลเป็นเครื่องมือที่มีประสิทธิภาพในการค้นหาความรู้จากข้อมูลขนาดใหญ่ มีการประยุกต์ใช้ในหลายสาขาและมีบทบาทสำคัญในยุคดิจิทัล
        """)

st.subheader("2.เทคนิคการจินตทัศน์ข้อมูล")
st.info("""
        การทำจินตทัศน์ข้อมูลเป็นทักษะที่มีประโยชน์สำหรับทุกคนเทคนิคต่างๆมาสามารถช่วยให้คุณนำเสนอข้อมูลได้อย่างมีประสิทธิภาพ
        """)