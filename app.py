import streamlit as st
import subprocess
import sys
import os

# Dashboard settings
st.set_page_config(
    page_title="Group 44 Dashboard",
    page_icon="📊",
    layout="wide"
)

# Title
st.title("📊 Group 44 - Worksheet Solutions Dashboard")
st.write("Computational Mathematics")
st.write("Four Questions | Four Contributors")

st.divider()

# Contributor details
st.subheader("Group Members")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("### Member 1")
    st.write("Question 1")

with col2:
    st.markdown("### Member 2")
    st.write("Question 2")

with col3:
    st.markdown("### Member 3")
    st.write("Question 3")

with col4:
    st.markdown("### Member 4")
    st.write("Question 4")

st.divider()

# Question selection
st.subheader("Run the Solutions")

question = st.selectbox(
    "Select a question:",
    [
        "Question 1",
        "Question 2",
        "Question 3",
        "Question 4"
    ]
)

# Python filenames
files = {
    "Question 1": "Q1.py",
    "Question 2": "Q2.py",
    "Question 3": "Q3.py",
    "Question 4": "Q4.py"
}

# Run the selected program
if st.button("Run Selected Question"):
    filename = files[question]

    if os.path.exists(filename):
        try:
            result = subprocess.run(
                [sys.executable, filename],
                capture_output=True,
                text=True,
                timeout=60
            )

            st.subheader("Output")

            if result.stdout:
                st.code(result.stdout)

            if result.stderr:
                st.error("An error or warning occurred:")
                st.code(result.stderr)

            if result.returncode == 0:
                st.success("Program execution completed.")

        except subprocess.TimeoutExpired:
            st.error("The program took too long to finish.")

    else:
        st.error(f"File not found: {filename}")

st.divider()

st.caption("Group 44 | Worksheet Solutions")
