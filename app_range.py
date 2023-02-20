import streamlit as st
import pandas as pd

st.title("Search names Range")

DATA_URL = 'dataset.csv'


@st.cache
def load_data_by_range(min, max):
    data = pd.read_csv(DATA_URL)
    filtered_data_by_range = data[(
        data['index'] >= min) & (data['index'] <= max)]
    return filtered_data_by_range


minRange = st.number_input("Min", step=1)
maxRange = st.number_input("Max", step=1)
btnRange = st.button('Search by range')

if (btnRange):
    filterbyrange = load_data_by_range(minRange, maxRange)
    count_row = filterbyrange.shape[0]
    st.write(f"Result : {count_row} rows")

    st.dataframe(filterbyrange)
