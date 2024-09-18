import streamlit as st
import google.generativeai as genai
from PyPDF2 import PdfReader
import io

# PDF 파일 읽기 함수
def read_pdf(uploaded_file):
    pdf_reader = PdfReader(io.BytesIO(uploaded_file.getvalue()))
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Streamlit 앱 설정
st.title("Gemini PDF 질문 답변기")

# API 키 입력 받기
api_key = st.text_input("Gemini API 키를 입력하세요:", type="password")

if api_key:
    # Gemini API 키 설정
    genai.configure(api_key=api_key)

    # PDF 파일 업로드 기능 추가
    uploaded_file = st.file_uploader("PDF 파일을 업로드하세요", type="pdf")

    if uploaded_file is not None:
        pdf_content = read_pdf(uploaded_file)
        # 사용자 입력 받기
        user_question = st.text_input("PDF에 대해 질문하세요:")

        if user_question:
            try:
                # Gemini 모델 생성
                model = genai.GenerativeModel('gemini-pro')
                
                # 프롬프트 생성
                prompt = f"다음 PDF 내용을 바탕으로 질문에 답해주세요:\n\nPDF 내용: {pdf_content}\n\n질문: {user_question}"
                
                # Gemini로 응답 생성
                response = model.generate_content(prompt)
                
                # 응답 출력
                st.write("Gemini의 답변:")
                st.write(response.text)
            except Exception as e:
                st.error(f"오류가 발생했습니다: {str(e)}")
        else:
            st.warning("질문을 입력해주세요.")
    else:
        st.warning("PDF 파일을 업로드해주세요.")
else:
    st.warning("API 키를 입력해주세요.")
