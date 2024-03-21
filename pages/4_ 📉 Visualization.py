import pandas as pd
import matplotlib.pyplot as plt

# อ่านข้อมูลจากไฟล์ CSV
df = pd.read_csv("app_data.csv")

# สมมติว่า BMI และ Severity เป็นชื่อคอลัมน์ใน CSV ของคุณ
BMI = df["BMI"]
Severity = df["Severity"]

# วาดแผนภูมิกระจาย
plt.scatter(BMI, Severity)
plt.xlabel("BMI")
plt.ylabel("Severity")
plt.title("แผนภูมิกระจายแสดงความสัมพันธ์ระหว่าง BMI กับความรุนแรง")
plt.show()
