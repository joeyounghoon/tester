import streamlit as st
import streamlit.components.v1 as components
import time
import openai



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

# OpenAI API 키 설정
openai.api_key = "sk-proj-ymDJhgmlypm59yovogzYT3BlbkFJa2IOtnB2mEXqIchhX4dO"
client = openai.OpenAI()
# 페이지 제목 설정
st.title("OpenAI Assistant 웹페이지")

# 상성보기 버튼 생성
show_button = st.button("상성보기")

# 상성보기 버튼 클릭 시 텍스트 입력 상자 및 응답 출력
if show_button:

    # OpenAI Assistant API call
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "LangChain은 무엇을 하는 라이브러리지?"}
        ]
    )
    
    # Process and display response
    if response["choices"]:
        response_text = response["choices"][0]["text"]
        st.write("**어시스트봇:**", response_text)
