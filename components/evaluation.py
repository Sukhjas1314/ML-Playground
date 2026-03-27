import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.metrics import confusion_matrix, roc_curve, auc

def evaluate_model(problem_type, y_test, y_pred, model, X_test):

    if problem_type == "Classification":
        from sklearn.metrics import accuracy_score

        acc = accuracy_score(y_test, y_pred)
        st.metric("Accuracy", f"{acc:.4f}")

        # Confusion Matrix
        st.subheader("📊 Confusion Matrix")
        cm = confusion_matrix(y_test, y_pred)

        fig, ax = plt.subplots()
        sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
        st.pyplot(fig)

        # ROC Curve
        if len(np.unique(y_test)) == 2:
            try:
                y_prob = model.predict_proba(X_test)[:, 1]
                fpr, tpr, _ = roc_curve(y_test, y_prob)
                roc_auc = auc(fpr, tpr)

                fig, ax = plt.subplots()
                ax.plot(fpr, tpr, label=f"AUC = {roc_auc:.2f}")
                ax.plot([0, 1], [0, 1], linestyle="--")
                ax.legend()
                st.pyplot(fig)
            except:
                st.info("ROC not available")

    else:
        from sklearn.metrics import mean_squared_error, mean_absolute_error

        rmse = mean_squared_error(y_test, y_pred, squared=False)
        mae = mean_absolute_error(y_test, y_pred)

        st.metric("RMSE", f"{rmse:.4f}")
        st.metric("MAE", f"{mae:.4f}")

        fig, ax = plt.subplots()
        ax.scatter(y_test, y_pred)
        st.pyplot(fig)