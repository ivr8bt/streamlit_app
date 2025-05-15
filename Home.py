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

col1, col2, col3 = st.columns([1, 6, 1])
with col2:
    st.title("Welcome to Sabra Health Analysis App")

st.write("Use the sidebar to navigate between pages.")

st.image("images/test_image.jpg")