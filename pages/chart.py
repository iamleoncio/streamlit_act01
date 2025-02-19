import pandas as pd
import streamlit as st


# Set full-width layout
st.set_page_config(layout="wide")

# Define layout columns
col1, col2, col3 = st.columns([1, 3, 1])

# Read data
data = pd.read_csv("tips_2.csv")

# Ensure correct data types
data["billdate"] = pd.to_datetime(data["billdate"], errors="coerce")
data["total_bill"] = pd.to_numeric(data["total_bill"], errors="coerce")
data["tip"] = pd.to_numeric(data["tip"], errors="coerce")

# Compute statistics
male = data[data["sex"] == "Male"].shape[0]
female = data[data["sex"] == "Female"].shape[0]
tip = data["tip"].sum()

# Column 1: Metrics & Salary Calculation
with col1:
    st.markdown("### 📊 Statistics")
    metric1, metric2, metric3 = st.columns(3)  # Place metrics in one row

    with metric1:
        st.metric(label="Male Count", value=male)
    with metric2:
        st.metric(label="Female Count", value=female)
    with metric3:
        st.metric(label="Total Tip", value=f"${tip:,.2f}")

    st.divider()

    # Salary Calculation
    st.markdown("### 💰 Salary Calculator")
    a = st.number_input("What is your salary?", min_value=0.0, format="%.2f")
    b = st.number_input("How much is your tax?", min_value=0.0, format="%.2f")
    c = a - b  # Fix: Subtract tax instead of adding
    st.markdown(f"#### 🏆 My net salary is **${c:,.2f}**")

# Column 2: Line & Scatter Charts
with col2:
    st.markdown("### 📈 Sales Daily Chart")
    st.line_chart(data, x="billdate", y="total_bill")
    st.scatter_chart(data, x="tip", y="total_bill")

# Column 3: Bar Chart & Chat Input
with col3:
    st.markdown("### 📊 Total Tips by Gender")
    tip_by_sex = data.groupby("sex")["tip"].sum().reset_index()
    st.bar_chart(tip_by_sex, x="sex", y="tip")  # Fix: Remove invalid params

    # Chat Container
    messages = st.container(height=300)
    if prompt := st.chat_input("Say something about us!"):
        messages.chat_message("user").write(prompt)
        messages.chat_message("assistant").write(f"Echo: {prompt}")
