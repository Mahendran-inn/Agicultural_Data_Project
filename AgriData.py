#Loading data
import pandas as pd

data=pd.read_csv("ICRISAT-District Level Data - ICRISAT-District Level Data - Copy.csv")
df=data.copy() # copy the data

df.info() # shows the summary
#it is clean,no need for any cleaning 


#i have separated cleaned dataset into 2 df
    #df_main -- Main dataset for EDA analysis & SQL Queries & Power BI (containes main columns for performist project questions)
    #df_removed -- It containes removed columns for performing streamlit web view (not listed in project)
col_removed=['State Code','State Name','Dist Code','Dist Name','Year','BARLEY AREA (1000 ha)','BARLEY PRODUCTION (1000 tons)','BARLEY YIELD (Kg per ha)','CHICKPEA AREA (1000 ha)','CHICKPEA PRODUCTION (1000 tons)','CHICKPEA YIELD (Kg per ha)','PIGEONPEA AREA (1000 ha)','PIGEONPEA PRODUCTION (1000 tons)','PIGEONPEA YIELD (Kg per ha)','MINOR PULSES AREA (1000 ha)','MINOR PULSES PRODUCTION (1000 tons)','MINOR PULSES YIELD (Kg per ha)','SESAMUM AREA (1000 ha)','SESAMUM PRODUCTION (1000 tons)','SESAMUM YIELD (Kg per ha)','RAPESEED AND MUSTARD AREA (1000 ha)','RAPESEED AND MUSTARD PRODUCTION (1000 tons)','RAPESEED AND MUSTARD YIELD (Kg per ha)','SAFFLOWER AREA (1000 ha)','SAFFLOWER PRODUCTION (1000 tons)','SAFFLOWER YIELD (Kg per ha)','CASTOR AREA (1000 ha)','CASTOR PRODUCTION (1000 tons)','CASTOR YIELD (Kg per ha)','LINSEED AREA (1000 ha)','LINSEED PRODUCTION (1000 tons)','LINSEED YIELD (Kg per ha)','FRUITS AREA (1000 ha)','VEGETABLES AREA (1000 ha)','FRUITS AND VEGETABLES AREA (1000 ha)','POTATOES AREA (1000 ha)','ONION AREA (1000 ha)','FODDER AREA (1000 ha)']
df_removed=df[col_removed]

df_main=df.drop(columns=['BARLEY AREA (1000 ha)','BARLEY PRODUCTION (1000 tons)','BARLEY YIELD (Kg per ha)','CHICKPEA AREA (1000 ha)','CHICKPEA PRODUCTION (1000 tons)','CHICKPEA YIELD (Kg per ha)','PIGEONPEA AREA (1000 ha)','PIGEONPEA PRODUCTION (1000 tons)','PIGEONPEA YIELD (Kg per ha)','MINOR PULSES AREA (1000 ha)','MINOR PULSES PRODUCTION (1000 tons)','MINOR PULSES YIELD (Kg per ha)','SESAMUM AREA (1000 ha)','SESAMUM PRODUCTION (1000 tons)','SESAMUM YIELD (Kg per ha)','RAPESEED AND MUSTARD AREA (1000 ha)','RAPESEED AND MUSTARD PRODUCTION (1000 tons)','RAPESEED AND MUSTARD YIELD (Kg per ha)','SAFFLOWER AREA (1000 ha)','SAFFLOWER PRODUCTION (1000 tons)','SAFFLOWER YIELD (Kg per ha)','CASTOR AREA (1000 ha)','CASTOR PRODUCTION (1000 tons)','CASTOR YIELD (Kg per ha)','LINSEED AREA (1000 ha)','LINSEED PRODUCTION (1000 tons)','LINSEED YIELD (Kg per ha)','FRUITS AREA (1000 ha)','VEGETABLES AREA (1000 ha)','FRUITS AND VEGETABLES AREA (1000 ha)','POTATOES AREA (1000 ha)','ONION AREA (1000 ha)','FODDER AREA (1000 ha)'])


