# 📊 Customer Personality Analysis Dashboard (Streamlit App)

## 🚀 Overview

This project is an **interactive data analytics dashboard** built using **Streamlit** to explore, analyze, and derive insights from a customer personality dataset.

It combines:

* Exploratory Data Analysis (EDA)
* Statistical Hypothesis Testing
* Interactive Visualizations
* Business Insight Generation

The goal is to simulate a **real-world data science workflow**—from raw data exploration to actionable business decisions.

---

## 🎯 Objectives

* Understand customer demographics and purchasing behavior
* Perform statistical hypothesis testing on customer segments
* Visualize patterns across income, spending, and campaigns
* Translate data insights into business recommendations

---

## 🧩 App Structure

### 1️⃣ Landing Page

* Project title and overview
* Objective of the analysis
* Brief description of the dataset

---

### 2️⃣ Data Explorer

* Interactive dataset preview
* Filters:

  * Age range
  * Income range
  * Other demographic attributes
* Summary statistics:

  * Mean
  * Median
  * Distribution counts

---

### 3️⃣ Hypothesis Testing Panel

Perform statistical testing dynamically based on selected inputs.

#### 🔧 Features:

* Dropdown selectors for:

  * Income group
  * Education
  * Campaign response
  * Marital status

* Button-triggered test execution

#### 📊 Output Includes:

* Selected test type:

  * Z-test
  * T-test
  * ANOVA
  * Chi-square
* Null and alternative hypotheses
* Test statistic value
* P-value
* Final conclusion:

  > “Significant difference found …” or “No significant evidence …”

---

### 4️⃣ Visualization Section


#### 📈 Available Plots:

* Histogram (distribution analysis)
* Boxplot (outlier & spread detection)
* Grouped bar charts (comparative analysis)
* Correlation heatmap (feature relationships)

#### ⚙️ Features:

* Real-time filtering
* Transparent Plotly charts aligned with UI theme
* Glassmorphism-based card layout for premium UI

---

### 5️⃣ Interpretation & Insights

This section bridges **data science → business impact**.

#### 🧠 Includes:

* Text-based interpretation of statistical outputs
* Insight summaries for each visualization
* Business-focused recommendations

#### 💼 Example:

> “Customers with higher income show significantly greater spending, indicating an opportunity for premium targeting strategies.”

---

## 🛠️ Tech Stack

* **Frontend & App Framework:** Streamlit
* **Data Processing:** Pandas, NumPy
* **Statistical Analysis:** SciPy
* **Visualization:** Plotly
* **Styling:** Custom CSS (Glassmorphism UI)

---

## ✨ Key Features

* Fully interactive dashboard
* Real-time filtering and updates
* Integrated statistical testing engine
* Modern **glassmorphism UI design**
* Clean separation of analysis and interpretation

---

## 📂 Dataset

* Customer Personality Analysis Dataset
* Includes:

  * Demographics (Age, Income, Education, Marital Status)
  * Purchase behavior
  * Campaign responses
  * Web/store activity

---

## ▶️ How to Run Locally

```bash
# Clone repository
git clone <your-repo-link>

# Navigate to project folder
cd <project-folder>

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py
```

---


## Click ⬇ for App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://customerpersonality.streamlit.app/)
