import streamlit as st


st.title("Rent Payment Tracker")
st.write("A simple Python project for a property management capstone milestone.")

name = st.text_input("What is your name?")
if name:
    st.write(f"Hello, {name}! Streamlit is working.")