# Renaming df_main columns for easy calling
df_main.rename(columns={
    'Dist Code': 'Distcode',
    'State Name': 'Statename',
    'State Code': 'Statecode',
    'Dist Name': 'Distname',
    'RICE AREA (1000 ha)': 'Rice_area',
    'RICE PRODUCTION (1000 tons)': 'Rice_production',
    'RICE YIELD (Kg per ha)': 'Rice_yield',
    'WHEAT AREA (1000 ha)': 'Wheat_area',
    'WHEAT PRODUCTION (1000 tons)': 'Wheat_production',
    'WHEAT YIELD (Kg per ha)': 'Wheat_yield',
    'KHARIF SORGHUM AREA (1000 ha)': 'Kharif_sorghum_area',
    'KHARIF SORGHUM PRODUCTION (1000 tons)': 'Kharif_sorghum_production',
    'KHARIF SORGHUM YIELD (Kg per ha)': 'Kharif_sorghum_yield',
    'RABI SORGHUM AREA (1000 ha)': 'Rabi_sorghum_area',
    'RABI SORGHUM PRODUCTION (1000 tons)': 'Rabi_sorghum_production',
    'RABI SORGHUM YIELD (Kg per ha)': 'Rabi_sorghum_yield',
    'SORGHUM AREA (1000 ha)': 'Sorghum_area',
    'SORGHUM PRODUCTION (1000 tons)': 'Sorghum_production',
    'SORGHUM YIELD (Kg per ha)': 'Sorghum_yield',
    'PEARL MILLET AREA (1000 ha)': 'Pearl_millet_area',
    'PEARL MILLET PRODUCTION (1000 tons)': 'Pearl_millet_production',
    'PEARL MILLET YIELD (Kg per ha)': 'Pearl_millet_yield',
    'MAIZE AREA (1000 ha)': 'Maize_area',
    'MAIZE PRODUCTION (1000 tons)': 'Maize_production',
    'MAIZE YIELD (Kg per ha)': 'Maize_yield',
    'FINGER MILLET AREA (1000 ha)  ': 'Finger_millet_area',
    'FINGER MILLET PRODUCTION (1000 tons)': 'Finger_millet_production',
    'FINGER MILLET YIELD (Kg per ha)': 'Finger_millet_yield',
    'GROUNDNUT AREA (1000 ha)': 'Groundnut_area',
    'GROUNDNUT PRODUCTION (1000 tons)': 'Groundnut_production',
    'GROUNDNUT YIELD (Kg per ha)': 'Groundnut_yield',
    'SUNFLOWER AREA (1000 ha)': 'Sunflower_area',
    'SUNFLOWER PRODUCTION (1000 tons)': 'Sunflower_production',
    'SUNFLOWER YIELD (Kg per ha)': 'Sunflower_yield',
    'SOYABEAN AREA (1000 ha)': 'Soyabean_area',
    'SOYABEAN PRODUCTION (1000 tons)': 'Soyabean_production',
    'SOYABEAN YIELD (Kg per ha)': 'Soyabean_yield',
    'OILSEEDS AREA (1000 ha)': 'Oilseeds_area',
    'OILSEEDS PRODUCTION (1000 tons)': 'Oilseeds_production',
    'OILSEEDS YIELD (Kg per ha)': 'Oilseeds_yield',
    'SUGARCANE AREA (1000 ha)': 'Sugarcane_area',
    'SUGARCANE PRODUCTION (1000 tons)': 'Sugarcane_production',
    'SUGARCANE YIELD (Kg per ha)': 'Sugarcane_yield',
    'COTTON AREA (1000 ha)': 'Cotton_area',
    'COTTON PRODUCTION (1000 tons)': 'Cotton_production',
    'COTTON YIELD (Kg per ha)': 'Cotton_yield',
}, inplace=True)

#optional, will help to create csv file
df_main.to_csv('Agri_cleaned_dataset.csv',index=False)

#insert the data in database
from sqlalchemy import create_engine

host= "localhost"
username= "postgres"
password= 1234567890
port= 5432
database= "Demo_Database"
engine_string = f"postgresql://{username}:{password}@{host}:{port}/{database}"
connection=create_engine(engine_string)
df_main.to_sql("AgriData_Explorer",connection,if_exists="replace")
df_removed.to_sql("AgriData_Filtered",connection,if_exists="replace")
print('Data loaded successfully.') #just confirmation whether above is executed or not


import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import psycopg2 #this will connect vs code with PostgreSQL

# Function to fetch data from PostgreSQL
def fetch_data(query):
    conn = psycopg2.connect(
        host= "localhost",
        user= "postgres",
        password= "1234567890",
        port= 5432,
        database= "Demo_Database",
    )
    cur = conn.cursor()
    cur.execute(query)
    results = cur.fetchall()
    #this line will show the column name
    colnames = [desc[0] for desc in cur.description]  # type: ignore
    cur.close()
    conn.close()
    #return results
    return pd.DataFrame(results, columns=colnames)

#page configuration for streamlit to view as dashboared
st.set_page_config(page_title="Agricultural Data Dashboard", layout="wide")
st.title("Agricultural Data Dashboard")
st.markdown("AgriData Table")
query='select * from "AgriData_Filtered"'
df_agri=fetch_data(query)
st.dataframe(df_agri, use_container_width=True)


