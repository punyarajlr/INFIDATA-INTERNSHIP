import streamlit as st

per=st.number_input("enter the percentage of a student")
if(per>90):
    st.write("grade A")
elif(per>80 and per<=90):
    print("grade B")
elif(per>=60 and per<=80):
    st.write("grade C")
elif(per<60):
    st.write("grade D")