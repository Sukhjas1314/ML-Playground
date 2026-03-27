import streamlit as st
import pandas as pd

def prediction_ui(model, X):

    st.subheader("🔮 Manual Prediction")

    input_data = {}
    for col in X.columns:
        input_data[col] = st.text_input(col)

    input_df = pd.DataFrame([input_data])

    if st.button("Predict"):
        pred = model.predict(input_df)
        st.success(f"Prediction: {pred[0]}")

    st.subheader("📂 CSV Prediction")

    file = st.file_uploader("Upload Test CSV", key="test")

    if file is not None:
        test_df = pd.read_csv(file)

        if st.button("Predict CSV"):
            preds = model.predict(test_df)
            test_df["Prediction"] = preds
            st.dataframe(test_df)