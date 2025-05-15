import streamlit as st

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

st.title("Welcome to Sabra Health Analysis App")
st.write("Use the sidebar to navigate between pages.")

st.image("images/test_image.png", use_column_width=True)