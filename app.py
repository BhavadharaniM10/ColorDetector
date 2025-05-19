import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from streamlit_drawable_canvas import st_canvas

# Page config
st.set_page_config(page_title="Color Detection from Image 🎨", layout="centered")

# Custom CSS
st.markdown("""
<style>
    .title {
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        color: #555;
        margin-bottom: 1rem;
    }
    .color-box {
        border-radius: 10px;
        border: 3px solid #000;
        width: 120px;
        height: 70px;
        margin-top: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🎨 Color Detector from Image</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Upload an image and click to detect the color!</div>', unsafe_allow_html=True)

# Load color data
@st.cache_data
def load_colors():
    return pd.read_csv("colors.csv")

colors_df = load_colors()

def get_closest_color_name(R, G, B):
    min_dist = float("inf")
    cname = "Unknown"
    for i in range(len(colors_df)):
        r, g, b = int(colors_df.loc[i, "r"]), int(colors_df.loc[i, "g"]), int(colors_df.loc[i, "b"])
        d = abs(R - r) + abs(G - g) + abs(B - b)
        if d <= min_dist:
            min_dist = d
            cname = colors_df.loc[i, "color_full_name"]
    return cname

# Upload image
uploaded_file = st.file_uploader("📁 Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    img_width, img_height = image.size
    img_array = np.array(image)

    # Row 1: Uploaded Image
    st.markdown("### 🖼️ Uploaded Image Preview")
    st.image(image, use_column_width=True)

    # Row 2: Canvas + Detected Color
    st.markdown("### ✍️ Click on the Image Below to Detect Color")
    canvas_result = st_canvas(
        fill_color="rgba(0,0,0,0)",
        stroke_width=2,
        stroke_color="#FF0000",
        background_image=image,
        update_streamlit=True,
        height=img_height,
        width=img_width,
        drawing_mode="point",
        key="color_picker_canvas",
    )

    if canvas_result.json_data is not None:
        objects = canvas_result.json_data["objects"]
        if objects:
            last_point = objects[-1]
            left = last_point.get("left", None)
            top = last_point.get("top", None)

            if left is not None and top is not None:
                x = int(left)
                y = int(top)

                if 0 <= x < img_width and 0 <= y < img_height:
                    r, g, b = img_array[y, x]
                    color_name = get_closest_color_name(r, g, b)

                    # Display detected color
                    st.markdown("### 🎯 Detected Color")
                    st.write(f"**Color Name:** `{color_name}`")
                    st.write(f"**RGB Values:** R = `{r}`, G = `{g}`, B = `{b}`")
                    st.markdown(
                        f'<div class="color-box" style="background-color: rgb({r},{g},{b});"></div>',
                        unsafe_allow_html=True,
                    )
