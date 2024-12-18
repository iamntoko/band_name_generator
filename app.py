import streamlit as st

# Welcome message
st.title("Band Name Generator App")

# User input fields
city = st.text_input("What city did you grow you up in?\n")
pet = st.text_input("What is the name of the pet you like?\n")

# Conditional Logic for generating the Band Name
if st.button("Generate Band Name"):
    if city and pet:
        band_name = f"{city} {pet}"
        st.success(f"Your band name is: {band_name}")
    else:
        st.error("Please fill out both fields!")
