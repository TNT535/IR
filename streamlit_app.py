import streamlit as st
from helper import *

st.set_page_config(page_title='IR System', page_icon=':mag')
st.title("Hệ thống tìm kiếm tin tức bằng tiếng Việt")
user_input = st.sidebar.text_input('Nhập từ khoá muốn tìm kiếm', "Từ khoá")
clicked = st.sidebar.button('Search')
if user_input == '':
    st.sidebar.error("Hãy nhập từ khoá cần tìm kiếm")

