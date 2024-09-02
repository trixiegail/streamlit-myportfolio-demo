import streamlit as st
import os
from PIL import Image

# Title of the app
st.title("BASTA GALLERY NI WITH MEMORIES")

# Path to the folder containing images
image_folder = 'assets'

# Fetch all image files from the folder
image_files = [os.path.join(image_folder, file) for file in os.listdir(image_folder) if file.endswith(('png', 'JPG', 'jpeg', 'gif'))]

# Display images in a grid format
st.subheader("Photo Gallery")

cols = st.columns(3)  # Display 3 images per row

for index, image_file in enumerate(image_files):
    img = Image.open(image_file)
    
    # Place image in the appropriate column
    with cols[index % 3]:
        st.image(img, caption=os.path.basename(image_file), use_column_width=True)

# Additional custom styling for the gallery
st.markdown(
    """
    <style>
    .stImage img {
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        transition: transform 0.2s;
    }
    .stImage img:hover {
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Optional: Add a footer or additional creative elements
st.markdown("---")
st.write("Enjoy the beautiful moments captured in these images!")
