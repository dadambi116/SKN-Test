import streamlit as st

st.title('Counter')

if 'customer_count' not in st.session_state:   # session_state에 customer_count 값이 없어야만 0으로 초기화 됨 /
    st.session_state.customer_count = 0        # 1번 돌고 나면 1이 추가되기 때문에 0으로 초기화 안 됨됨
      
                                               
 # customer_count = 0           # 버튼 누르면 다시 0으로 세팅
if st.button("손님 한 명 추가요~!"):
    st.session_state.customer_count += 1 # 1에서 더 늘어나지 않음 / streamlit의 특성 때문: 리랜더링 된다는 한계점, interaction에 대한 trigger 없음
                                                    #세션스테이트 통해 해결 가능


if st.button("오늘 장사 끝! 손님 수 초기화!"):
    st.session_state.customer_count = 0

st.write(f"지금까지 온 손님 수: {st.session_state.customer_count}")




