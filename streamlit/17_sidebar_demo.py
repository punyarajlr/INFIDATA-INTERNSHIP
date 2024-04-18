import streamlit as st

add_selectbox=st.sidebar.selectbox(
    "how would you like to be contacted?",
    ("Email","Home Phone","Mobile Phone")
)
with st.sidebar:
    add_radio = st.radio(
        'choose a shipping method',
        ('standard(5-15days)', 'expess(2-5days)')
    )
    name = st.text_input('enter the customer name:')