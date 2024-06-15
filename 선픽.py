import streamlit as st
import streamlit.components.v1 as components
import time
import openai
from PIL import Image
import os
import base64
import pandas as pd



# Streamlit 애플리케이션 시작
st.set_page_config(layout="wide")

# 상성 보기 버튼 처리
if st.button("상성 보기"):
    st.subheader('This is a subheader with a divider', divider='rainbow')
    st.subheader('_Streamlit_ is :blue[cool] :sunglasses:')

# 사이드바 설정
st.sidebar.title('OptimalBotAI')

# CSS 적용
st.markdown(
    """
    <style>
    .divider {
        width: 100%;
        height: 2px;
        position: absolute;
        top: 50%;
        z-index: 99999;
        background-color: black;
    }
    .sidebar {
        padding: 10px;
        background-color: #d3d3d3;
        position: relative;
        user-select: auto;
        width: 336px;
        height: 100vh;
        box-sizing: border-box;
        flex-shrink: 0;
    }
    .champion-section {
        width: 100%;
        display: flex;
        flex-direction: column;
        margin-bottom: 20px;
    }
    .champion-list-content {
        width: 300px;
        height: 350px;
        display: flex;
        flex-direction: column;
        item-align: center;
        gap: 10px;
    }
    .recommend-champ-title {
        margin-top: 10px;
        font-size: 15px;
        font-weight: bold;
        text-align: left;
        color: black;
    }
    </style>
    """, unsafe_allow_html=True
)

# 사이드바 내용 추가
st.sidebar.markdown(
    """
    <div class='divider'></div>
    <div class='champion-section'>
        <h5 class='recommend-champ-title'>원딜 추천 챔피언</h5>
        <div class="champion-list-content">
            <!-- 챔피언 리스트 내용 추가 -->
        </div>
    </div>
    <div class='champion-section'>
        <h5 class='recommend-champ-title'>서폿 추천 챔피언</h5>
        <div class="champion-list-content">
            <!-- 챔피언 리스트 내용 추가 -->
        </div>
    </div>
    """, unsafe_allow_html=True
)

# CSS 스타일을 정의하여 이미지를 동그랗게 만듭니다.
st.markdown("""
    <style>
    .circle-img {
        display: inline-block;
        border-radius: 50%;
        overflow: hidden;
        width: 80px;
        height: 80px;
        margin: 10px;
    }
    .circle-img img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
    </style>
    """, unsafe_allow_html=True)


# Streamlit 페이지에 CSS 적용하기
st.markdown(
    """
    <style>
    .image-container {
        display: flex;
        flex-direction: row;
    }
    .thumbnail {
        width: 100px;
        height: 100px;
        object-fit: cover;
        margin: 5px;
        cursor: pointer;
        transition: transform 0.2s;
    }
    .thumbnail:hover {
        transform: scale(1.1);
    }
    .selected-image {
        width: 300px;
        height: 300px;
        object-fit: contain;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load images as base64 encoded strings
image1_data = open('image1.png', 'rb').read()
image1_b64 = base64.b64encode(image1_data).decode()

image2_data = open('images.png', 'rb').read()
image2_b64 = base64.b64encode(image2_data).decode()

# Create HTML and JavaScript code for image display and click event
html_code = f"""
<!DOCTYPE html>
<html>
<head>
<style>
#image1 {
  display: block;
  cursor: pointer;
  max-width: 500px;
  height: auto;
}

#images {
  display: none;
  max-width: 500px;
  height: auto;
}
</style>
</head>
<body>
<img id="image1" src="data:image/png;base64,{image1_b64}" alt="Image 1">
<img id="images" src="data:image/png;base64,{image2_b64}" alt="Image 2">

<script>
document.getElementById('image1').addEventListener('click', function() {{
  document.getElementById('image1').style.display = 'none';
  document.getElementById('images').style.display = 'block';
}});
</script>
</body>
</html>
"""

# Display the HTML content in Streamlit
st.write(html_code, unsafe_allow_html=True)
