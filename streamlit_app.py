import streamlit as st
from helper import *
import time


def token_corpus(text_input):
    tokens = word_tokenize(text_input)
    return tokens


flag = True
evaluate = False

st.set_page_config(page_title='IR System', page_icon=':mag')
st.title("Hệ thống tìm kiếm tin tức bằng tiếng Việt :newspaper:")

st.sidebar.header(":desktop_computer: Tìm kiếm")
user_input = st.sidebar.text_input('Nhập từ khoá muốn tìm kiếm', "Từ khoá", key=1)
clicked = st.sidebar.button('Search')
st.sidebar.info("Xoá từ khoá tìm kiếm trong khung :point_up_2: trước khi lựa chọn từ khoá có sẵn")

st.sidebar.write("Hoặc")
arr = ['Chọn', 'Huế', 'Đà Nẵng', 'query_3', 'query_4', 'query_5',
       'query_6', 'query_7', 'query_8', 'query_9', 'query_10']
option = st.sidebar.selectbox(
    'Chọn những từ khoá đã được chú thích', options=arr)


if (user_input == 'Từ khoá' or user_input == '') and option != 'Chọn':
    user_input = option
    evaluate = True
elif user_input != 'Từ khoá' and user_input != '' or clicked:
    pass
else:
    st.sidebar.error(":x: Hãy nhập từ khoá cần tìm kiếm")
    flag = False

if user_input in arr:
    evaluate = True

start_time = time.time()
if flag:
    result = Read_Content(user_input)
    st.success("Đã chạy model xong! :tada:")
    end_time = time.time()
    st.write(":stopwatch: Top 20 kết quả trả về trong ", round(end_time - start_time, 4), "s")
    pos = 0
    index = 0
    for item in result.items():
        with st.container():
            title = f"### :page_facing_up: Tên tập tin: {item[0]}"
            st.markdown(title)
            text = item[1].decode('utf-16')
            st.text_area('', text, height=444, key=index)
            index += 1

if evaluate:
    st.sidebar.write(":arrow_right: Độ đo MAP của hệ thống đánh giá dựa trên 10 từ khoá trên ~", 123)





