import streamlit as st
import pandas as pd

# App title
st.title("Upload your .csv file")

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

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

# If a file is uploaded
if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("File uploaded successfully!")

        # Show preview of the data
        st.subheader("Preview of Data")
        st.dataframe(df)

        # Show basic statistics
        st.subheader("Summary Statistics")
        st.write(df.describe())

        # Optional: Show column selection
        st.subheader("Select Columns to Display")
        selected_columns = st.multiselect("Choose columns", df.columns.tolist(), default=df.columns.tolist())
        st.dataframe(df[selected_columns])

        st.line_chart(df[selected_columns])

    except Exception as e:
        st.error(f"An error occurred while reading the file: {e}")
else:
    st.info("Awaiting a CSV file upload...")


