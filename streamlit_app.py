import streamlit as st

st.set_page_config(page_title='IR System', page_icon=':mag')
st.title("Hệ thống tìm kiếm tin tức bằng tiếng Việt")
user_input = st.text_input('Nhập từ khoá muốn tìm kiếm', 'Nhập')
clicked = st.button('Search')
if user_input == '':
    st.error("Hãy nhập từ khoá cần tìm kiếm")
else:
    st.write("Từ khoá là", user_input)
