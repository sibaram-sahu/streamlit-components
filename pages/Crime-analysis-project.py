import streamlit as st
import pandas as pd
import numpy as np


st.title("Crime analysis in USA")

st.markdown("#### This project used this data, Crime data [click here](https://catalog.data.gov/dataset/crime-data-from-2020-to-present)")


df = pd.read_csv('data/Crime_Data_from_2020_to_Present.csv')

# load data
st.write("City of Los Angeles Crime data from 2020 to present.")

st.write(df.head())

st.text("Updated the time format.")

# Define the conversion function
def convert_to_time(time_str):
    split_result = str(time_str).split(',')
    join_result = "".join(split_result)

    hours = join_result[:2]
    minutes = join_result[2:]

    # Combine hours and minutes with a colon
    return f"{hours}:{minutes}"

# Apply the conversion function to the column
df['TIME OCC'] = df['TIME OCC'].head(5).apply(lambda x: convert_to_time(x))

st.write(df.head())

col1, col2 = st.columns(2)

# count of the crimes as per area
uniqe_area_name = df["AREA NAME"].value_counts()

with col1:
    st.text("Count of crimes in which area?")
    st.write(uniqe_area_name)
    st.bar_chart(uniqe_area_name)
