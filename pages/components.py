import streamlit as st
import pandas as pd
import numpy as np

st.button("Click me")
# st.download_button("Download file", [])
st.link_button("Go to gallery", "https://google.com")
st.page_link("app.py", label="Home")
# st.data_editor("Edit data", [])
st.checkbox("I agree")
st.toggle("Enable")
st.radio("Pick one", ["cats", "dogs"])
st.selectbox("Pick one", ["cats", "dogs"])
st.multiselect("Buy", ["milk", "apples", "potatoes"])
st.slider("Pick a number", 0, 100)
st.select_slider("Pick a size", ["S", "M", "L"])
st.text_input("First name")
st.number_input("Pick a number", 0, 10)
st.text_area("Text to translate")
st.date_input("Your birthday")
st.time_input("Meeting time")
st.file_uploader("Upload a CSV")
st.camera_input("Take a picture")
st.color_picker("Pick a color")