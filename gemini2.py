import streamlit as st
import google.generativeai as genai
from PyPDF2 import PdfReader
import os

# PDF 파일 읽기 함수
def get_pdf_path():
    # 현재 스크립트와 같은 디렉토리의 ojt.pdf 파일 경로
    current_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_path = os.path.join(current_dir, 'ojt.pdf')
    return os.path.normpath(pdf_path)

def read_pdf():
    # PDF 파일 경로 가져오기
    pdf_path = get_pdf_path()
    try:
        pdf_reader = PdfReader(pdf_path)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        st.error(f"PDF 파일을 읽는 중 오류가 발생했습니다: {str(e)}")
        return None

# 페이지 기본 설정
st.set_page_config(
    page_title="제이씨현 시스템 신입사원 교육 도우미 🎓",
    page_icon="🏢",
    layout="wide"
)

# CSS 스타일 추가
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fb;
    }
    .stButton>button {
        background-color: #3498db;
        color: white;
        border-radius: 10px;
        padding: 0.5rem 1rem;
        border: none;
    }
    .stTextInput>div>div>input {
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 메인 타이틀
st.title("제이씨현 시스템 신입사원 교육 도우미 🎓")
st.markdown("---")

# 환영 메시지
st.markdown("""
### 안녕하세요! 제이씨현 시스템 신입사원 여러분 환영합니다! 👋

저희 교육 도우미 팀을 소개합니다:

1. **Ted (기술전문가) 🤓**
   - IT 및 기술 관련 전문 지식 제공
   - 업무 관련 기술적 질문 답변
   
2. **Jane (교육전문가) 📚**
   - 복잡한 개념을 쉽게 설명
   - 업무 프로세스 가이드 제공
   
3. **Will (멘토) 🌟**
   - 전반적인 안내 및 조언
   - 회사 생활 적응 도움
""")

# API 키 입력 (숨김 처리)
with st.sidebar:
    st.markdown("### ⚙️ 시스템 설정")
    api_key = st.text_input("Gemini API 키를 입력하세요:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    
    # PDF 내용 읽기
    pdf_content = read_pdf()
    
    if pdf_content:
        # 탭 생성
        tab1, tab2 = st.tabs(["💬 질문하기", "📚 학습자료"])
        
        with tab1:
            st.markdown("### 궁금한 점을 물어보세요! 🤔")
            user_question = st.text_area("질문을 입력해주세요:", 
                                    placeholder="예: 회사의 주요 제품은 무엇인가요?")
            
            if st.button("답변 받기 ✨"):
                try:
                    with st.spinner("답변을 생성중입니다... 🤖"):
                        model = genai.GenerativeModel('gemini-pro')
                        prompt = f"""당신은 제이씨현 시스템의 신입사원 교육 도우미입니다.
                        다음 문서의 내용을 기반으로 질문에 친절하고 명확하게 답변해주세요. 
                        답을 최대한 구체적이고 길게 주세요. 신입사원들이 회사에 대해 잘 알 수 있게 해주세요.
                        이모티콘을 적절히 사용하고, 필요한 경우 예시를 들어 설명해주세요.
                        
                        문서 내용:
                        {pdf_content}
                        
                        질문: {user_question}"""
                        response = model.generate_content(prompt)
                        st.success("답변이 준비되었습니다! 📝")
                        st.write(response.text)
                except Exception as e:
                    st.error(f"죄송합니다. 오류가 발생했습니다 😢: {str(e)}")
        
        with tab2:
            st.markdown("### 회사 소개 자료 📚")
            if st.button("자료 요약 보기 📋"):
                try:
                    model = genai.GenerativeModel('gemini-pro')
                    prompt = f"""다음 회사 소개 자료의 주요 내용을 요약하고, 
                    핵심 포인트를 3-5개로 정리해주세요:\n\n{pdf_content}"""
                    response = model.generate_content(prompt)
                    st.write(response.text)
                except Exception as e:
                    st.error(f"요약 중 오류가 발생했습니다 😢: {str(e)}")

else:
    st.warning("🔑 서비스 이용을 위해 API 키를 입력해주세요!")

# 푸터 추가
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>제이씨현 시스템 신입사원 교육 도우미 v1.0 | 도움이 필요하시면 언제든 물어보세요! 😊</p>
</div>
""", unsafe_allow_html=True)
