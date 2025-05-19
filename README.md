
### Color Detector from Image

🎨 Color Detector from Image is a Streamlit web app that allows users to upload an image and detect the color of any clicked point on the image. It uses OpenCV for image processing and a colors dataset (`colors.csv`) from Kaggle to match and display the closest color name along with its RGB values.

---

## Features

- Upload JPG, JPEG, or PNG images.  
- Click anywhere on the uploaded image to detect the color at that pixel.  
- Displays the closest color name from the dataset along with the exact RGB values.  
- Shows a color preview block for easy visualization.  

---

## Technologies Used

- Python  
- Streamlit  
- OpenCV (`cv2`)  
- Pandas  
- Numpy  
- Streamlit Drawable Canvas  
- Pillow (PIL)  

---

## Setup and Installation

1. Clone or download this repository.

2. Ensure you have Python 3.7+ installed.

3. Install required packages:

```bash
pip install streamlit opencv-python pandas numpy streamlit-drawable-canvas pillow
````

4. Download the `colors.csv` file from Kaggle and place it in the same directory as `app.py`.

5. Run the app:

```bash
streamlit run app.py
```

---

## Usage

* Open the app in your browser via Streamlit's local URL.
* Upload an image file using the file uploader.
* Click anywhere on the displayed image canvas.
* The app will show the detected color name, its RGB values, and a color preview.

---

## File Description

* **app.py**: Main Streamlit application file containing the color detection logic and UI.
* **colors.csv**: Dataset containing color names and their RGB values used for matching the clicked pixel color.

---

## Notes

* The app uses a simple distance metric (sum of absolute differences) to find the closest color in the dataset.
* The color detection works best on images with clear and distinct colors.
* Make sure the uploaded images are of supported formats and reasonable size for performance.

---

## License

This project is open source and free to use.
