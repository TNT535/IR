import streamlit as st
from helper import *

st.set_page_config(page_title='IR System', page_icon=':mag')
st.title("Hệ thống tìm kiếm tin tức bằng tiếng Việt")
user_input = st.sidebar.text_input('Nhập từ khoá muốn tìm kiếm', "Từ khoá")
clicked = st.sidebar.button('Search')
if user_input == '':
    st.sidebar.error("Hãy nhập từ khoá cần tìm kiếm")

if user_input != 'Từ khoá' and user_input != '':
    result = Read_Content(user_input)
    st.success("Đã chạy model xong!")
    pos = 0
    index = 0
    for item in result.items():
        with st.container():
            title = f"### Tên tập tin: {item[0]}"
            st.markdown(title)
            text = item[1].decode('utf-16')
            st.text_area('', text, height=444, key=index)
            index += 1

