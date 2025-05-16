import streamlit as st
import pandas as pd
import altair as alt  # or use matplotlib, seaborn, etc.

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

st.title("Plotting Page")

if "uploaded_df" in st.session_state:
    df = st.session_state["uploaded_df"]
    
    # Optional: Show column selection
    st.subheader("Select Columns to Display")
    selected_columns = st.multiselect("Choose columns", df.columns.tolist(), default=df.columns.tolist())
    st.dataframe(df[selected_columns])

    # Example: simple plot
    column = st.selectbox("Select column to plot", df.columns)
    st.bar_chart(df[column])
else:
    st.warning("Please upload a file first on the Upload page.")
