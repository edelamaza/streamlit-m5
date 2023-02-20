import streamlit as st
import pandas as pd

st.title("Search Names Example VS 1.0")

DATA_URL = 'dataset.csv'


@st.cache
def load_data_by_name(name):
    data = pd.read_csv(DATA_URL)
    filtered_data_by_name = data[data['name'].str.contains(name)]
    return filtered_data_by_name


myName = st.text_input("What is your name?")
if (myName):
    filterbyname = load_data_by_name(myName)
    count_row = filterbyname.shape[0]
    st.write(f"Result : {count_row} rows")

    st.dataframe(filterbyname)
