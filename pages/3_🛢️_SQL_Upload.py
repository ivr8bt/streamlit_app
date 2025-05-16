import streamlit as st
import pyodbc

st.markdown(
    """
    <style>
        .stApp {
            background-color: #fff9b0;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Database Upload")

# secrets = st.secrets["database"]

# conn = pyodbc.connect(
#     f'DRIVER={{ODBC Driver 17 for SQL Server}};'
#     f'SERVER={secrets.server};'
#     f'DATABASE={secrets.database};'
#     f'UID={secrets.username};'
#     f'PWD={secrets.password}'
# )