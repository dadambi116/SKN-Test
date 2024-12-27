import streamlit as st
# dataframe 표의 형태로 자료 가지고 있음

# streamlit hello 시작
# ctrl +  c : 서버 중단

# cd(change directory) - 경로 옮기기 / 한 번에 연결 안 될 경우 상위 파일 호출 용도!

st.title('오늘은 신나는 금요일!')
st.header("오늘은 streamlit 배우는 날!~")
st.subheader("streamlit으로 만들어 보는 내 사이트!")




my_site = st.text_input("오늘 내가 만들어보고 싶은 사이트는?")
st.write(my_site) # g 화면에 글자 출력

if st.button(f"{my_site} 접속하기"):
    st.success(f"{my_site}로 접속 중🚀🚀🚀",icon= '✅')

# pages 의 이용 
    # 파일명에서 맨앞 언더바 숫자를 반영 안 됨, 이모지 반영 O



st.title('실습 페이지')
print("수정 사항!!")