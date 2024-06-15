import streamlit as st
import streamlit.components.v1 as components
import time
import openai

# OpenAI API 키 설정
openai.api_key = "sk-proj-ymDJhgmlypm59yovogzYT3BlbkFJa2IOtnB2mEXqIchhX4dO"

def translate_to_korean(file_path, user_message):
    # 파일 업로드
    with open(file_path, 'rb') as file:
        my_file = openai.File.create(file=file, purpose='assistants')

    # 어시스턴트 생성
    assistant = openai.Assistant.create(
        name="롤 코치",
        description="리그오브레전드 게임의 코치입니다.",
        model="gpt-4-turbo-preview",
        tools=[{"type": "code_interpreter"}],
        file_ids=[my_file.id]
    )

    # 스레드 생성
    thread = openai.Thread.create(
        messages=[
            {
                "role": "user",
                "content": user_message,
                "file_ids": [my_file.id]
            }
        ]
    )

    # 작업 실행 및 대기
    run = openai.run_and_wait(assistant, thread)

    # 스레드 메시지 리스트
    thread_messages = openai.Thread.messages.list(thread.id)

    # 메시지 내용 수집
    translated_text = []
    for msg in thread_messages.data:
        translated_text.append(f"{msg.role}: {msg.content}")

    # 스레드 삭제
    response_thread_delete = openai.Thread.delete(thread.id)

    # 어시스턴트 삭제
    response_assistant_delete = openai.Assistant.delete(assistant.id)

    # 파일 삭제
    response_file_delete = openai.File.delete(my_file.id)

    return {
        "translated_text": translated_text,
        "response_thread_delete": response_thread_delete,
        "response_assistant_delete": response_assistant_delete,
        "response_file_delete": response_file_delete
    }


# Streamlit 애플리케이션 시작
st.set_page_config(layout="wide")

# 상성 보기 버튼 처리
if st.button("상성 보기"):
    file_path = "ashe.docx"  # 파일 경로 설정
    user_message = '첨부한 docx 파일의 글을 읽은 다음, 챔피언의 상성을 알려줘.'
    response = translate_to_korean(file_path, user_message)

    # 결과 출력
    st.write("번역 결과:")
    for key, value in response.items():
        st.write(f"{key}: {value}")

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
