import streamlit as st
import  pandas as pd

st.title("Data Table")
data = pd.read_csv("tips.csv")
st.table(data)
