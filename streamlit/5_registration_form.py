import streamlit as st
import datetime
st.header("student registration form")
my_form=st.form(key='form_1')
fname=my_form.text_input("student first name")
lname=my_form.text_input("student last name")
email=my_form.text_input("student email")
mobile=my_form.number_input("student mobile number")
gender=my_form.radio('gender',('male','female'))
age=my_form.slider("AGE",1,100)
dob=my_form.date_input("enter date of birth",min_value=datetime.date(1990,1,1))
address=my_form.text_area("enter address")
resume=my_form.file_uploader("upload your resume")
my_form.form_submit_button("submit")

st.write("first name:",fname)
st.write("last name:",lname)
st.write("email id:",email)
st.write("gender:",gender)
st.write("mobile:",mobile)
st.write("age:",age)
st.write("DOB:",dob)
st.write("address:",address)




