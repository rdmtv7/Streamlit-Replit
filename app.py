# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from st_aggrid import AgGrid

# Set page config
st.set_page_config(page_title='Google Ads Summary', layout='wide')

# Function to load data
def load_data():
    try:
        # Example: Load a CSV file from an uploaded file
        uploaded_file = st.file_uploader("Upload your input CSV file", type=["csv"])
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            return df
    except Exception as e:
        st.error(f"An error occurred while loading data: {e}")
        return None

# Function to create a dynamic layout
def create_layout(df):
    col1, col2 = st.columns([3, 2])

    with col1:
        st.subheader('Data Table')
        AgGrid(df)

    with col2:
        st.subheader('Data Visualization')
        # Generate a bar chart for conversions vs. cost per conversion
        if 'Conversions' in df.columns and 'Cost Per Conversion' in df.columns:
            fig = px.bar(df, x='Conversions', y='Cost Per Conversion', 
                         title="Conversions vs. Cost Per Conversion")
            st.plotly_chart(fig)
        else:
            st.error("Required columns are not in the dataframe")

# Main app function
def main():
    df = load_data()

    if df is not None:
        create_layout(df)

if __name__ == '__main__':
    main()
