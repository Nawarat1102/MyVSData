import json
import time
import requests
import streamlit as st

st.set_page_config(
    page_title="Data Visualization Project",
    page_icon= ":bar_chart:",
)
st.sidebar.success("เลือกรายการด้านบน.")

st.header("🖥️⌨️การทำ Data Visualization!⌨️🖥️")
st.subheader("1.หลักการและเหตุผล")
st.info("""
        คือการนำข้อมูลดิบ มาวิเคราะห์และแสดงผลข้อมูลออกมาในรูปแบบของกราฟ แผนภูมิ
        ที่ช่วยให้คุณได้ข้อมูลเชิงลึกจากข้อมูลดิบเหล่านั้น ทำให้คุณเห็นคุณค่าของข้อมูล
        """)
st.subheader("2.วัตถุประสงค์")
st.info("""
        เพื่อนำเสนอข้อมูลให้อยู่ในรูปแบบที่เข้าใจง่ายโดยใช้วิธีจินตทัศน์ข้อมูล
        """)
st.balloons()