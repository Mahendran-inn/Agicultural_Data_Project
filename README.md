# 🌾 Indian Agriculture Crop Analysis Dashboard

This project explores and visualizes agricultural data across Indian districts and states over 50+ years. It uses **Python (Streamlit, Pandas, SQL)** for interactive analysis, and **Power BI** for professional business dashboards.

---

## 🚀 Features

- 📦 Cleaned and transformed crop-wise data (area, production, yield)
- 🔍 EDA using Matplotlib, Seaborn, and Plotly
- 📊 Dual dashboards: Streamlit (web app) and Power BI (business reporting)
- 🔗 PostgreSQL integration via SQLAlchemy and psycopg2
- 📁 Dataset divided for optimized visual tools (Power BI vs Streamlit)

---

## 🧱 Project Structure

agri-data-dashboard/
│
├── data/
│ ├── agri_cleaned_dataset.csv # Cleaned full dataset (Power BI + SQL + EDA use)
│ ├── streamlit_dataset.csv # Trimmed/optimized dataset for Streamlit
│
├── scripts/
│ ├── data_cleaning.py # Cleaning using pandas
│ ├── data_loader.py # PostgreSQL upload via SQLAlchemy & psycopg2
│ ├── eda_visuals.py # Optional reusable EDA functions
│
├── notebooks/
│ └── EDA_analysis.ipynb # Jupyter notebook for visual exploration
│
├── streamlit_app/
│ ├── app.py # Streamlit dashboard app
│ └── components/ # Optional custom modules
│
├── powerbi/
│ ├── agri_dashboard.pbix # Power BI report
│ └── screenshots/ # Power BI visuals for README
│
├── images/
│ └── dashboard_view.png # Streamlit dashboard screenshots
│
├── README.md # Project documentation


---

## 📊 Power BI Dashboard

This project includes a **Power BI dashboard** for powerful data-driven storytelling and high-level insights.

### Key Features:
- 📌 State-wise and district-wise crop analysis
- 🔄 Time-series trends of production, yield, and area
- 📊 Top crops and high-yielding regions
- 🗃️ Filters for crop, year, state, district

🖼️ Sample Power BI Visual:

![Power BI Sample](<img width="766" height="433" alt="image" src="https://github.com/user-attachments/assets/90c8d167-e57c-4594-9b88-47e20445dc8e" />
<img width="763" height="431" alt="image" src="https://github.com/user-attachments/assets/af7347ac-8b37-4228-ac00-14c82304449a" />
)

---

## 🛠️ Tech Stack

| Layer              | Tools/Frameworks |
|-------------------|------------------|
| Language           | Python           |
| Data Cleaning      | pandas           |
| Database           | PostgreSQL       |
| ORM & Connector    | SQLAlchemy + psycopg2 |
| Visualizations     | Matplotlib, Seaborn, Plotly |
| Dashboard UI       | Streamlit        |
| BI Tool            | Power BI         |

---

## 📄 Dataset Overview

| Dataset Used | Purpose                                |
|--------------|----------------------------------------|
| `Agri_cleaned_dataset.csv`  | Used for Power BI, SQL analysis, and Python EDA |
| `Agri_filtered_dataset.csv` | Lightweight version for use in Streamlit        |

---

## 📉 Sample Visualizations (Python)

- ✅ Top 7 rice-producing states (bar chart)
- ✅ Chickpea yield trend over the years (line plot)
- ✅ Correlation between barley area and production (scatter plot)
- ✅ Top 5 mustard-producing states (latest year)
- ✅ District with highest potato area

Implemented using `matplotlib`, `seaborn`, and `plotly`, and rendered interactively using Streamlit.

---

## 🧹 Data Cleaning Highlights

- Removed missing/null values
- Converted units to standard format
- Standardized state/district names
- Converted datatypes for numeric columns
- Renamed columns for readability

---

## 🛢️ PostgreSQL Integration

Data was loaded into a PostgreSQL database for efficient querying:

```python
from sqlalchemy import create_engine
import pandas as pd

engine_string = f"postgresql://{username}:{password}@{host}:{port}/{database}"
connection=create_engine(engine_string)
df_main.to_sql("AgriData_Explorer",connection,if_exists="replace")
