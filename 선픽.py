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

# 이미지 파일 디렉토리 경로
img_dir = 'path/to/your/image/directory'  # 여기에 실제 이미지 디렉토리 경로를 설정하세요.

# 이미지 파일 리스트
img_files = ['image1.png', 'image2.png', 'image3.png']

# 이미지를 화면에 동그랗게 나열하여 출력합니다.
for img_file in img_files:
    img_path = os.path.join(img_dir, img_file)
    image = Image.open(img_path)

    img_col = f"""
    <div class="circle-img">
        <img src="data:image/png;base64,{st.image(image, use_column_width=True)}" alt="Image">
    </div>
    """
    st.markdown(img_col, unsafe_allow_html=True)
