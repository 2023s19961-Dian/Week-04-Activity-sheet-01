#cd "/Users/diansugeeshwara/Documents/University Of Colombo/Level 3/SEM 2/AM 3084/Week 04 Activity sheet 01-20261022"
#python3 -m streamlit run Dashboard.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sympy as sp
import io
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Maths & Stats Dashboard", layout="wide")

# ---------------------------------------------------------------- Sidebar styling
st.markdown(
    """
    <style>
    /* ---- Wider sidebar with a deep teal gradient ---- */
    section[data-testid="stSidebar"][aria-expanded="true"] {
        min-width: 360px !important;
        max-width: 360px !important;
    }
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f2c3a 0%, #134e5e 55%, #1b6b73 100%);
        border-right: 1px solid rgba(255,255,255,0.08);
    }
    section[data-testid="stSidebar"] > div:first-child {
        padding: 1.5rem 1.25rem;
    }

    /* ---- Text colours inside the sidebar ---- */
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] span {
        color: #eaf6f6;
    }
    section[data-testid="stSidebar"] h3 {
        font-size: 1.15rem;
    }

    /* ---- Brand block (logo badge + title) ---- */
    .sb-brand {
        display: flex;
        align-items: center;
        gap: 0.9rem;
        padding: 0.2rem 0.2rem 1.3rem 0.2rem;
        border-bottom: 1px solid rgba(255,255,255,0.15);
        margin-bottom: 1.3rem;
    }
    .sb-brand .logo {
        width: 52px;
        height: 52px;
        flex-shrink: 0;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 12px;
        background: #f6c453;
        color: #10303b;
        font-size: 1.3rem;
        font-weight: 800;
    }
    .sb-brand .title {
        font-size: 1.4rem;
        font-weight: 700;
        color: #ffffff;
        line-height: 1.2;
    }
    .sb-brand .sub {
        font-size: 0.85rem;
        color: #a9d6d8;
        margin-top: 0.15rem;
    }

    /* ---- Radio -> flat menu rows ---- */
    section[data-testid="stSidebar"] div[role="radiogroup"] {
        gap: 1.5rem;
    }
    section[data-testid="stSidebar"] div[role="radiogroup"] > label {
        background: transparent;
        border: 2px solid transparent;
        border-radius: 6px;
        padding: 1.5rem 1.4rem;
        min-height: 5.2rem;
        display: flex;
        align-items: center;
        width: 100%;
        cursor: pointer;
        transition: background 0.15s ease, border-color 0.15s ease;
    }
    /* rectangle that appears on hover */
    section[data-testid="stSidebar"] div[role="radiogroup"] > label:hover {
        background: rgba(255,255,255,0.14);
        border-color: #ffffff;
    }
    /* hide the little radio circle */
    section[data-testid="stSidebar"] div[role="radiogroup"] > label > div:first-child {
        display: none;
    }
    section[data-testid="stSidebar"] div[role="radiogroup"] > label p {
        font-size: 1.4rem;
        font-weight: 500;
    }
    /* selected row: solid filled block */
    section[data-testid="stSidebar"] div[role="radiogroup"] > label:has(input:checked),
    section[data-testid="stSidebar"] div[role="radiogroup"] > label:has(input:checked):hover {
        background: #f6c453;
        border-color: #f6c453;
    }
    section[data-testid="stSidebar"] div[role="radiogroup"] > label:has(input:checked) p {
        color: #10303b;
        font-weight: 700;
    }

    /* ---- Divider above the settings section ---- */
    section[data-testid="stSidebar"] h3 {
        border-top: 1px solid rgba(255,255,255,0.15);
        padding-top: 1.3rem;
        margin-top: 1.8rem;
    }

    /* ---- Inputs ---- */
    section[data-testid="stSidebar"] [data-testid="stNumberInput"] input {
        font-size: 1.05rem;
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff;
        caret-color: #ffffff;
        background: transparent;
    }
    section[data-testid="stSidebar"] [data-testid="stNumberInput"] > div,
    section[data-testid="stSidebar"] [data-testid="stNumberInput"] div[data-baseweb="input"],
    section[data-testid="stSidebar"] [data-testid="stNumberInput"] div[data-baseweb="base-input"] {
        border-radius: 10px;
        background: rgba(0,0,0,0.30);
    }
    /* +/- stepper buttons */
    section[data-testid="stSidebar"] [data-testid="stNumberInput"] button {
        background: rgba(255,255,255,0.10);
        color: #ffffff;
    }
    section[data-testid="stSidebar"] [data-testid="stNumberInput"] button svg {
        fill: #ffffff;
    }

    /* ---- Solution values (Q2) ---- */
    .sol {
        font-size: 2.4rem;
        font-weight: 700;
        line-height: 1.2;
    }

    /* ---- Data chips (Q1 arrays) ---- */
    .chips {
        display: grid;
        grid-template-columns: repeat(10, 1fr);
        gap: 0.6rem;
        margin: 0.4rem 0 1rem 0;
    }
    .chip {
        background: #134e5e;
        border-radius: 10px;
        padding: 0.6rem 0.2rem 0.4rem 0.2rem;
        text-align: center;
    }
    .chip .val {
        font-size: 1.6rem;
        font-weight: 700;
        color: #ffffff;
        line-height: 1.1;
    }
    .chip .no {
        font-size: 0.75rem;
        color: #a9d6d8;
        margin-top: 0.2rem;
    }
    .chip.changed {
        background: #f6c453;
        box-shadow: 0 0 0 3px rgba(246,196,83,0.35);
    }
    .chip.changed .val, .chip.changed .no {
        color: #10303b;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("📊 Week 04 Activity sheet 01 ")

with st.sidebar:
    st.markdown(
        """
        <div class="sb-brand">
            <div class="logo">AM</div>
            <div>
                <div class="title">Dashboard</div>
                <div class="sub">AM 3084 · Week 04</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    page = st.radio(
        "Select question",
        [
            "📈  Q1 – Descriptive Statistics",
            "🧮  Q2 – Linear Algebra",
            "∫  Q3 – Calculus (SymPy)",
            "📋  Q4 – Student Performance",
        ],
        label_visibility="collapsed",
    )

# Short key used for routing ("Q1" ... "Q4")
page_key = "Q1" if "Q1" in page else "Q2" if "Q2" in page else "Q3" if "Q3" in page else "Q4"


def fmt(arr, decimals=4):
    """Format a NumPy array (real or complex) as text for display."""
    return np.array2string(np.round(arr, decimals), precision=decimals, suppress_small=True)


def show_array(x, label=None, highlight=None):
    """Show a 1-D array as a grid of boxes (value on top, student number below)."""
    chips = "".join(
        f'<div class="chip{" changed" if i == highlight else ""}">'
        f'<div class="val">{v}</div><div class="no">#{i + 1}</div></div>'
        for i, v in enumerate(x)
    )
    st.markdown(f'<div class="chips">{chips}</div>', unsafe_allow_html=True)


# ---------------------------------------------------------------- Q1
if page_key == "Q1":
    st.header("(Q1) · Self-study hours")

    A = np.array([5, 2, 8, 4, 7, 1, 5, 10, 4, 7, 3, 6, 3, 5, 2, 7, 4, 9, 5, 11])

    st.sidebar.subheader("⚙️ Q1 settings")
    old_val = st.sidebar.number_input("Value to replace (first occurrence)", value=8, step=1)
    new_val = st.sidebar.number_input("Replace with", value=12, step=1)

    B = A.copy()
    idx = np.where(B == old_val)[0]
    if len(idx) > 0:
        B[idx[0]] = new_val
    else:
        st.sidebar.warning(f"{old_val} not found in data – no change made.")

    def stats(x):
        return {
            "Mean": np.mean(x),
            "Median": np.median(x),
            "Sample variance": np.var(x, ddof=1),
            "Sample std dev": np.std(x, ddof=1),
        }

    sa, sb = stats(A), stats(B)

    st.subheader("Original data")
    c = st.columns(4)
    for col, (k, v) in zip(c, sa.items()):
        col.metric(k, f"{v:.4f}")
    show_array(A, "Hours")

    st.subheader("Updated data")
    c = st.columns(4)
    for col, (k, v) in zip(c, sb.items()):
        col.metric(k, f"{v:.4f}", delta=f"{v - sa[k]:+.4f}")
    show_array(B, "Hours", highlight=int(idx[0]) if len(idx) > 0 else None)

    st.subheader("Comparison")
    st.dataframe(pd.DataFrame({"Original": sa, "Updated": sb}).round(4), use_container_width=True)

    st.subheader("Histogram")
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.hist(B, bins=np.arange(0.5, B.max() + 1.5, 1), edgecolor="black")
    ax.set_xlabel("Self-study hours")
    ax.set_ylabel("Number of students")
    ax.set_title("Self-study hours (updated data)")
    st.pyplot(fig)

# ---------------------------------------------------------------- Q2
elif page_key == "Q2":
    st.header("(Q2) · Matrices and linear systems")

    A = np.array([[2, 1, 1],
                  [1, 3, 2],
                  [3, 1, 2]], dtype=float)
    B = np.array([10, 18, 17], dtype=float)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Matrix A")
        st.latex(sp.latex(sp.Matrix(A.astype(int))))
    with col2:
        st.subheader("Vector B")
        st.latex(sp.latex(sp.Matrix(B.astype(int))))

    st.subheader("Matrix properties")
    det = np.linalg.det(A)
    st.metric("det(A)", f"{det:.4f}")

    if abs(det) > 1e-12:
        st.markdown("**Inverse of A**")
        st.dataframe(pd.DataFrame(np.linalg.inv(A)).round(4), use_container_width=True)
    else:
        st.error("A is singular – no inverse.")

    values, vectors = np.linalg.eig(A)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**Eigenvalues**")
        st.code(fmt(values))
    with c2:
        st.markdown("**Eigenvectors (columns)**")
        st.code(fmt(vectors))

    st.subheader("Solution of AX = B")
    X = np.linalg.solve(A, B)
    c = st.columns(3)
    for col, name, v in zip(c, ["x", "y", "z"], X):
        col.markdown(f'<div class="sol">{name} = {v:.4f}</div>', unsafe_allow_html=True)

    st.subheader("Residual")
    R = A @ X - B
    st.code(f"R = {fmt(R, 10)}")
    st.metric("||R||₂", f"{np.linalg.norm(R):.3e}")

# ---------------------------------------------------------------- Q3
elif page_key == "Q3":
    st.header("(Q3) · Polynomial calculus with SymPy")

    t = sp.Symbol("t")
    f = t**3 - 6 * t**2 + 9 * t + 2

    st.latex(r"f(t) = " + sp.latex(f))

    st.subheader("Factorisation")
    st.latex(r"f(t) = " + sp.latex(sp.factor(f)))
    st.markdown("**Numerical roots**")
    roots = sp.Poly(f, t).nroots()
    for i, (col, r) in enumerate(zip(st.columns(len(roots)), roots), start=1):
        re_, im_ = float(sp.re(r)), float(sp.im(r))
        if abs(im_) < 1e-9:
            txt = f"{re_:.6f}"
        else:
            txt = f"{re_:.6f} {'+' if im_ >= 0 else '-'} {abs(im_):.6f}i"
        col.metric(f"Root {i}", txt)

    st.subheader("Equation solving")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**f(t) = 0**")
        for r in sp.Poly(f, t).nroots():
            st.latex(sp.latex(sp.N(r, 6)))
    with c2:
        st.markdown("**f(t) = 2**")
        st.latex(r"t = " + sp.latex(sp.solve(sp.Eq(f, 2), t)))

    st.subheader("Derivatives")
    c1, c2 = st.columns(2)
    c1.latex(r"f'(t) = " + sp.latex(sp.diff(f, t)))
    c2.latex(r"f''(t) = " + sp.latex(sp.diff(f, t, 2)))

    st.subheader("Indefinite integral")
    st.latex(r"\int f(t)\,dt = " + sp.latex(sp.integrate(f, t)) + r" + C")

    st.subheader("Definite integral")
    st.latex(r"\int_0^2 f(t)\,dt = " + sp.latex(sp.integrate(f, (t, 0, 2))))

    st.subheader("Plot of f(t)")
    lo, hi = st.slider("t range", -3.0, 6.0, (-1.0, 5.0))
    ts = np.linspace(lo, hi, 400)
    fn = sp.lambdify(t, f, "numpy")
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(ts, fn(ts), label="f(t)")
    ax.axhline(0, color="grey", lw=0.8)
    ax.set_xlabel("t")
    ax.set_ylabel("f(t)")
    ax.grid(alpha=0.3)
    ax.legend()
    st.pyplot(fig)


# ---------------------------------------------------------------- Q4
else:
    st.header("(Q4) · Student performance data")

    # Built-in copy of student_performance.csv (used if the CSV is not found next to this script)
    DEFAULT_CSV = (
        "Student,Study Hours,Assignment,Exam\n"
        "S01,2,45,48\nS02,3,50,52\nS03,4,55,58\nS04,4,60,61\nS05,5,62,65\n"
        "S06,6,68,70\nS07,6,72,74\nS08,7,78,80\nS09,8,85,87\nS10,9,90,93\n"
    )

    def strength(r):
        if np.isnan(r):
            return "not defined"
        a = abs(r)
        word = ("very weak" if a < 0.2 else "weak" if a < 0.4 else
                "moderate" if a < 0.6 else "strong" if a < 0.8 else "very strong")
        return f"{word} {'positive' if r > 0 else 'negative'} correlation"

    # ---------- Load the data
    # Order: uploaded file -> student_performance.csv next to this script -> built-in copy
    local_csv = Path(__file__).parent / "student_performance.csv"
    uploaded = st.file_uploader("Use a different file (optional)", type=["csv", "xlsx"])

    try:
        if uploaded is not None:
            if uploaded.name.lower().endswith(".csv"):
                df = pd.read_csv(uploaded)
            else:
                df = pd.read_excel(uploaded)
            st.caption(f"Data source: uploaded file ({uploaded.name})")
        elif local_csv.exists():
            df = pd.read_csv(local_csv)
            st.caption(f"Data source: {local_csv.name}")
        else:
            df = pd.read_csv(io.StringIO(DEFAULT_CSV))
            st.caption("Data source: student_performance.csv (built-in copy)")
    except Exception as e:
        st.error(f"Could not read the file: {e}")
        st.stop()

    # ---------- Column mapping (auto-detected, can be changed)
    cols = df.columns.tolist()

    def guess(keys, default):
        for i, c in enumerate(cols):
            if any(k in str(c).lower() for k in keys):
                return i
        return min(default, len(cols) - 1)

    with st.expander("Column mapping (change if the wrong columns were picked)"):
        m1, m2, m3, m4 = st.columns(4)
        name_col = m1.selectbox("Student", cols, index=guess(["name", "student", "id"], 0))
        study_col = m2.selectbox("Study hours", cols, index=guess(["study", "hour"], 1))
        exam_col = m3.selectbox("Exam marks", cols, index=guess(["exam"], 2))
        assign_col = m4.selectbox("Assignment marks", cols, index=guess(["assign"], 3))

    # ---------- Dataset overview
    st.subheader("Dataset overview")
    c1, c2 = st.columns(2)
    c1.metric("Rows", df.shape[0])
    c2.metric("Columns", df.shape[1])

    st.markdown("**Data types**")
    st.dataframe(df.dtypes.astype(str).rename("Data type").to_frame(), use_container_width=True)

    st.markdown("**First rows**")
    st.dataframe(df.head(), use_container_width=True)

    st.markdown("**Summary statistics**")
    st.dataframe(df.describe().round(4), use_container_width=True)

    # ---------- Cleaning (used for everything below)
    clean = df.drop_duplicates().copy()
    for c in {study_col, exam_col, assign_col}:
        clean[c] = pd.to_numeric(clean[c], errors="coerce")
    clean = clean.dropna(subset=list({study_col, exam_col, assign_col})).reset_index(drop=True)

    if clean.empty:
        st.error("No usable rows left after cleaning – check the column mapping above.")
        st.stop()
    if len(clean) < len(df):
        st.caption(f"Cleaning removed {len(df) - len(clean)} duplicate or incomplete row(s).")

    # ---------- Exam mark statistics
    st.subheader("Exam mark statistics")
    exam = clean[exam_col]
    c = st.columns(3)
    c[0].metric("Mean", f"{exam.mean():.4f}")
    c[1].metric("Median", f"{exam.median():.4f}")
    c[2].metric("Standard deviation", f"{exam.std():.4f}")

    top = clean[exam == exam.max()]
    names = ", ".join(top[name_col].astype(str))
    st.success(f"Highest exam mark: {exam.max():g} – {names}")
    st.dataframe(top, use_container_width=True)

    # ---------- Correlation
    st.subheader("Correlation: study hours and exam marks")
    r = clean[study_col].corr(clean[exam_col], method="pearson")
    st.metric("Pearson r", f"{r:.4f}")
    st.write(f"This is a {strength(r)}.")

    # ---------- Categories and export
    st.subheader("Exam mark categories")
    clean["Exam_Category"] = pd.cut(
        clean[exam_col],
        bins=[-np.inf, 60, 80, np.inf],
        labels=["Low", "Medium", "High"],
        right=False,                      # Low < 60, 60 <= Medium < 80, High >= 80
    )
    counts = clean["Exam_Category"].value_counts().reindex(["Low", "Medium", "High"]).fillna(0).astype(int)
    c = st.columns(3)
    for col, (k, v) in zip(c, counts.items()):
        col.metric(k, int(v))
    st.dataframe(clean, use_container_width=True)

    summary = clean.describe().T
    summary.index.name = "Column"

    st.markdown("**Export**")
    out_dir = Path(__file__).parent
    b1, b2, b3 = st.columns(3)
    if b1.button("Save CSV files to the dashboard folder"):
        clean.to_csv(out_dir / "cleaned_data.csv", index=False)
        summary.to_csv(out_dir / "summary_statistics.csv")
        st.success(f"Saved cleaned_data.csv and summary_statistics.csv in {out_dir}")
    b2.download_button("Download cleaned_data.csv", clean.to_csv(index=False), "cleaned_data.csv", "text/csv")
    b3.download_button("Download summary_statistics.csv", summary.to_csv(), "summary_statistics.csv", "text/csv")

    # ---------- Plots
    st.subheader("Plots")
    p1, p2 = st.columns(2)

    with p1:
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.scatter(clean[study_col], clean[exam_col], color="#134e5e", alpha=0.8)
        if len(clean) > 1 and clean[study_col].nunique() > 1:
            m, b = np.polyfit(clean[study_col], clean[exam_col], 1)
            xs = np.linspace(clean[study_col].min(), clean[study_col].max(), 100)
            ax.plot(xs, m * xs + b, color="#f6c453", lw=2, label="Trend line")
            ax.legend()
        ax.set_xlabel(study_col)
        ax.set_ylabel(exam_col)
        ax.set_title("Study hours vs exam marks")
        ax.grid(alpha=0.3)
        st.pyplot(fig)

    with p2:
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.hist(clean[exam_col], bins=10, color="#1b6b73", edgecolor="black")
        ax.set_xlabel(exam_col)
        ax.set_ylabel("Number of students")
        ax.set_title("Histogram of exam marks")
        st.pyplot(fig)

    p3, p4 = st.columns(2)

    with p3:
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.boxplot(clean[exam_col].values, patch_artist=True,
                   boxprops=dict(facecolor="#9fd3d6"), medianprops=dict(color="#10303b", lw=2))
        ax.set_xticks([1])
        ax.set_xticklabels([exam_col])
        ax.set_ylabel("Marks")
        ax.set_title("Box plot of exam marks")
        ax.grid(alpha=0.3)
        st.pyplot(fig)

    with p4:
        corr = clean[[study_col, assign_col]].corr()
        fig, ax = plt.subplots(figsize=(6, 4))
        im = ax.imshow(corr.values, cmap="coolwarm", vmin=-1, vmax=1)
        ax.set_xticks(range(2))
        ax.set_yticks(range(2))
        ax.set_xticklabels(corr.columns)
        ax.set_yticklabels(corr.columns)
        for i in range(2):
            for j in range(2):
                ax.text(j, i, f"{corr.values[i, j]:.2f}", ha="center", va="center", fontsize=14, fontweight="bold")
        fig.colorbar(im, ax=ax)
        ax.set_title("Heatmap: study hours vs assignment marks")
        st.pyplot(fig)