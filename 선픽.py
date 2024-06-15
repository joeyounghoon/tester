import streamlit as st
import openai
import streamlit.components.v1 as components

# OpenAI API 키 설정 (API 키를 환경변수 또는 직접 입력)
openai.api_key = 'sk-proj-mayBgL7AxeyXQnxLlJL5T3BlbkFJPmO5bCmENRMUbggB2dNA'

# OpenAI 챔피언 클래스 정의
class Champion:
    def __init__(self, model='gpt-4'):
        self.model = model

    def get_response(self, prompt):
        try:
            response = openai.Completion.create(
                model=self.model,
                prompt=prompt,
                max_tokens=150
            )
            return response.choices[0].text.strip()
        except Exception as e:
            return f"Error: {e}"

# 챔피언 객체 생성
champion = Champion()

# 사용자 입력 받기
user_input = st.text_area("질문을 입력하세요:")

if st.button("응답 받기"):
    if user_input:
        response = champion.get_response(user_input)
        st.write("챔피언의 응답:")
        st.write(response)
    else:
        st.write("질문을 입력하세요.")

# 이미지 업로드 및 표시
uploaded_file = st.file_uploader("이미지를 업로드하세요", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # 이미지 표시
    st.image(uploaded_file, caption='업로드된 이미지', use_column_width=True)
    
    # 커스텀 HTML/CSS 및 JavaScript 코드 삽입
    components.html(f"""
        <style>
            img {{
                border: 5px solid #555;
                border-radius: 15px;
                cursor: pointer;
            }}
        </style>
        <img src="data:image/jpeg;base64,{uploaded_file.getvalue().decode('utf-8')}" id="clickable-image" width="100%" />
        <div id="response-box" style="margin-top: 20px; display: none;">
            <textarea id="response-text" rows="4" style="width: 100%;"></textarea>
        </div>
        <script>
            document.getElementById('clickable-image').onclick = function() {{
                document.getElementById('response-box').style.display = 'block';
                const textArea = document.getElementById('response-text');
                textArea.value = `{champion.get_response(user_input)}`;
            }};
        </script>
    """, height=600)



# Streamlit 페이지 구성
st.set_page_config(layout="wide")

# 사이드바에 들어가는 타이틀
st.sidebar.title('OptimalBotAI')

# Streamlit 페이지에 CSS 적용하기!
st.markdown(
    """
    <style>
    body {
        overflow: hidden;
    }
    .main {
        background-color: #f0f2f6;
        display: flex;
        flex-direction: row;
        height: 100vh;
    }
    .sidebar {
        padding: 10px;
        background-color: #d3d3d3;
        position: relative;
        user-select: auto;
        width: 336px;
        height: 842px;
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
    .divider {
        width: 100%;
        height: 2px;
        position: absolute;
        top: 50%;
        z-index: 99999;
        background-color: black;
    }

    /*미디어 쿼리 패딩 제거 */
    @media (min-width: 576px) {
        .st-emotion-cache-1jicfl2 {
            padding-left: 0 !important;
            padding-right: 0 !important;
        }
    }

    /* 스크롤바 제거 */
    .st-emotion-cache-1jicfl2 {
        width: 100%;
        padding: 0;
        min-width: auto;
        max-width: initial;
    }

    /*streamlit 기본 상단 바 제거*/
    .st-emotion-cache-h4xjwg {
        height: 0;
    }

    /*여백 안남게 scoll-margin 제거*/
    .st-emotion-cache-1jzia57 h1, 
    .st-emotion-cache-1jzia57 h2, 
    .st-emotion-cache-1jzia57 h3, 
    .st-emotion-cache-1jzia57 h4, 
    .st-emotion-cache-1jzia57 h5, 
    .st-emotion-cache-1jzia57 h6, 
    .st-emotion-cache-1jzia57 span {
        scroll-margin-top: 0;
    }

    /*streamlit에서 기본으로 제공하는 공유, 깃허브 링크 등등 바 설정*/
    .st-emotion-cache-15ecox0.ezrtsby0 {
        background-color: black;
        border-radius: 10px;
    }

    /*화면 상단 gap 제거*/
    .st-emotion-cache-1wmy9hl div {
        gap: 0;
    }
    

    /*여백 제거*/
    .st-emotion-cache-ul70r3 {
        margin-bottom: 0;
    }
    </style>
    """, unsafe_allow_html=True
)

# Streamlit markdown으로 구성!
st.markdown(
    """
    <div class='divider'></div>
    <div class='sidebar'>
        <div class='champion-section'>
            <h5 class='recommend-champ-title'>원딜 추천 챔피언</h5>
            <div class="champion-list-content">
            </div>
        </div>
        <div class='champion-section'>
            <h5 class='recommend-champ-title'>서폿 추천 챔피언</h5>
            <div class="champion-list-content">
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True
)

