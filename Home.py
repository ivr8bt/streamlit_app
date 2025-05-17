from PIL import Image
import streamlit as st

# Open and resize the image
img = Image.open("images/Sabra_Logo.png")

# Set a new height and calculate width to maintain aspect ratio
new_height = 200
aspect_ratio = img.width / img.height
new_width = int(new_height * aspect_ratio)

# Resize and display
resized_img = img.resize((new_width, new_height))
col1, col2, col3 = st.columns([1, 1, 1])  # Adjust ratios as needed
with col2:
    st.image(resized_img, use_container_width=False)

st.markdown(
    """
    <style>
        .stApp {
            background-color: #1E1E1E;
            color: white;
        }
    </style>

    <div style='text-align: center;'>
        <h1>Welcome to Sabra Health Analysis App</h1>
    </div>
    """,
    unsafe_allow_html=True
)


st.image("images/test_image.jpg")