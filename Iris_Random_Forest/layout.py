import streamlit as st 

st.set_page_config(page_title="Registration", layout="centered", page_icon=":cl")

st.title("Registration Form")



col1, col2 = st.columns(2)

col1.text_input("First Name",value = "first name")

col2.text_input("Second Name")

col3, col4 = st.columns([3, 1])


col3.text_input("Email ID")

col4.text_input("Mob number")

col5 ,col6 ,col7  = st.columns(3)

col5.text_input("Username")

a =col6.text_input("Password", type = "password")

col7.text_input("Repeat Password" , type = "password")

but1,but2,but3 = st.columns([1,4,1])

agree  = but1.checkbox("I Agree")

if but3.button("Submit"):
    if agree:  
        st.success("Done")
    else:
        st.warning("Please Check the T&C box")