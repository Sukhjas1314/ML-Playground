<div align="center">

<!-- Animated Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f0c29,50:302b63,100:24243e&height=200&section=header&text=ML%20Playground&fontSize=60&fontColor=ffffff&fontAlignY=38&desc=Train%20%E2%80%A2%20Evaluate%20%E2%80%A2%20Predict%20%E2%80%94%20No%20Code%20Required&descAlignY=58&descSize=18&descColor=a78bfa" width="100%"/>

<br/>

<!-- Badges -->
![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-7c3aed?style=for-the-badge)

<br/>

> **A no-code interactive machine learning platform built with Streamlit.**  
> Upload your dataset, configure preprocessing, pick a model, train it — and get predictions instantly.

<br/>

[🚀 Get Started](#-quick-start) • [✨ Features](#-features) • [📁 Project Structure](#-project-structure) • [🤝 Contributing](#-contributing)

</div>

---

## 🎯 What is ML Playground?

**ML Playground** is an end-to-end, interactive ML experimentation tool that removes the friction of writing boilerplate code. Whether you're a beginner exploring machine learning or a practitioner doing quick dataset experiments — this app lets you go from raw CSV to trained model in minutes.


Upload Data → Select Target → Configure Preprocessing → Choose Model → Train → Evaluate → Predict


---

## ✨ Features

| Feature | Description |
|---|---|
| 📂 **Data Upload** | Upload any CSV dataset directly in the browser |
| 🎯 **Target Selection** | Dynamically pick your target column from the sidebar |
| 🔁 **Problem Detection** | Switch between **Classification** and **Regression** tasks |
| 🔧 **Preprocessing** | One-Hot Encoding + StandardScaler / MinMaxScaler via pipelines |
| 🤖 **Model Selection** | Choose from multiple scikit-learn models with tunable parameters |
| 📊 **Evaluation** | Accuracy, RMSE, confusion matrix, and more — rendered instantly |
| 🔮 **Live Prediction** | Input values manually and get real-time model predictions |
| ⚡ **Modular Architecture** | Clean component-based structure — easy to extend |

---

## 🖥️ App Preview

(Refer the app)
https://ml-playground-o4et5sq2trbad2eawaoxmu.streamlit.app


<img width="1439" height="777" alt="Screenshot 2026-03-28 at 1 24 52 PM" src="https://github.com/user-attachments/assets/2a8fa5a7-b036-4374-a225-5c9fd9ef5407" />


---

## 📁 Project Structure

```
ML-Playground/
│
├── app.py                    # 🚀 Main Streamlit application entry point
├── requirements.txt          # 📦 Python dependencies
│
└── components/               # 🧩 Modular components
    ├── data_upload.py        # 📂 CSV file loading & preview
    ├── preprocessing.py      # 🔧 Feature encoding & scaling pipelines
    ├── model_training.py     # 🤖 Model selection & hyperparameter UI
    ├── evaluation.py         # 📊 Metrics, plots & evaluation reports
    └── prediction.py         # 🔮 Interactive prediction interface
```

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/Sukhjas1314/ML-Playground.git
cd ML-Playground
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the App

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501` 🎉

---

## 📦 Tech Stack

```python
streamlit       # Interactive web UI framework
pandas          # Data loading and manipulation
scikit-learn    # ML models, pipelines, preprocessing & evaluation
```

---

## 🔧 How It Works

```mermaid
flowchart LR
    A[📂 Upload CSV] --> B[🎯 Select Target Column]
    B --> C{Problem Type?}
    C -->|Classification| D[🤖 Classifier Models]
    C -->|Regression| E[📈 Regressor Models]
    D --> F[🔧 Build sklearn Pipeline]
    E --> F
    F --> G[✂️ Train / Test Split]
    G --> H[🚀 Train Model]
    H --> I[📊 Evaluate Metrics]
    I --> J[🔮 Live Predictions]
```

---

## 🤝 Contributing

Contributions, ideas, and pull requests are welcome!

```bash
# Fork the repo
# Create your feature branch
git checkout -b feature/AmazingFeature

# Commit your changes
git commit -m "Add AmazingFeature"

# Push to the branch
git push origin feature/AmazingFeature

# Open a Pull Request
```

---

## 📬 Connect

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-Sukhjas1314-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Sukhjas1314)

</div>

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:24243e,50:302b63,100:0f0c29&height=120&section=footer" width="100%"/>

<sub>Built with ❤️ using Python & Streamlit</sub>

</div>
