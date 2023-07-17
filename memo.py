import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np

add_selectbox = st.sidebar.selectbox(
    "목차",
    ("검은패딩", "셔츠","흰티 갈색바지","흰티 청바지","검은티 청바지")
)

if add_selectbox == '검은패딩':
    st.header("검은패딩 코디")
    image = Image.open('검패1.jpg')
    st.image(image)
    image = Image.open('검패2.jpg')
    st.image(image)
    image = Image.open('검패3.jpg')
    st.image(image)
    image = Image.open('검패4.jpg')
    st.image(image)
    image = Image.open('검패5.jpg')
    st.image(image)
    image = Image.open('검패6.jpg')
    st.image(image)