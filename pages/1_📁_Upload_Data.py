import streamlit as st
import pandas as pd

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
        <h1 class='grow-in'>Upload your .csv file</h1>
    </div>
    """,
    unsafe_allow_html=True
)


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


