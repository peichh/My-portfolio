import streamlit as st
import pandas as pd

# ตั้งค่าหน้าเว็บให้รองรับมือถือและคอมพิวเตอร์
st.set_page_config(page_title="Theerapong Portfolio", layout="centered")

# ส่วนแนะนำตัว
st.title("Theerapong Thanarodpaibun (Peach)")
st.subheader("Capacity Planner | Data Analyst")

st.write("---")
st.markdown("""
### เกี่ยวกับฉัน
ผมเป็นคนจัดการด้าน **Capacity Planning** และ **Vendor Management** เชี่ยวชาญการใช้ SQL, VBA และ Python ในการทำ Automation เพื่อเพิ่มประสิทธิภาพงาน
""")

# ส่วนทักษะ
st.write("---")
st.header("Technical Skills")
skills = {"Skill": ["SQL", "VBA", "Power Query", "Python (Pandas)", "Excel"],
          "Level": [90, 85, 95, 80, 100]}
df_skills = pd.DataFrame(skills)
st.bar_chart(df_skills.set_index("Skill"))

st.write("---")
st.info("💡 เว็บไซต์นี้สร้างด้วย Python + Streamlit")
