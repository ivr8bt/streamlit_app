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
st.image(resized_img)

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