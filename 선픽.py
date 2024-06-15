import streamlit as st
from openai import OpenAI
import streamlit.components.v1 as components
import time

# 응답함수
def run_and_wait(client, assistant, thread):
  run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id
  )
  while True:
    run_check = client.beta.threads.runs.retrieve(
      thread_id=thread.id,
      run_id=run.id
    )
    print(run_check.status)
    if run_check.status in ['queued','in_progress']:
      time.sleep(2)
    else:
      break
  return run

import openai

openai.api_key = 'YOUR_OPENAI_API_KEY'


def translate_image_to_korean(file_id, user_message):
  
    my_file = client.files.create(
      file = open("ashe.docx",'rb'),
      purpose='assistants'
    )
    my_file  
  
    # 어시스턴트 생성
    assistant = openai.Assistant.create(
        name="번역 전문가",
        description="당신은 번역 전문가입니다.",
        model="gpt-4-turbo-preview",
        tools=[{"type": "code_interpreter"}],
        file_ids=[file_id]
    )

    # 스레드 생성
    thread = openai.Thread.create(
        messages=[
            {
                "role": "user",
                "content": user_message,
                "file_ids": [file_id]
            }
        ]
    )

    # 작업 실행 및 대기
    run = openai.run_and_wait(client, assistant, thread)

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
    response_file_delete = openai.File.delete(file_id)

    return {
        "translated_text": translated_text,
        "response_thread_delete": response_thread_delete,
        "response_assistant_delete": response_assistant_delete,
        "response_file_delete": response_file_delete
    }


if st.button("상성 보기"):  
  file_id = 'YOUR_FILE_ID'
  user_message = '첨부한 pdf 파일의 글을 읽은 다음, 챔피언의 상성을 알려줘.'
  response = translate_image_to_korean(file_id, user_message)

  # 결과 출력 (선택 사항)
  for key, value in response.items():
    print(f"{key}: {value}")
  if st.button("닫기"):
    
  


# OpenAI API 키 설정
openai.api_key = 'sk-proj-mayBgL7AxeyXQnxLlJL5T3BlbkFJPmO5bCmENRMUbggB2dNA'

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

