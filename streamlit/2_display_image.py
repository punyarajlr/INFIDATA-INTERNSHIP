import streamlit as st
from PIL import Image
img=Image.open('images.jpeg')
img2=Image.open('images (1).jpeg')
st.title('DISPLAYING IMAGE')
st.image(img,width=750)
st.image(img2,width=750)