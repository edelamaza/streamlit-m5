import streamlit as st
import pandas as pd

st.title("Filter by sex")

DATA_URL = 'dataset.csv'


@st.cache
def load_data():
    data = pd.read_csv(DATA_URL)
    return data


@st.cache
def load_data_by_sex(sex):
    data = pd.read_csv(DATA_URL)
    filtered_data_by_sex = data[data['sex'] == sex]
    return filtered_data_by_sex


data = load_data()
selected_sex = st.selectbox('Select sex', data['sex'].unique())
btnFilterBySex = st.button('Filter by sex')

if (btnFilterBySex):
    filteredbysex = load_data_by_sex(selected_sex)
    count_row = filteredbysex.shape[0]
    st.write(f"Result : {count_row} rows")
    st.dataframe(filteredbysex)
