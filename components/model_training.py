import streamlit as st

def get_model(problem_type):

    params = {}

    if problem_type == "Classification":
        from sklearn.linear_model import LogisticRegression
        from sklearn.neighbors import KNeighborsClassifier
        from sklearn.tree import DecisionTreeClassifier
        from sklearn.ensemble import RandomForestClassifier

        model_name = st.sidebar.selectbox(
            "Model",
            ["Logistic Regression", "KNN", "Decision Tree", "Random Forest"]
        )

        if model_name == "Logistic Regression":
            params["C"] = st.sidebar.slider("C", 0.01, 10.0, 1.0)
            params["max_iter"] = st.sidebar.slider("Max Iter", 100, 2000, 1000)
            model = LogisticRegression(**params)

        elif model_name == "KNN":
            params["n_neighbors"] = st.sidebar.slider("Neighbors", 1, 20, 5)
            model = KNeighborsClassifier(**params)

        elif model_name == "Decision Tree":
            params["max_depth"] = st.sidebar.slider("Max Depth", 1, 20, 5)
            model = DecisionTreeClassifier(**params)

        else:
            params["n_estimators"] = st.sidebar.slider("Trees", 10, 200, 100)
            model = RandomForestClassifier(**params)

    else:
        from sklearn.linear_model import LinearRegression
        from sklearn.tree import DecisionTreeRegressor
        from sklearn.ensemble import RandomForestRegressor

        model_name = st.sidebar.selectbox(
            "Model",
            ["Linear Regression", "Decision Tree", "Random Forest"]
        )

        if model_name == "Linear Regression":
            model = LinearRegression()

        elif model_name == "Decision Tree":
            params["max_depth"] = st.sidebar.slider("Max Depth", 1, 20, 5)
            model = DecisionTreeRegressor(**params)

        else:
            params["n_estimators"] = st.sidebar.slider("Trees", 10, 200, 100)
            model = RandomForestRegressor(**params)

    return model, params, model_name