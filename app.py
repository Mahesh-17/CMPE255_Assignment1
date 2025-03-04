import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import folium
from folium.plugins import HeatMap  # type: ignore
from google.cloud import bigquery
from google.oauth2 import service_account
from streamlit_folium import folium_static


credentials_path = st.secrets["gcp"]["credentials_path"]


credentials = service_account.Credentials.from_service_account_file(credentials_path)
client = bigquery.Client(credentials=credentials, project=credentials.project_id)

@st.cache_data
def load_data():
    query = """
    SELECT * FROM `concise-emblem-452601-s2.crash_data.crash_data_2022_present`
    """
    return client.query(query).to_dataframe()


df = load_data()


st.title("San Jose Crash Data Analysis (2022-Present)")


st.sidebar.header("Filters")
severity_filter = st.sidebar.multiselect("Select Injury Severity", ["Fatal", "Severe", "Moderate", "Minor"])
weather_filter = st.sidebar.multiselect("Select Weather Condition", df['Weather'].unique())


filtered_df = df.copy()

if severity_filter:
    severity_columns = {
        "Fatal": "FatalInjuries",
        "Severe": "SevereInjuries",
        "Moderate": "ModerateInjuries",
        "Minor": "MinorInjuries"
    }
    selected_columns = [severity_columns[severity] for severity in severity_filter if severity in severity_columns]
    filtered_df = filtered_df[filtered_df[selected_columns].gt(0).any(axis=1)]

if weather_filter:
    filtered_df = filtered_df[filtered_df['Weather'].isin(weather_filter)]

# Visualization 1: Bar Chart (Crash Severity)
st.subheader("Distribution of Crash Severity")
severity_counts = filtered_df[['FatalInjuries', 'SevereInjuries', 'ModerateInjuries', 'MinorInjuries']].sum()
st.bar_chart(severity_counts)

# Visualization 2: Heatmap (Crash Locations)
st.subheader("Crash Locations Heatmap")
san_jose_map = folium.Map(location=[37.3382, -121.8863], zoom_start=12)
heat_data = filtered_df[['Latitude', 'Longitude']].values.tolist()
HeatMap(heat_data).add_to(san_jose_map)
folium_static(san_jose_map)

# Visualization 3: Line Chart (Weather Impact)
st.subheader("Number of Crashes by Weather Condition")
weather_counts = filtered_df['Weather'].value_counts()
st.line_chart(weather_counts)
