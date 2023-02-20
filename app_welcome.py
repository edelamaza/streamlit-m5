import streamlit as st


def welcome(name):
    myMessage = "Hello " + name + "!"
    return myMessage


myName = st.text_input("What is your name?")

if (myName):
    myMessage = welcome(myName)
    st.write(f"Result : {myMessage}")
