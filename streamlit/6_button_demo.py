import streamlit as st

animal_shelter=['cat','dog','rabbit','tiger']

animal=st.text_input('type an animal ')

if st.button('check availability'):
    have_it=animal.lower() in animal_shelter
    if(have_it):
        st.info("we have this animal")
    else:
        st.info("we dont have this animal")