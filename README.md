# 📊 Indian Agriculture Crop Analysis Dashboard

This project is a comprehensive data exploration and visualization dashboard built using **Python**, **Streamlit**, and **PostgreSQL** to analyze district-level agricultural data across India. It provides key insights into crop production, yield trends, and spatial variations over time.

---

## 🚀 Features

- 🔍 Exploratory Data Analysis (EDA) on over 15+ major Indian crops
- 📦 Data cleaning and transformation using **pandas**
- 💾 Data storage and querying with **PostgreSQL** using **SQLAlchemy** and **psycopg2**
- 📉 Visualizations with **Matplotlib**, **Seaborn**, **Plotly**
- 🖥️ Interactive dashboard created with **Streamlit**

---

## 🛠️ Tech Stack

| Layer              | Tools/Frameworks |
|-------------------|------------------|
| Language           | Python           |
| Data Cleaning      | pandas           |
| Database           | PostgreSQL       |
| ORM                | SQLAlchemy       |
| DB Connection      | psycopg2         |
| Visualizations     | Matplotlib, Seaborn, Plotly |
| Dashboard UI       | Streamlit        |

---

## 📁 Project Structure


---

## 📊 Visualizations Included

- 📈 Crop-wise yield trends over 50 years
- 🗺️ State & district-level top producers
- 📉 Correlation between area and production
- 📌 Year-on-year crop performance (bar/line charts)
- 🔄 Comparison across multiple crops (e.g. rice vs wheat)

---

## 🧹 Data Cleaning

- Removed nulls and inconsistencies
- Unified naming conventions for states/districts
- Converted all numeric columns to appropriate dtypes
- Handled missing yield/area/production values
- Renamed and standardized column headers

---

## 🛢️ Database Connection

Data was inserted into PostgreSQL using SQLAlchemy for flexibility and psycopg2 for optimized query execution.

```python
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('postgresql+psycopg2://username:password@localhost:5432/dbname')
df.to_sql('agri_data', engine, index=False, if_exists='replace')


