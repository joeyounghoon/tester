import streamlit as st
import streamlit.components.v1 as components

# Custom CSS for styling
st.markdown("""
<style>
body {
    font-family: 'Spoqa Han Sans Neo', sans-serif;
}

.header {
    background-color: #333;
    color: white;
    padding: 20px;
    text-align: center;
    font-size: 25px;
}

.sidebar {
    width: 20%;
    float: left;
    padding: 20px;
}

.sidebar img {
    max-width: 100%;
    height: auto;
}

.main-content {
    width: 78%;
    float: right;
    padding: 20px;
}

.champion-box, .combo-box, .counter-box {
    display: inline-block;
    vertical-align: top;
    margin: 5px;
    padding: 10px;
    border-radius: 5px;
    border: 1px solid #ddd;
    text-align: center;
}

.champion-box {
    background-color: #f4f4f9;
    width: 80px;
    height: 80px;
}

.combo-box {
    background-color: #e3f2fd;
    width: 150px;
    height: 150px;
}

.counter-box {
    background-color: #fce4ec;
    width: 100px;
    height: 100px;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="header">OptimalBotAI</div>', unsafe_allow_html=True)

# Sidebar content
st.markdown('<div class="sidebar">', unsafe_allow_html=True)
st.text_input("Search Champions", "")
st.markdown('<p>챔피언 목록</p>', unsafe_allow_html=True)
champion_names = ["카이사", "진", "에쉬", "블츠", "룰루", "세라핀"]
for name in champion_names:
    st.markdown(f'<div class="champion-box">{name}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Main content
st.markdown('<div class="main-content">', unsafe_allow_html=True)
st.markdown('<p>챔피언을 선택해 주세요!</p>', unsafe_allow_html=True)

selections = {
    "조합": ["룰루", "룰루", "룰루"],
    "카운터": ["세라핀", "진"]
}

# Selections display
st.markdown('<div>', unsafe_allow_html=True)
for key, imgs in selections.items():
    st.markdown(f'<p>{key}</p>', unsafe_allow_html=True)
    for img in imgs:
        st.markdown(f'<div class="combo-box">{img}</div>', unsafe_allow_html=True)
    st.markdown('<div class="combo-box">+</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