st.subheader("EDA Visuals")

selected_query = st.selectbox('Select any EDA question:', [
    "Top 7 RICE PRODUCTION State Data (Bar Plot)",
    "Chickpea Yield Trend Over the Years",
    "Correlation between Barley Area and Production",
    "Top 5 Mustard Producing States (Latest Year)",
    "District with Highest Potato Area (Latest Year)"
])

if st.button("Run Visualization"):
    
    if selected_query == "Top 7 RICE PRODUCTION State Data (Bar Plot)":
        rice_state = df.groupby('State Name')['RICE PRODUCTION (1000 tons)'].sum().nlargest(7)
        fig, ax = plt.subplots(figsize=(10, 6))
        rice_state.plot(kind='bar', color='green', ax=ax)
        ax.set_title("Top 7 Rice Producing States")
        ax.set_ylabel("Rice Production (1000 tons)")
        ax.set_xlabel("State")
        st.pyplot(fig)

    elif selected_query == "Chickpea Yield Trend Over the Years":
        chickpea_yield = df.groupby('Year')['CHICKPEA YIELD (Kg per ha)'].mean().reset_index()
        fig = px.line(chickpea_yield, x='Year', y='CHICKPEA YIELD (Kg per ha)',
                      title='Chickpea Yield Trend in India (Kg/ha)', markers=True)
        st.plotly_chart(fig)

    elif selected_query == "Correlation between Barley Area and Production":
        fig, ax = plt.subplots()
        sns.scatterplot(
            data=df,
            x='BARLEY AREA (1000 ha)',
            y='BARLEY PRODUCTION (1000 tons)',
            alpha=0.5,
            ax=ax
        )
        ax.set_title("Barley Area vs Production")
        st.pyplot(fig)
        corr_val = df['BARLEY AREA (1000 ha)'].corr(df['BARLEY PRODUCTION (1000 tons)'])
        st.write(f"**Correlation Coefficient:** {corr_val:.2f}")

    elif selected_query == "Top 5 Mustard Producing States (Latest Year)":
        latest_year = df['Year'].max()
        mustard_state = df[df['Year'] == latest_year].groupby('State Name')['RAPESEED AND MUSTARD PRODUCTION (1000 tons)'].sum().nlargest(5)
        fig, ax = plt.subplots(figsize=(10, 6))
        mustard_state.plot(kind='bar', color='orange', ax=ax)
        ax.set_title(f"Top 5 Mustard Producing States in {latest_year}")
        ax.set_ylabel("Mustard Production (1000 tons)")
        ax.set_xlabel("State")
        st.pyplot(fig)

    elif selected_query == "District with Highest Potato Area (Latest Year)":
        latest_year = df['Year'].max()
        potato_district = df[df['Year'] == latest_year].groupby('Dist Name')['POTATOES AREA (1000 ha)'].sum().reset_index()
        top_districts = potato_district.sort_values(by='POTATOES AREA (1000 ha)', ascending=False).head(5)

        st.subheader(f"Top 5 Districts by Potato Area in {latest_year}")
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(top_districts['Dist Name'], top_districts['POTATOES AREA (1000 ha)'], color='purple')
        ax.set_title("Top 5 Potato Growing Districts")
        ax.set_xlabel("District")
        ax.set_ylabel("Potato Area (1000 ha)")
        plt.xticks(rotation=45)
        st.pyplot(fig)


#Now Answer Time for EDA:

# 1.Top 7 RICE PRODUCTION State Data(Bar_plot) 
rice_state = df_main.groupby('Statename')['Rice_production'].sum().nlargest(7)
rice_state.plot(kind='bar', title='Top 7 Rice Producing States', ylabel='Production (tonnes)', figsize=(10, 6), color='green')
plt.show()


# 2.Top 5 Wheat Producing States Data(Bar_chart)and its percentage(%)(Pie_chart) 
wheat_state = df_main.groupby('Statename')['Wheat_production'].sum().nlargest(5)

# Bar chart
wheat_state.plot(kind='bar', title='Top 5 Wheat Producing States', ylabel='Production', figsize=(8, 5), color='orange')
plt.show()

# Pie chart with % values
wheat_state.plot(kind='pie', autopct='%1.1f%%', title='Wheat Production Share (%)', figsize=(6, 6))
plt.ylabel('')
plt.show()


# 3.Oil seed production by top 5 states 
oil_states = df_main.groupby('Statename')['Oilseeds_production'].sum().nlargest(5)
sns.barplot(x=oil_states.values, y=oil_states.index, palette='copper')
plt.title("Top 5 States in Oilseed Production")
plt.xlabel("Production")
plt.show()


