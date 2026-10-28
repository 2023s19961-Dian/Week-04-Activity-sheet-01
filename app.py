import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sympy as sp

# ---------------- Page setup and chart styling ----------------
st.set_page_config(
    page_title="Week 04 Activity Dashboard",
    page_icon="📊",
    layout="wide",
)

sns.set_theme(style="whitegrid", palette="viridis", font_scale=1.05)

# ---------------- Custom dashboard theme ----------------
st.markdown(
    """
    <style>
    /* Overall page: warm ivory with subtle blue-green tint */
    .stApp {
        background: linear-gradient(135deg, #f8fafc 0%, #f5f3ff 52%, #ecfeff 100%);
        color: #172033 !important;
    }
    .block-container { padding-top: 1.8rem; max-width: 1400px; }

    /* Consistent headings and body text */
    h1, h2, h3, h4 { color: #172554; }
    h1 { font-weight: 800; }
    h2 { color: #1d4ed8; }
    h3 { color: #0f766e; }
    /* Keep the title and subtitle white inside the dark banner */
    .hero-banner h1, .hero-banner p, .hero-banner div {
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
    }
    .stApp p, .stApp label, .stApp [data-testid="stMarkdownContainer"],
    .stApp [data-testid="stText"], .stApp li {
        color: #243247;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #102a43 0%, #164e63 55%, #0f766e 100%);
    }
    section[data-testid="stSidebar"] * { color: #ffffff !important; }
    section[data-testid="stSidebar"] [data-testid="stRadio"] label {
        background: rgba(255,255,255,0.07);
        border-radius: 9px;
        padding: 5px 8px;
    }

    /* Main banner */
    .hero-banner {
        background: linear-gradient(120deg, #102a43 0%, #155e75 55%, #0f766e 100%);
        padding: 32px;
        border-radius: 20px;
        margin-bottom: 25px;
        color: #ffffff;
        box-shadow: 0 10px 28px rgba(16,42,67,0.18);
    }

    /* Metric cards: explicitly force readable dark text */
    div[data-testid="stMetric"] {
        background: #ffffff !important;
        border: 1px solid #cbd5e1;
        border-top: 4px solid #0d9488;
        padding: 18px;
        border-radius: 15px;
        box-shadow: 0 5px 16px rgba(15, 23, 42, 0.07);
    }
    div[data-testid="stMetric"] label,
    div[data-testid="stMetric"] label *,
    div[data-testid="stMetric"] [data-testid="stMetricLabel"],
    div[data-testid="stMetric"] [data-testid="stMetricLabel"] *,
    div[data-testid="stMetric"] [data-testid="stMetricValue"],
    div[data-testid="stMetric"] [data-testid="stMetricValue"] * {
        color: #172033 !important;
        -webkit-text-fill-color: #172033 !important;
        opacity: 1 !important;
    }

    /* Expanders: navy headers, white titles, white content cards */
    div[data-testid="stExpander"] {
        background: #ffffff !important;
        border: 1px solid #cbd5e1;
        border-radius: 12px;
        overflow: hidden;
    }
    div[data-testid="stExpander"] summary {
        background: #17324d !important;
        color: #ffffff !important;
        font-weight: 700 !important;
    }
    div[data-testid="stExpander"] summary p,
    div[data-testid="stExpander"] summary span,
    div[data-testid="stExpander"] summary svg {
        color: #ffffff !important;
        fill: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
    }
    div[data-testid="stExpander"] summary:hover {
        background: #0f766e !important;
    }
    div[data-testid="stExpander"] [data-testid="stMarkdownContainer"],
    div[data-testid="stExpander"] p,
    div[data-testid="stExpander"] span {
        color: #243247 !important;
        -webkit-text-fill-color: #243247 !important;
    }

    /* Code / calculated values: light background and dark readable text */
    .stApp code, .stApp pre,
    .stApp [data-testid="stCode"] *,
    .stApp [data-testid="stCodeBlock"] *,
    .stApp [data-testid="stCode"] code,
    .stApp [data-testid="stCodeBlock"] code {
        color: #172033 !important;
        -webkit-text-fill-color: #172033 !important;
        background-color: #f1f5f9 !important;
        opacity: 1 !important;
    }
    .stApp [data-testid="stCode"] pre,
    .stApp [data-testid="stCodeBlock"] pre {
        background-color: #f1f5f9 !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 10px !important;
    }

    /* Inputs and upload area */
    .stApp input, .stApp textarea, .stApp [data-baseweb="select"] * {
        color: #172033 !important;
    }
    [data-testid="stFileUploader"] {
        background: #ffffff;
        border: 1px dashed #94a3b8;
        border-radius: 14px;
        padding: 14px;
    }
    [data-testid="stFileUploader"] label,
    [data-testid="stFileUploader"] label *,
    [data-testid="stFileUploader"] small,
    [data-testid="stFileUploader"] section,
    [data-testid="stFileUploader"] section * {
        color: #243247 !important;
        -webkit-text-fill-color: #243247 !important;
        opacity: 1 !important;
    }
    [data-testid="stFileUploader"] button {
        background: #155e75 !important;
        color: #ffffff !important;
        border: 0 !important;
    }
    [data-testid="stFileUploader"] button * {
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
    }

    /* Buttons */
    .stButton > button, .stDownloadButton > button {
        background: linear-gradient(90deg, #155e75, #0f766e) !important;
        color: #ffffff !important;
        border-radius: 10px;
        border: none;
        font-weight: 650;
    }
    .stButton > button:hover, .stDownloadButton > button:hover {
        background: linear-gradient(90deg, #0f766e, #0d9488) !important;
        border: 1px solid #0f766e;
        color: #ffffff !important;
    }

    /* Alerts */
    [data-testid="stAlert"] {
        border-radius: 12px;
    }
    
/* Improve input and upload text visibility */
.stApp input,
.stApp textarea,
.stApp select {
    color: #1f2937 !important;
    background-color: #ffffff !important;
    border: 1px solid #cbd5e1 !important;
}

/* Number input controls */
div[data-testid="stNumberInput"] input {
    color: #1f2937 !important;
    background-color: #ffffff !important;
    -webkit-text-fill-color: #1f2937 !important;
}

/* CSV uploader text */
div[data-testid="stFileUploader"] section {
    background-color: #f8fafc !important;
}

div[data-testid="stFileUploader"] section,
div[data-testid="stFileUploader"] section span,
div[data-testid="stFileUploader"] section small {
    color: #334155 !important;
}

/* Make the upload button readable */
div[data-testid="stFileUploader"] button {
    background-color: #0f766e !important;
    color: #ffffff !important;
    border: none !important;
}

/* Number input +/- buttons */
div[data-testid="stNumberInput"] button {
    color: #1f2937 !important;
    background-color: #f1f5f9 !important;
}

    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------- Header ----------------
st.markdown(
    """
    <div class="hero-banner">
        <div style="font-size:14px;letter-spacing:2px;">AM 3038/3084 • WEEK 04</div>
        <h1 style="color:white !important;font-size:34px;margin:12px 0;">
            Computational Mathematics
        </h1>
        <p style="font-size:17px;margin-bottom:0;color:white !important;">
            Explore Statistics, Linear Algebra, Calculus and Student Data Analysis.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("## 🗂️ Project Overview")
col1, col2, col3 = st.columns(3)
with col1:
    st.info("📊 **Question 1**\n\nDescriptive Statistics")
with col2:
    st.info("🔢 **Question 2**\n\nMatrix Calculations")
with col3:
    st.info("∫ **Question 3**\n\nPolynomial and Calculus")
st.success(
    "📈 Question 4: Student Performance Analysis — "
    "explore student data using statistics and interactive charts."
)

# ---------------- Sidebar navigation ----------------
st.sidebar.markdown("## 🧭 Navigation")
st.sidebar.caption("Choose a module to explore")
question = st.sidebar.radio(
    "Activity Questions",
    [
        "Question 1: Statistics",
        "Question 2: Matrices",
        "Question 3: Calculus",
        "Question 4: Student Data",
    ],
    captions=[
        "📊 Descriptive statistics",
        "🔢 Matrix calculations",
        "∫ Polynomial and calculus",
        "📈 Student performance",
    ],
)
st.sidebar.divider()
st.sidebar.markdown("### 📚 About This Project")
st.sidebar.write("**Course:** AM 3038/3084")
st.sidebar.write("**Activity:** Week 04")
st.sidebar.write("Computational Mathematical Modeling")
st.sidebar.divider()
st.sidebar.caption("AM 3038/3084")
st.sidebar.caption("Computational Mathematical Modeling")

# ==================================================
# QUESTION 1 — STATISTICS
# ==================================================
if question == "Question 1: Statistics":
    st.header("Question 1 — Descriptive Statistics")
    st.markdown(
        """
        **Question:** A sample of 20 undergraduate students reported the number
        of hours they dedicated to self-study during a midterm revision week.

        **Dataset:**

        `5, 2, 8, 4, 7, 1, 5, 10, 4, 7, 3, 6, 3, 5, 2, 7, 4, 9, 5, 11`
        """
    )
    data = [5, 2, 8, 4, 7, 1, 5, 10, 4, 7, 3, 6, 3, 5, 2, 7, 4, 9, 5, 11]

    with st.expander("Part (a): Determine the mean and median", expanded=True):
        st.latex(r"\bar{x}=\frac{\sum x_i}{n}")
        st.write("Mean:", f"{np.mean(data):.2f}")
        st.write("Median:", f"{np.median(data):.2f}")

    with st.expander("Part (b): Sample variance and standard deviation"):
        st.write("Sample variance:", f"{np.var(data, ddof=1):.4f}")
        st.write("Sample standard deviation:", f"{np.std(data, ddof=1):.4f}")

    st.markdown(
        "**Part (c):** Suppose a recording error occurred and the first student "
        "who recorded 8 hours had actually studied 12 hours. Update the dataset "
        "and recalculate the quantities above."
    )
    corrected_value = st.number_input(
        "Corrected study hours", min_value=0, max_value=100, value=12, step=1
    )
    updated_data = data.copy()
    updated_data[2] = corrected_value

    st.markdown("### 📊 Updated Statistical Results")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("📈 Mean", f"{np.mean(updated_data):.2f}")
    with col2:
        st.metric("🎯 Median", f"{np.median(updated_data):.2f}")
    with col3:
        st.metric("📐 Sample Variance", f"{np.var(updated_data, ddof=1):.2f}")
    with col4:
        st.metric("📊 Sample SD", f"{np.std(updated_data, ddof=1):.2f}")

    st.markdown("**Part (d):** Plot a histogram of the updated dataset with appropriate binning and labels.")
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.hist(updated_data, bins=range(0, 15, 2), color="#0f766e", edgecolor="white", linewidth=2, alpha=0.9)
    ax.set_xlabel("Self-study Hours", fontsize=12)
    ax.set_ylabel("Number of Students", fontsize=12)
    ax.set_title("Distribution of Self-study Hours", fontsize=16, fontweight="bold")
    ax.grid(axis="y", alpha=0.25)
    ax.set_axisbelow(True)
    st.pyplot(fig)
    plt.close(fig)

# ==================================================
# QUESTION 2 — MATRICES
# ==================================================
elif question == "Question 2: Matrices":
    st.header("Question 2 — Matrix Calculations")
    st.markdown("**Question:** Consider the following system:")
    st.latex(r"2x+y+z=10")
    st.latex(r"x+3y+2z=18")
    st.latex(r"3x+y+2z=17")

    A = np.array([[2, 1, 1], [1, 3, 2], [3, 1, 2]], dtype=float)
    B = np.array([10, 18, 17], dtype=float)

    st.markdown("### Part (a): Matrix properties")
    st.markdown("**Coefficient matrix A**")
    st.dataframe(pd.DataFrame(A, columns=["x", "y", "z"], index=["Equation 1", "Equation 2", "Equation 3"]))

    with st.expander("(i) Compute the determinant", expanded=True):
        st.latex(r"\det(A)")
        st.write("Determinant:", round(np.linalg.det(A), 4))
    with st.expander("(ii) Compute the inverse matrix"):
        st.dataframe(pd.DataFrame(np.linalg.inv(A)))

    eigenvalues, eigenvectors = np.linalg.eig(A)
    with st.expander("(iii) Find the eigenvalues"):
        st.write(eigenvalues)
    with st.expander("(iv) Find the corresponding eigenvectors"):
        st.write("Each column corresponds to an eigenvalue in order.")
        st.dataframe(pd.DataFrame(eigenvectors))

    st.markdown("### Part (b): Solve the system")
    X = np.linalg.solve(A, B)
    st.latex(r"AX=B")
    st.dataframe(pd.DataFrame(X, index=["x", "y", "z"], columns=["Solution"]))

    st.markdown("### Part (c): Residual vector and Euclidean norm")
    R = A @ X - B
    st.latex(r"R=AX-B")
    st.write("Residual vector:", R)
    st.write("Euclidean norm:", np.linalg.norm(R, 2))

# ==================================================
# QUESTION 3 — CALCULUS
# ==================================================
elif question == "Question 3: Calculus":
    st.header("Question 3 — Polynomial and Calculus")
    t = sp.symbols("t")
    f = t**3 - 6*t**2 + 9*t + 2

    st.markdown("**Question:** Consider the function")
    st.latex(sp.latex(sp.Eq(sp.Function("f")(t), f)))

    st.markdown("### Part (a): Factorise the polynomial")
    st.write("Factorisation over the rational numbers:")
    st.latex(sp.latex(sp.factor(f)))
    st.caption("The polynomial has no factorisation into simpler rational linear factors.")

    st.markdown("### Part (b): Solve the equations")
    with st.expander("Solve f(t) = 0", expanded=True):
        st.markdown("**Exact solutions:**")
        exact_roots = sp.solve(f, t)
        exact_text = "  ,  ".join(sp.sstr(root) for root in exact_roots)
        st.markdown(
            f'<div style="background:#f1f5f9;color:#172033;padding:16px;border:1px solid #cbd5e1;border-radius:10px;overflow-wrap:anywhere;">{exact_text}</div>',
            unsafe_allow_html=True,
        )
        st.markdown("**Numerical approximations:**")
        numeric_roots = [f"{float(sp.re(root)):.6f}" for root in sp.nroots(f)]
        numeric_text = "  ,  ".join(numeric_roots)
        st.markdown(
            f'<div style="background:#f1f5f9;color:#172033;padding:16px;border:1px solid #cbd5e1;border-radius:10px;">{numeric_text}</div>',
            unsafe_allow_html=True,
        )
    with st.expander("Solve f(t) = 2"):
        roots_f2 = sp.solve(f - 2, t)
        roots_f2_text = "  ,  ".join(sp.sstr(root) for root in roots_f2)
        st.markdown(
            f'<div style="background:#f1f5f9;color:#172033;padding:16px;border:1px solid #cbd5e1;border-radius:10px;">{roots_f2_text}</div>',
            unsafe_allow_html=True,
        )

    st.markdown("### Part (c): First and second derivatives")
    st.write("First derivative:")
    st.latex(sp.latex(sp.diff(f, t)))
    st.write("Second derivative:")
    st.latex(sp.latex(sp.diff(f, t, 2)))

    st.markdown("### Part (d): Indefinite integral")
    st.latex(sp.latex(sp.integrate(f, t)) + r"+C")
    st.markdown("### Part (e): Definite integral")
    st.latex(r"\int_0^2 f(t)\,dt")
    st.write("Answer:", sp.integrate(f, (t, 0, 2)))

# ==================================================
# QUESTION 4 — STUDENT DATA
# ==================================================
elif question == "Question 4: Student Data":
    st.header("Question 4 — Student Performance Analysis")
    st.markdown(
        "**Question:** Consider the given dataset containing student performance data. "
        "Upload the CSV file to perform the analysis."
    )
    uploaded_file = st.file_uploader("Upload student_performance.csv", type=["csv"])

    if uploaded_file is None:
        st.info("Upload your student_performance.csv file to view the answers and visualisations for Question 4.")
    else:
        df = pd.read_csv(uploaded_file)
        required_columns = ["Student", "Study Hours", "Assignment", "Exam"]
        if not all(col in df.columns for col in required_columns):
            st.error("The CSV must contain these columns: " + ", ".join(required_columns))
        else:
            # Ensure numeric fields are usable in statistics and plots.
            for col in ["Study Hours", "Assignment", "Exam"]:
                df[col] = pd.to_numeric(df[col], errors="coerce")

            st.markdown("### Part (a): Explore the dataset")
            with st.expander("(i) Dimensions", expanded=True):
                st.write("Rows and columns:", df.shape)
            with st.expander("(ii) Data types"):
                st.dataframe(df.dtypes.astype(str).rename("Data type"))
            with st.expander("(iii) First few rows"):
                st.dataframe(df.head())
            with st.expander("(iv) Basic summary statistics"):
                st.dataframe(df.describe())

            st.markdown("### Part (b): Exam marks")
            c1, c2, c3 = st.columns(3)
            c1.metric("Mean", f"{df['Exam'].mean():.2f}")
            c2.metric("Median", f"{df['Exam'].median():.2f}")
            c3.metric("Standard deviation", f"{df['Exam'].std():.2f}")
            st.write("Student with the highest exam mark:")
            if df["Exam"].notna().any():
                st.dataframe(df.loc[[df["Exam"].idxmax()]])
            else:
                st.warning("No numeric exam marks were found in the uploaded file.")

            st.markdown("### Part (c): Pearson correlation")
            corr = df["Study Hours"].corr(df["Exam"])
            st.metric("Pearson correlation", f"{corr:.4f}" if pd.notna(corr) else "Not available")

            st.markdown("### Part (d): Exam mark categories")
            clean_df = df.copy()
            clean_df["Category"] = pd.cut(
                clean_df["Exam"],
                bins=[-np.inf, 60, 80, np.inf],
                labels=["Low", "Medium", "High"],
                right=False,
            )
            st.dataframe(clean_df, use_container_width=True)
            st.download_button(
                "Download cleaned data CSV",
                clean_df.to_csv(index=False).encode("utf-8"),
                "cleaned_student_data.csv",
                "text/csv",
            )
            summary = clean_df.describe(include="all")
            st.download_button(
                "Download summary statistics CSV",
                summary.to_csv().encode("utf-8"),
                "summary_statistics.csv",
                "text/csv",
            )

            # Interactive charts — all four choices are handled here.
            st.markdown("### 📊 Part (e): Interactive Visualisations")
            chart_choice = st.selectbox(
                "Choose a chart to explore:",
                [
                    "Scatter Plot: Study Hours vs Exam Marks",
                    "Histogram: Exam Marks",
                    "Box Plot: Exam Marks",
                    "Heatmap: Study Hours vs Assignment Marks",
                ],
            )

            if chart_choice == "Scatter Plot: Study Hours vs Exam Marks":
                plot_df = df[["Study Hours", "Exam"]].dropna()
                fig, ax = plt.subplots(figsize=(9, 5))
                ax.scatter(plot_df["Study Hours"], plot_df["Exam"], color="#0f766e", s=100, edgecolor="white")
                ax.set_xlabel("Study Hours")
                ax.set_ylabel("Exam Marks")
                ax.set_title("Study Hours vs Exam Marks")
                ax.grid(alpha=0.25)
                st.pyplot(fig)
                plt.close(fig)
            elif chart_choice == "Histogram: Exam Marks":
                fig, ax = plt.subplots(figsize=(9, 5))
                ax.hist(df["Exam"].dropna(), bins=5, color="#0d9488", edgecolor="white", linewidth=2)
                ax.set_xlabel("Exam Marks")
                ax.set_ylabel("Frequency")
                ax.set_title("Distribution of Exam Marks")
                ax.grid(axis="y", alpha=0.25)
                st.pyplot(fig)
                plt.close(fig)
            elif chart_choice == "Box Plot: Exam Marks":
                fig, ax = plt.subplots(figsize=(9, 5))
                ax.boxplot(df["Exam"].dropna(), patch_artist=True, boxprops=dict(facecolor="#99f6e4"))
                ax.set_ylabel("Exam Marks")
                ax.set_title("Exam Marks Box Plot")
                ax.grid(axis="y", alpha=0.25)
                st.pyplot(fig)
                plt.close(fig)
            elif chart_choice == "Heatmap: Study Hours vs Assignment Marks":
                fig, ax = plt.subplots(figsize=(7, 5))
                sns.heatmap(
                    df[["Study Hours", "Assignment"]].corr(),
                    annot=True,
                    cmap="YlGnBu",
                    vmin=-1,
                    vmax=1,
                    ax=ax,
                )
                ax.set_title("Study Hours vs Assignment Marks")
                st.pyplot(fig)
                plt.close(fig)
