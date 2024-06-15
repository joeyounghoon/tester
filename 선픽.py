import streamlit as st
import streamlit.components.v1 as components
import time
import openai
from PIL import Image
import os



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

# 이미지 파일 경로 설정
image_paths = images.png

# 초기 이미지 선택
selected_image_path = image_paths[0]

# Streamlit 애플리케이션 구성
st.title('이미지 클릭 예시')

# 이미지 컨테이너 생성
image_container = st.empty()

# 이미지 클릭 시 실행할 JavaScript 코드
javascript = """
<script>
function showImage(imagePath) {
    var img = document.getElementById('selected-image');
    img.src = imagePath;
}
</script>
"""

# JavaScript 코드 삽입
components.html(javascript)

# 이미지를 클릭하면 JavaScript 함수를 호출하여 선택된 이미지 변경
for image_path in image_paths:
    image_html = f'<img class="thumbnail" src="{image_path}" onclick="showImage(\'{image_path}\')" />'
    image_container.markdown(image_html, unsafe_allow_html=True)

# 선택된 이미지 표시
selected_image_html = f'<img id="selected-image" class="selected-image" src="{selected_image_path}" />'
st.markdown(selected_image_html, unsafe_allow_html=True)
