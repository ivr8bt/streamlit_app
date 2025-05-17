import streamlit as st
import pandas as pd
#import pyodbc You will need this in the actual implementation

st.title("Database Upload")


if "uploaded_df" in st.session_state:
    df = st.session_state["uploaded_df"]
    # Show column selection
    st.subheader("Select Columns to Display")
    selected_columns = st.multiselect("Choose columns", df.columns.tolist(), default=df.columns.tolist())
    st.dataframe(df[selected_columns])


    # You will need all this in the actual implementation with the SQL Server database
    
    # secrets = st.secrets["database"]

    # conn = pyodbc.connect(
    #     f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    #     f'SERVER={secrets.server};'
    #     f'DATABASE={secrets.database};'
    #     f'UID={secrets.username};'
    #     f'PWD={secrets.password}'
    # )

else:
    st.warning("Please upload a file first on the Upload page.")

