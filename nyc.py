import streamlit as st
import pandas as pd
import numpy as np

st.title('Bike Rides in NYC - Esteban de la Maza Castro A01720548')

DATE_COLUMN = 'started_at'
DATA_URL = 'citibike-tripdata.csv'

tab1, tab2, tab3 = st.tabs(["Raw Data", "Bar Chart", "Map"])


@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    data.rename({'start_lat': 'lat', 'start_lng': 'lon'}, axis=1, inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


with st.spinner('Loading data...'):
    data = load_data(1000)
    st.success("Done! (using st.cache)")

with tab1:
    st.subheader('Raw data')
    st.dataframe(data)

with tab2:
    st.subheader('Number of Pickups by Hour')

    hist_values = np.histogram(
        data[DATE_COLUMN].dt.hour, bins=24, range=(0, 24))[0]
    st.bar_chart(hist_values)


with tab3:
    # Some number in the range 0-23
    hour_to_filter = st.slider('hour', 0, 23, 17)
    filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

    st.subheader('Map of all pickups at %s:00' % hour_to_filter)
    st.map(filtered_data)
