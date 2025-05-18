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

    # Insert database into SQL
    # df.to_sql(df, con=conn, if_exists='append', index=False)

    #Checking columns names
    col_names = ['entity', 'account', 'dataSource', 'value', 'timeID', 'createDate', 'updatedAt']
    df_cols=list(df.columns)
    difference = list(set(col_names) - set(df_cols))
    difference2 = list(set(df_cols) - set(col_names))
    if difference:
        st.warning(f'Missing columns {difference}')
        n = st.selectbox("Would like to add in null values for these columns?", ["Yes","No"])
        if n=='Yes':
            for col in difference:
                df[col] = [None] * len(df)
            df=df[col_names]
        else:
            # Sends warning and then stops execution because .csv must be changed before insertion
            st.warning("Change column names in .csv before database insertion")
            st.stop()
    elif difference2:
        st.warning(f'Extra columns {difference2}')
        # If there are columns missing then they should already be dealt with
        # If there are extra columns this will get rid of them
        df=df[col_names]

    # Checking columns types 
    expected_types=[str,int,str,float,str,str,str]

    def validate_column_types(df, expected) -> bool:
        message=False
        for col, expected in zip(df.columns, expected):
            for i, val in enumerate(df[col]):
                if pd.isnull(val):
                    continue  # Acceptable null value
                if not isinstance(val, expected):
                    print(
                        st.warning(f"Type mismatch in column '{col}': expected {expected.__name__}, got {type(val).__name__}")
                    )
                    message=True
                    break
        if message:
            return True
        
    if validate_column_types(df,expected_types):
        st.warning("Fix type mismatch")
        st.stop()
    else:
        # Change string to datetime before SQL insertion
        df['timeID'] = pd.to_datetime(df['timeID'])
        df['createDate'] = pd.to_datetime(df['createDate'])
        df['updatedAt'] = pd.to_datetime(df['updatedAt'])
        # Insert database into SQL
        # df.to_sql(df, con=conn, if_exists='append', index=False)


else:
    st.warning("Please upload a file first on the Upload page.")

