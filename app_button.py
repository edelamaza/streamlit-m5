import streamlit as st

myname = st.text_input("What is your name?")
if st.button('Search'):
    st.write(f"Hello {myname}")
