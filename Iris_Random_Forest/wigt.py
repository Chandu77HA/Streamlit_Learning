import streamlit as st

st.title("WIDGETS")

if st.button("Subscribe"):
    st.write("Like this video too")

name = st.text_input("Name")
st.write(name)

address = st.text_area("Enter your address")
st.write(address)

st.date_input("enter a date")

st.time_input("enter a time")

if st.checkbox("you accept the T&C",value = True):
    st.write("Thank you")

v1 = st.radio("Colours",["r","g","b"],index = 1)
v2 = st.selectbox("Colours",["r","g","b"],index = 0)

st.write(v1,v2)

v3 = st.multiselect("Colours",["r","g","b"])
st.write(v3)

st.slider("age",min_value = 18,max_value=60,value = 30,step = 2)

st.number_input("numbers",min_value = 18,max_value=60,value = 30,step = 2)

img = st.file_uploader("Upload a file")

import streamlit as st
from PIL import Image
import io

# Upload an image file
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    try:
        # Convert to PIL Image
        img = Image.open(uploaded_file)
        if img is None:
            st.error("Failed to load image. Please upload a valid image file.")
        else:
            st.image(img, caption="Uploaded Image")
    except Exception as e:
        st.error(f"Error: {e}")
