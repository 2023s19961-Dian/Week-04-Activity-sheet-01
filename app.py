
import streamlit as st
import subprocess
import sys
import os

# -------------------------------
# Dashboard Settings
# -------------------------------
st.set_page_config(
    page_title="Group 03 Dashboard",
    page_icon="📊",
    layout="wide"
)

# Project folder
folder = os.path.dirname(os.path.abspath(__file__))

# -------------------------------
# Dashboard Title
# -------------------------------
st.title("📊 Group 03 - Worksheet Solutions Dashboard")
st.write("Computational Mathematics")
st.write("Four Questions | Four Contributors")

st.divider()

# -------------------------------
# Group Members
# -------------------------------
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

# -------------------------------
# Question Selection
# -------------------------------
st.subheader("Run the Solutions")

files = {
    "Question 1": "Q1.py",
    "Question 2": "act4_q2.py",
    "Question 3": "Q3.py",
    "Question 4": "Q4.py"
}

graph_files = {
    "Question 1": ["Q1_graph.png"],
    "Question 2": ["Q2_graph.png"],
    "Question 3": ["Q3_graph.png"],
    "Question 4": ["Q4_graph.png"]
}

question = st.selectbox(
    "Select a question:",
    list(files.keys())
)

# -------------------------------
# Run Selected Question
# -------------------------------
if st.button("Run Selected Question", type="primary"):

    filename = files[question]
    file_path = os.path.join(folder, filename)

    if not os.path.isfile(file_path):
        st.error(f"File not found: {filename}")

    else:
        # Read and display the source code
        st.subheader(f"{question} - Python Source Code")

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                source_code = file.read()

            st.code(source_code, language="python")

        except Exception as e:
            st.error(f"Could not read the source code: {e}")

        # Execute the selected Python program
        try:
            with st.spinner(f"Running {question}..."):

                result = subprocess.run(
                    [sys.executable, file_path],
                    capture_output=True,
                    text=True,
                    timeout=60,
                    cwd=folder
                )

            # Display program output
            st.subheader(f"{question} - Program Output")

            if result.stdout.strip():
                st.code(result.stdout, language="text")
            else:
                st.info("The program did not produce text output.")

            # Display errors
            if result.returncode != 0:
                st.error("The program did not finish successfully.")

                if result.stderr.strip():
                    st.subheader("Error Details")
                    st.code(result.stderr, language="text")

            else:
                st.success("Program executed successfully!")

                # Display saved graphs
                for graph_file in graph_files.get(question, []):

                    graph_path = os.path.join(folder, graph_file)

                    if os.path.isfile(graph_path):
                        st.subheader(f"{question} - Graph")
                        st.image(
                            graph_path,
                            caption=graph_file,
                            use_container_width=True
                        )

                # Display additional messages
                if result.stderr.strip():
                    st.subheader("Additional Messages")
                    st.code(result.stderr, language="text")

        except subprocess.TimeoutExpired:
            st.error("The program took longer than 60 seconds.")

        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")

st.divider()

# -------------------------------
# Footer
# -------------------------------
st.caption(
    "Group 03 | Computational Mathematics | Worksheet Solutions"
)
