import streamlit as st
import pandas as pd
#import pyodbc You will need this in the actual implementation

st.markdown(
    """
    <style>
        .stApp {
            background-color: #fff9b0;
        }

        .fade-in {
        animation: fadeIn 2s;
        -webkit-animation: fadeIn 2s;
        -moz-animation: fadeIn 2s;
        -o-animation: fadeIn 2s;
        -ms-animation: fadeIn 2s;
        }

        @keyframes fadeIn {
        0% {opacity:0;}
        100% {opacity:1;}
        }

         @keyframes growIn {
        from {
            transform: scale(0.8);
            opacity: 0;
        }
        to {
            transform: scale(1);
            opacity: 1;
        }
    }

    .grow-in {
        animation: growIn 0.6s ease-out;
    }
    </style>

    <div style='text-align: center;'>
        <h1 class='grow-in'>Database Upload</h1>
    </div>
    """,
    unsafe_allow_html=True
)

if "uploaded_df" in st.session_state:
    df = st.session_state["uploaded_df"]
    # Show column selection
    st.subheader("Select Columns to Display")
    selected_columns = st.multiselect("Choose columns", df.columns.tolist(), default=df.columns.tolist())
    st.dataframe(df[selected_columns])


    # You will need all this in the actual implementation with the SQL Server database
    
    # secrets = st.secrets["database"]

    #Set up connection to database
    # conn = pyodbc.connect(
    #     f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    #     f'SERVER={secrets.server};'
    #     f'DATABASE={secrets.database};'
    #     f'UID={secrets.username};'
    #     f'PWD={secrets.password}'
    # )

    # result = conn.execute("SELECT * FROM your_table_name LIMIT 1")
    # cols = list(result.keys())
    # df_cols = df.columns.tolist()
    # if df_cols==cols:
    #     # Insert database into SQL
    #     df.to_sql(df, con=conn, if_exists='append', index=False)
    # else:
    #     st.warning("Column names must match for proper insert")


else:
    st.warning("Please upload a file first on the Upload page.")

