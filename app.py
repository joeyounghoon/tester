import streamlit as st

if st.button("optimalbot"):
    st.switch_page("app.py")
if st.button("선픽"):
    st.switch_page("pages/선픽.py")
if st.button("후픽"):
    st.switch_page("pages/후픽.py")
