import streamlit as st
#import pyodbc

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

 # Show column selection
st.subheader("Select Columns to Display")
selected_columns = st.multiselect("Choose columns", df.columns.tolist(), default=df.columns.tolist())
st.dataframe(df[selected_columns])


# secrets = st.secrets["database"]

# conn = pyodbc.connect(
#     f'DRIVER={{ODBC Driver 17 for SQL Server}};'
#     f'SERVER={secrets.server};'
#     f'DATABASE={secrets.database};'
#     f'UID={secrets.username};'
#     f'PWD={secrets.password}'
# )