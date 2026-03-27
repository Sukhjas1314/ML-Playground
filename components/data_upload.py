import streamlit as st
import pandas as pd

def load_data():
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        st.subheader("📊 Dataset Preview")
        st.dataframe(df.head())

        col1, col2 = st.columns(2)
        col1.write(f"Shape: {df.shape}")
        col2.write(f"Columns: {list(df.columns)}")

        st.subheader("❗ Missing Values")
        st.write(df.isnull().sum())

        return df

    return None