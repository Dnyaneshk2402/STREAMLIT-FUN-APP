import streamlit as st

st.title("Innomatics Data science Internship 23")

btn_click = st.button("Click Me!")

if btn_click == True:
    st.subheader("You clicked me :smile:")
    st.balloons()