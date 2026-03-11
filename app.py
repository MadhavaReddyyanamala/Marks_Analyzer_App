import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------- Page Config --------
st.set_page_config(page_title="Student Result Analyzer", page_icon="📊", layout="centered")

# -------- Custom CSS --------
# st.markdown("""
# <style>

# .title {
# text-align: center;
# font-size: 60px;   /* increased size */
# font-weight: bold;
# color: black;
# margin-bottom: 20px;
# }

# </style>
# """, unsafe_allow_html=True)

st.markdown(
    "<h1 style='text-align: center; color: black; font-size:40px; font-weight:bold;'>📊 Student Result Analyzer</h1>",
    unsafe_allow_html=True
)

# -------- Title --------
# st.markdown('<p class="title">📊 Student Result Analyzer</p>', unsafe_allow_html=True)

st.write("Enter student details to analyze performance")

# -------- Student Name --------
name = st.text_input("👤 Student Name")

# -------- Marks Section --------
st.subheader("📚 Enter Subject Marks")

col1, col2 = st.columns(2)

with col1:
    math = st.number_input("Math", 0, 100)
    science = st.number_input("Science", 0, 100)

with col2:
    english = st.number_input("English", 0, 100)
    python = st.number_input("Python", 0, 100)

# -------- Analyze Button --------
if st.button("🚀 Analyze Result"):

    marks = [math, science, english, python]
    subjects = ["Math", "Science", "English", "Python"]

    total = sum(marks)
    average = total / len(marks)

    st.subheader("📋 Result Summary")

    col3, col4 = st.columns(2)

    with col3:
        st.info(f"👤 Student: {name}")
        st.success(f"📊 Total Marks: {total}")

    with col4:
        st.warning(f"📈 Average Marks: {round(average,2)}")

        if average >= 40:
            st.success("✅ Status: PASS")
        else:
            st.error("❌ Status: FAIL")

    # -------- Chart --------
    df = pd.DataFrame({
        "Subjects": subjects,
        "Marks": marks
    })

    st.subheader("📊 Subject-wise Performance")

    fig, ax = plt.subplots()
    ax.bar(subjects, marks)
    ax.set_ylabel("Marks")
    ax.set_title("Marks Distribution")

    st.pyplot(fig)