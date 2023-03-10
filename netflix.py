import streamlit as st
import pandas as pd


st.title('Netflix Activty - Esteban de la Maza Castro A01720548')

DATA_URL = 'movies.csv'


@st.cache
def load_data(nrows):
    return pd.read_csv(DATA_URL, nrows=nrows)


def filter_data_by_film(film):
    return data[data['name'].str.lower().str.contains(film)]


def filter_data_by_director(director):
    return data[data['director'] == director]


with st.spinner('Loading data...'):
    data = load_data(1000)
    st.success('Done!')

if st.sidebar.checkbox('Show all films'):
    st.subheader('All Films')
    st.dataframe(data)


filmTitle = st.sidebar.text_input('Film title:')
btnFilterTitle = st.sidebar.button('Search')

if btnFilterTitle:
    data_film = filter_data_by_film(filmTitle.lower())
    count_row = data_film.shape[0]
    st.metric(label="Total Films", value=count_row)
    st.dataframe(data_film)


selected_director = st.sidebar.selectbox(
    "Select Director", data['director'].unique())
btnFilterbyDirector = st.sidebar.button('Filter director ')

if btnFilterbyDirector:
    filterbydir = filter_data_by_director(selected_director)
    count_row = filterbydir.shape[0]
    st.metric(label="Total Films", value=count_row)
    st.dataframe(filterbydir)
