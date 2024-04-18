import streamlit as st
name=st.text_input("enter student name")
id=st.number_input("enter student id")
branch=st.text_input("enter the branch name")
test1=st.number_input("enter the 1st test marks")
test2=st.number_input("enter the 2nd test marks")
test3=st.number_input("enter the 3rd test marks")
avg=(test1+test2+test3)/3
st.write("student name",name)
st.write("student id",id)
st.write("student branch",branch)
st.write("student average",avg)


