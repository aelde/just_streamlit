import streamlit as st

st.header('st.button')

st.button("Say bye", type="primary")
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')