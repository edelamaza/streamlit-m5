import streamlit as st
import numpy as np
import pandas as pd

map_data = pd.DataFrame(
    np.random.randn(1, 2) / [2000, 2000] + [25.643860, -100.407448],
    columns=['lat', 'lon'])

st.map(map_data)
st.dataframe(map_data)
