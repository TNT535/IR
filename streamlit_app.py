import streamlit as st
from helper import *
import time


def token_corpus(text_input):
    tokens = word_tokenize(text_input)
    return tokens


flag = False
expand_query = False

st.set_page_config(page_title='IR System', page_icon=':mag')
st.title("Hệ thống tìm kiếm tin tức bằng tiếng Việt :newspaper:")

st.sidebar.header(":desktop_computer: Tìm kiếm")
user_input = st.sidebar.text_input('Nhập từ khoá muốn tìm kiếm', "Từ khoá", key=1)
clicked = st.sidebar.button('Search')

keyword_searched = {}

if user_input == 'Từ khoá' or user_input == '':
    st.sidebar.error(":x: Hãy nhập từ khoá cần tìm kiếm")
else:
    flag = True

if clicked:
    flag = True

if user_input in st.session_state:  # expand here
    expand_query = True

if expand_query:
    pass
    # user_input = Query_Expansion(user_input)   # And a list of result from before

start_time = time.time()
content_to_expand = []
if flag:
    with st.spinner("Xin vui lòng chờ một chút..."):
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
            content_to_expand.append(Clean_Data(text))
            st.text_area('', text, height=444, key=index)
            index += 1
with st.sidebar.expander("Kết quả đánh giá mô hình"):
    st.write(":pushpin: Mô hình được đánh giá dựa trên độ đo Precision")
    st.write(":pushpin: Với 10 câu query nhóm tự gán nhãn")
    st.table(table)
if user_input not in st.session_state:
    st.session_state[user_input] = content_to_expand
else:
    a = Update_Query(user_input, st.session_state['bắt tạm giam'])
    print(a)









