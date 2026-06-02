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

# 🏗️ Architecture Overview

```text
                    User
                      │
                      ▼
            Streamlit Dashboard
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
   XGBoost Model  Gemini Chatbot  Business Rules
        │             │
        │             ▼
        │         SQL Query
        │             ▼
        └────── SQLite Database
```

### Components

* **Streamlit UI** provides an interactive interface.
* **XGBoost Model** predicts loan default probability.
* **Business Rules Engine** converts predictions into risk categories.
* **Gemini LLM** converts natural language into SQL queries.
* **SQLite Database** stores processed credit risk data.
* **Explainability Module** provides feature importance insights.

---

# ⚖️ Model Selection Rationale

Several machine learning approaches were considered for credit risk prediction. XGBoost was selected due to its ability to handle tabular data effectively and its strong performance on imbalanced classification problems.

### Why XGBoost?

* Handles missing values efficiently.
* Supports class imbalance handling.
* Provides feature importance analysis.
* Achieved the highest ROC-AUC score among tested models.
* Widely adopted in financial risk modeling.

---

# 📉 Class Imbalance Strategy

The Home Credit dataset contains a significant class imbalance:

| Class       | Percentage |
| ----------- | ---------- |
| Non-Default | 91.93%     |
| Default     | 8.07%      |

To address this challenge:

* XGBoost's class weighting mechanism was used.
* ROC-AUC was selected as the primary evaluation metric.
* Risk probabilities were calibrated into business-friendly risk bands.

This approach improved the model's ability to identify default cases while maintaining overall performance.

---

# 🧠 Prompt Engineering Approach

The Talk-to-Data chatbot uses Google Gemini to convert natural language questions into executable SQLite queries.

### Prompt Constraints

* Generate only SQLite-compatible SQL.
* Use only columns available in the dataset.
* Return executable SQL without additional explanations.
* Prevent generation of unsupported database operations.
* Minimize token usage through concise prompt design.

### Example

**User Question**

```text
How many customers defaulted?
```

**Generated SQL**

```sql
SELECT COUNT(SK_ID_CURR)
FROM credit_data
WHERE TARGET = 1;
```

---

# 🎯 Design Decisions

## Why XGBoost?

XGBoost was selected because it performs exceptionally well on tabular data and handles class imbalance effectively. It also provides feature importance scores that improve model interpretability.

## Why Streamlit?

Streamlit was chosen for rapid development of interactive dashboards and machine learning applications with minimal frontend complexity.

## Why SQLite?

SQLite is lightweight, portable, and easy to integrate with the chatbot module for natural language to SQL interactions.

## Why Gemini?

Google Gemini was used to convert natural language questions into SQL queries, enabling business users to interact with data without SQL knowledge.

---

# ⚠️ Known Limitations

* The model is trained on historical credit data and may require retraining for changing market conditions.
* Chatbot performance depends on LLM availability and API quotas.
* Explainability currently focuses on feature importance rather than individual SHAP explanations.
* The platform uses a subset of engineered features and may benefit from additional external data sources.
* Real-time model retraining is not currently implemented.
* SQLite is suitable for demonstration purposes but may not scale for enterprise workloads.

```
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
