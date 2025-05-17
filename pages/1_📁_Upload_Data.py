import streamlit as st
import pandas as pd

# App title
st.title("Upload your .csv file")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

# If a file is uploaded
if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.session_state["uploaded_df"] = df  # Save the DataFrame to session state
        st.success("File uploaded and saved!")

        num = st.number_input("Enter how many rows you wan to see", min_value=1, max_value=len(df), value=3, step=1)
        st.write("You entered:", num)
        # Show preview of the data
        st.subheader("Preview of Data")
        new_df=df[:num]
        st.dataframe(new_df)

        # Show basic statistics
        st.subheader("Summary Statistics")
        st.write(df.describe())

    except Exception as e:
        st.error(f"An error occurred while reading the file: {e}")
else:
    st.info("Awaiting a CSV file upload...")


