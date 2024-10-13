# Gemini PDF 분석기

이 프로젝트는 Streamlit과 Google의 Gemini AI를 사용하여 PDF 파일을 분석하고 질문에 답변하는 웹 애플리케이션입니다.

## 기능

- PDF 파일 내용 읽기
- 사용자의 질문에 대해 Gemini AI를 사용하여 답변 생성
- 간단한 웹 인터페이스 제공

## 설치 방법

1. 이 저장소를 클론합니다:
   ```
   git clone https://github.com/yourusername/gemini-pdf-analyzer.git
   cd gemini-pdf-analyzer
   ```

2. 필요한 라이브러리를 설치합니다:
   ```
   pip install streamlit google-generativeai PyPDF2
   ```

## 사용 방법

1. `gemini2.py` 파일에서 PDF 파일 경로를 설정합니다:
   ```python
   pdf_path = "여러분의_PDF_파일_경로.pdf"
   ```

2. 애플리케이션을 실행합니다:
   ```
   streamlit run gemini2.py
   ```

3. 웹 브라우저에서 애플리케이션에 접속합니다.

4. Gemini API 키를 입력합니다.

5. PDF 내용에 대해 질문을 입력하고 답변을 받습니다.

## 주의사항

- Gemini API 키가 필요합니다. [Google AI Studio](https://makersuite.google.com/app/apikey)에서 키를 발급받을 수 있습니다.
- PDF 파일 경로는 절대 경로로 지정해야 합니다.

## 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다.

## 기여

버그 리포트, 기능 제안, 풀 리퀘스트 등 모든 기여를 환영합니다.
