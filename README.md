# 🏦 Credit Risk Intelligence Platform

## 📌 Project Overview

The Credit Risk Intelligence Platform is an AI-powered decision support system designed to assess loan default risk using machine learning, explainable AI, business rules, and natural language analytics. The platform helps financial institutions identify high-risk applicants, understand the factors driving risk predictions, and interact with credit data using a conversational chatbot.

The project is built using the Home Credit Default Risk dataset and integrates machine learning, data analytics, explainability, and business intelligence into a unified Streamlit application.

---

# 🎯 Objectives

* Predict the probability of loan default for applicants.
* Provide explainable AI insights for model predictions.
* Enable users to interact with data using natural language questions.
* Generate business-friendly risk rules for decision-making.
* Visualize key credit risk insights through interactive dashboards.

---

# 🚀 Key Features

### 🤖 Credit Risk Prediction

* Predicts applicant default risk using XGBoost.
* Categorizes applicants into:

  * Low Risk
  * Medium Risk
  * High Risk

### 📊 EDA Dashboard

* Interactive visualizations.
* Default distribution analysis.
* Gender-wise and education-wise risk analysis.
* Income and demographic insights.

### 📈 Explainable AI

* Feature importance visualization.
* Identifies factors influencing risk predictions.
* Improves transparency and trust in model decisions.

### 💬 Talk-to-Data Chatbot

* Powered by Google Gemini.
* Converts natural language questions into SQL queries.
* Executes queries on SQLite database.
* Returns business-friendly answers.

### 📜 Business Rules Engine

* Converts model insights into understandable credit policies.
* Generates risk explanations for business users.
* Supports transparent decision-making.

---

# 📂 Dataset

Dataset Used:
Home Credit Default Risk Dataset

### Dataset Statistics

| Metric           | Value   |
| ---------------- | ------- |
| Records          | 307,511 |
| Initial Features | 122     |
| Final Features   | 80      |
| Default Rate     | 8.07%   |

Target Variable:

* TARGET = 0 → Non-Default
* TARGET = 1 → Default

---

# 🛠️ Technology Stack

### Programming Language

* Python

### Machine Learning

* XGBoost
* Scikit-Learn

### Data Processing

* Pandas
* NumPy

### Visualization

* Plotly
* Matplotlib

### Database

* SQLite

### Conversational AI

* Google Gemini API

### Web Framework

* Streamlit

---

# 📊 Exploratory Data Analysis

Key findings from the dataset:

* Only 8.07% of applicants defaulted.
* Male applicants showed a higher default rate than female applicants.
* Lower Secondary education had the highest default rate.
* Academic Degree holders had the lowest default rate.
* Income and credit amount significantly influenced risk levels.

---

# ⚙️ Data Preprocessing

The following preprocessing steps were performed:

* Missing value treatment
* Feature selection
* Categorical encoding
* Numerical imputation
* Train-test splitting
* Data transformation using pipelines

---

# 🧠 Machine Learning Model

### Algorithm Used

XGBoost Classifier

### Model Performance

| Metric        | Value |
| ------------- | ----- |
| ROC-AUC Score | 0.753 |

The XGBoost model achieved the best performance among the evaluated models and was selected for deployment.

---

# 📈 Explainable AI

Model interpretability was provided using feature importance analysis.

Top influential features include:

* EXT_SOURCE_2
* EXT_SOURCE_3
* AMT_CREDIT
* AMT_INCOME_TOTAL
* DAYS_BIRTH

These features significantly contributed to default risk prediction.

---

# 💬 Talk-to-Data System

Users can ask business questions in natural language.

### Example Questions

* How many customers defaulted?
* What is the average income of applicants?
* Which education group has the highest default rate?
* Which gender has the highest default rate?

### Workflow

User Question → Gemini → SQL Query → SQLite Database → Business Answer

---

# 📜 Business Rules Engine

The platform converts analytical insights into business-friendly rules.

### Sample Rules

* Lower Secondary Education → Higher Risk
* High Credit Amount (> 800000) → Higher Risk
* Probability > 70% → High Risk
* Probability between 30% and 70% → Medium Risk
* Probability < 30% → Low Risk

---

# 🖥️ Streamlit Application Modules

### Home

Project overview and summary.

### EDA Dashboard

Interactive visual analytics and insights.

### Credit Risk Prediction

Applicant risk assessment interface.

### Explainability

Feature importance and model interpretation.

### Talk-to-Data Chatbot

Natural language analytics.

### Business Rules

Risk categorization and decision support.

---

# 📁 Project Structure

```text
credit_risk_platform/

├── data/
├── documents/
├── models/
│   └── credit_risk_model.pkl
│
├── notebooks/
│
├── sql/
│   └── credit_risk.db
│
├── src/
│   ├── app.py
│   │
│   ├── pages/
│   │   ├── 1_EDA_Dashboard.py
│   │   ├── 2_Risk_Prediction.py
│   │   ├── 3_Explainability.py
│   │   ├── 4_Chatbot.py
│   │   └── 5_Business_Rules.py
│   │
│   ├── talk_to_data/
│   └── rules/
│
├── requirements.txt
├── Dockerfile
└── README.md
```

---

# ▶️ Installation Using Docker

## Clone the Repository

```bash
git clone <repository-url>
cd credit_risk_platform
```

## Build Docker Image

```bash
docker build -t credit-risk-platform .
```

## Run Docker Container

```bash
docker run -p 8501:8501 credit-risk-platform
```

## Access the Application

Open your browser and navigate to:

```text
http://localhost:8501
```

---

# ▶️ Installation Using Docker Compose

## Build and Start Services

```bash
docker compose up --build
```

or

```bash
docker-compose up --build
```

## Access the Application

```text
http://localhost:8501
```

---

# 🛑 Stop the Application

If using Docker Compose:

```bash
docker compose down
```

or

```bash
docker-compose down
```

If using Docker:

```bash
docker ps
docker stop <container_id>
```


---

# 📌 Future Enhancements

* Real-time credit scoring API
* Advanced SHAP explainability
* Cloud deployment
* Automated model retraining
* Fraud detection integration
* Multi-language chatbot support

---

# 🏁 Conclusion

The Credit Risk Intelligence Platform combines machine learning, explainable AI, conversational analytics, and business intelligence into a single decision support system. The platform helps financial institutions assess applicant risk, improve transparency, and make data-driven lending decisions efficiently.
