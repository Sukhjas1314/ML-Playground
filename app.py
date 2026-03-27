import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

from components.data_upload import load_data
from components.preprocessing import create_preprocessor
from components.model_training import get_model
from components.evaluation import evaluate_model
from components.prediction import prediction_ui

st.set_page_config(page_title="ML Playground", layout="wide")

st.title("🤖 ML Playground (Modular)")

df = load_data()

if df is not None:

    st.sidebar.title("Models & Parameters")

    st.sidebar.header("🎯 Target")
    target_column = st.sidebar.selectbox("Select Target", df.columns)

    problem_type = st.sidebar.radio(
        "Problem Type",
        ["Classification", "Regression"]
    )

    st.sidebar.header("⚙️ Preprocessing")

    encoding_option = st.sidebar.selectbox("Encoding", ["None", "One-Hot Encoding"])
    scaling_option = st.sidebar.selectbox("Scaling", ["None", "StandardScaler", "MinMaxScaler"])

    X = df.drop(columns=[target_column])
    y = df[target_column]

    preprocessor = create_preprocessor(X, encoding_option, scaling_option)

    model, params, model_name = get_model(problem_type)

    pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("model", model)
    ])

    test_size = st.slider("Test Size", 0.1, 0.5, 0.2)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=42
    )

    if st.button("🚀 Train Model"):
        pipeline.fit(X_train, y_train)
        y_pred = pipeline.predict(X_test)

        st.session_state["model"] = pipeline
        st.session_state["X"] = X

        evaluate_model(problem_type, y_test, y_pred, pipeline, X_test)

    if "model" in st.session_state:
        prediction_ui(st.session_state["model"], st.session_state["X"])