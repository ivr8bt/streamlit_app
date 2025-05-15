import streamlit as st

st.markdown(
    """
    <style>
        .stApp {
            background-color: #fff9b0;
        }
    </style>

    <div style='text-align: center;'>
        <h1>Welcome to Sabra Health Analysis App</h1>
        <h3>Use the sidebar to navigate between pages</h3>
    </div>
    """,
    unsafe_allow_html=True
)


st.image("images/test_image.jpg")