
import streamlit as st
import subprocess
import sys
import os

# Dashboard settings
st.set_page_config(
    page_title="Group 03 Dashboard",
    page_icon="📊",
    layout="wide"
)

# Project folder
folder = os.path.dirname(os.path.abspath(__file__))

# Title
st.title("📊 Group 03 - Worksheet Solutions Dashboard")
st.write("Computational Mathematics")
st.write("Four Questions | Four Contributors")

st.divider()

# Contributor details
st.subheader("Group Members")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("### Janethri")
    st.write("Question 1")

with col2:
    st.markdown("### Sachini")
    st.write("Question 2")

with col3:
    st.markdown("### Dain")
    st.write("Question 3")

with col4:
    st.markdown("### Komashi")
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
    "Question 2": "act4_q2.py",
    "Question 3": "Q3.py",
    "Question 4": "Q4.py"
}

# Graph filenames for Question 1 and Question 4
graph_files = {
    "Question 1": ["Q1_graph.png"],
    "Question 4": ["Q4_graph.png"]
}

# Run the selected program
if st.button("Run Selected Question"):
    filename = files[question]
    file_path = os.path.join(folder, filename)

    if os.path.exists(file_path):
        try:
            result = subprocess.run(
                [sys.executable, file_path],
                capture_output=True,
                text=True,
                timeout=60,
                cwd=folder
            )

            st.subheader(f"{question} Output")

            if result.stdout.strip():
                st.code(result.stdout)

            if result.stderr.strip():
                st.warning("Program messages:")
                st.code(result.stderr)

            if result.returncode == 0:
                st.success("Program execution completed successfully.")
            else:
                st.error(
                    f"Program failed with exit code {result.returncode}."
                )

            # Display graph for Question 1 or Question 4
            if result.returncode == 0 and question in graph_files:
                for graph_file in graph_files[question]:
                    graph_path = os.path.join(folder, graph_file)

                    if os.path.exists(graph_path):
                        st.subheader(f"{question} Graph")
                        st.image(
                            graph_path,
                            caption=f"{question} Graph",
                            use_container_width=True
                        )
                    else:
                        st.info(
                            f"{graph_file} was not found. "
                            f"Update {filename} to save its graph "
                            f"as {graph_file}."
                        )

        except subprocess.TimeoutExpired:
            st.error("The program took too long to finish.")

        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")

    else:
        st.error(f"File not found: {filename}")

st.divider()

st.caption("Group 03 | Worksheet Solutions")