# 4.Top 7 SUNFLOWER PRODUCTION  State 
sun_states = df_main.groupby('Statename')['Sunflower_production'].sum().nlargest(7)
sun_states.plot(kind='barh', title='Top 7 Sunflower Producing States', color='goldenrod')
plt.xlabel('Production')
plt.show()


# 5.India's SUGARCANE PRODUCTION From Last 50 Years(Line_plot) 
sugar_trend = df_main.groupby('Year')['Sugarcane_production'].sum()
sugar_trend.plot(title='India’s Sugarcane Production (50 Years)', figsize=(10, 5), color='purple')
plt.ylabel('Production')
plt.grid()
plt.show()


# 6.Rice Production Vs Wheat Production (Last 50y)
trend = df_main.groupby('Year')[['Rice_production', 'Wheat_production']].sum()
trend.plot(title='Rice vs Wheat Production (50 Years)', figsize=(10, 6))
plt.ylabel('Production')
plt.grid()
plt.show()


# 7.Rice Production By West Bengal Districts 
wb_rice = df_main[df_main['Statename'] == 'West Bengal'].groupby('Distname')['Rice_production'].sum().sort_values(ascending=False)
wb_rice.plot(kind='bar', figsize=(12, 5), title='Rice Production by Districts in West Bengal', color='teal')
plt.ylabel('Production')
plt.xticks(rotation=90)
plt.show()


# 8.Top 10 Wheat Production Years From UP 
up_wheat = df_main[df_main['Statename'] == 'Uttar Pradesh'].groupby('Year')['Wheat_production'].sum().nlargest(10)
up_wheat.plot(kind='bar', title='Top 10 Wheat Production Years (UP)', color='maroon')
plt.ylabel('Production')
plt.show()


# 9.Millet Production (Last 50y) 
millet = df_main.groupby('Year')[['Sorghum_production', 'Pearl_millet_production', 'Finger_millet_production']].sum()
millet.plot(title='Millet Production Over 50 Years', figsize=(10, 6))
plt.ylabel('Production')
plt.grid()
plt.show()


# 10.Sorghum Production (Kharif and Rabi) by Region 
sorghum = df_main.groupby('Statename')[['Kharif_sorghum_production', 'Rabi_sorghum_production']].sum()
sorghum.nlargest(10, 'Kharif_sorghum_production').plot(kind='bar', stacked=True, figsize=(10, 6), title='Kharif Sorghum vs Rabi Sorghum Production by State')
plt.ylabel('Production')
plt.show()


# 11.Top 7 States for Groundnut Production 
groundnut = df_main.groupby('Statename')['Groundnut_production'].sum().nlargest(7)
sns.barplot(y=groundnut.index, x=groundnut.values, palette='magma')
plt.title("Top 7 States in Groundnut Production")
plt.xlabel("Production")
plt.show()


# 12.Soybean Production by Top 5 States and Yield Efficiency 
soy = df_main.groupby('Statename')[['Soyabean_production', 'Soyabean_yield']].sum().nlargest(5, 'Soyabean_production')
fig, ax1 = plt.subplots()

# Bar plot
soy['Soyabean_production'].plot(kind='bar', ax=ax1, color='olive', label='Production')
ax1.set_ylabel('Production')
ax1.set_title('Top 5 Soybean Producing States and Yield')
ax2 = ax1.twinx()

# Line plot for yield
soy['Soyabean_yield'].plot(color='blue', marker='o', ax=ax2, label='Yield')
ax2.set_ylabel('Yield')

plt.legend()
plt.show()


# 13.Oilseed Production in Major States 
major_oil = df_main.groupby('Statename')['Oilseeds_production'].sum().sort_values(ascending=False).head(10)
sns.barplot(x=major_oil.values, y=major_oil.index, palette='summer')
plt.title("Oilseed Production in Major States")
plt.xlabel("Production")
plt.show()


# 14.Impact of Area Cultivated on Production (Rice, Wheat, Maize) 
sns.scatterplot(data=df_main, x='Rice_area', y='Rice_production', label='Rice')
sns.scatterplot(data=df_main, x='Wheat_area', y='Wheat_production', label='Wheat')
sns.scatterplot(data=df_main, x='Maize_area', y='Maize_production', label='Maize')
plt.title('Area vs Production')
plt.legend()
plt.show()


# 15.Rice vs. Wheat Yield Across States
yield_state = df_main.groupby('Statename')[['Rice_yield', 'Wheat_yield']].mean()
yield_state.plot(kind='bar', figsize=(12, 6), title='Rice vs Wheat Yield Across States')
plt.ylabel('Yield (Kg/Ha)')
plt.xticks(rotation=90)
plt.grid()
plt.show()
