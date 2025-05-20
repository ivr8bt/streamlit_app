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
            background-color: #fff9b0;
            secondaryBackgroundColor= #32CD32;
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
    </style>

    <div style='text-align: center;'>
        <title class='fade-in'>Welcome to Sabra Health Analysis App</title>
        <h3>Use the sidebar to navigate between the pages. 
        Start with uploading your .csv file and then you can plot values and upload to SQL Server.</h3>
    </div>
    """,
    unsafe_allow_html=True
    )

st.image("images/test_image.jpg")