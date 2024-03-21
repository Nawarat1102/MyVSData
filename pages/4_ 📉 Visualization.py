import plotly.express as px

# สร้างแผนภูมิเส้น
fig = px.line(df, x="Age", y="BMI")
fig.show()

# สร้างแผนภูมิแท่ง
fig = px.bar(df, x="Sex", y="Severity")
fig.show()

# ... เพิ่มเติมสำหรับกราฟอื่น ๆ
