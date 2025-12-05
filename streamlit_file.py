# STREAMLIT IS A PYTHON LIBRARY TO CREATE WEB APPS FOR DATA PROJECTS - WITHOUT NEEDING HTML,CSS AND JAVASCRIPT.
# IT TURNS YOUR PYTHON SCRIPTS INTO INTERACTIVE WEB APPS JUST BY RUNNING A SCRIPTS.

# create the simple web app:-

import streamlit as st

st.title("My First Streamlit App")
st.header("Welcome to the Demo App")
st.write("This is a simple app built with Streamlit!")

name = st.text_input("What is your name?")

if name:
    st.success(f"Hello! {name}.")

age = st.slider("Select your age", 1, 100, 25)
st.write("You selected", age)


