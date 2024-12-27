import streamlit as st

st.title("강아지 육아 일기")

with st.form("나의 애완견"):
    name = st.text_input("이름: (필수)")
    species = st.text_input("견종: (필수)")
    share = st.text_input("같이 공유해줄 일지 링크: (선택)")
    checked = st.checkbox("개인정보 제공 동의")
    submit = st.form_submit_button("제출")
if submit:
    st.write(f"이름: {name}, 견종: {species}")


# age = st.number_input("나이" "(1년 미만은 0년)", min_value=0,max_value= 20)
st.divider()

col1, col2,col3 = st.columns(3) 

with col1:
    st.header("훈련 일지")

    st.expander("훈련 종류")
    options = ['앉아','엎드려','굴러','손','충성']
    selected = st.selectbox("어떤 훈련을 원하니?", options)
    with st.expander("이미지는?"):
        img = st.image("강쥐.jpg")

    st.link_button("망나니 강쥐의 훈련 과정!",url="https://blog.naver.com/PostList.naver?blogId=uryzipi&from=postList&categoryNo=16")


with col2:
    st.header("일상 일지")
    st.link_button("주인장의 일상 일지로 이동",url="https://blog.naver.com/PostList.naver?blogId=uryzipi&from=postList&categoryNo=6&parentCategoryNo=6")

with col3:
    st.header("여행 일지")
    st.link_button("여행가기 좋은 장소,카페,음식점 공유!", url="https://blog.naver.com/PostList.naver?blogId=uryzipi&from=postList&categoryNo=17")

