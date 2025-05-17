from PIL import Image
import streamlit as st
import time

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
    </style>

    <div style='text-align: center;'>
        <h1>Welcome to Sabra Health Analysis App</h1>
    </div>
    """,
    unsafe_allow_html=True
)

def type_writer(text, delay=0.05):
    output = ""
    for char in text:
        output += char
        st.markdown(f"<h3 style='font-family:sans-serif;'>{output}</h3>", unsafe_allow_html=True)
        time.sleep(delay)
        st.experimental_rerun()  # Uncomment only if you control the loop

# Basic version (without rerun loop)
typed_text = ""
for char in "Welcome to the Dashboard":
    typed_text += char
    st.markdown(f"<h3 style='font-family:sans-serif;'>{typed_text}</h3>", unsafe_allow_html=True)
    time.sleep(0.05)

st.image("images/test_image.jpg")