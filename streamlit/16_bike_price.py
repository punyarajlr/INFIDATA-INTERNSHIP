import streamlit as st

price=st.number_input("enter the bike price")
if(price>100000):
    tax=price+0.15
    st.write("tax with 15%",tax)
elif(price>50000 and price<=100000):
    tax=price+0.10
    st.write("tax with 10%", tax)
elif(price<=50000):
    tax=price+0.5
    st.write("tax with 5%",tax)