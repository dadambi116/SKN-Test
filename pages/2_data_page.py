import streamlit as st
   # pandas 데이터프레임 활용
import pandas as pd
# import matplotlib.pyplot

st.title("게임 캐릭터의 인지도")

data = pd.DataFrame({
    "캐릭터": ["전사",'법사','힐러','탱커','랜덤'],
    '선택 횟수': [120, 95, 150, 80, 111],
    '승률 (%)': [52, 48, 56, 60, 49],
    '인지도 (%)': [25, 20, 30, 15, 22]
})

st.dataframe(data,use_container_width = True)  # 화면 너비에 맞게 맞춰줌


# edited_data = st.data_editor(data)  # 데이터 수정이 가능
# st.write(edited_data)

st.bar_chart(data.set_index('캐릭터')['선택 횟수'])   # 캐릭터 인덱스, 값이 선택횟수 됨
st.line_chart(data.set_index('캐릭터')['승률 (%)'])

fig = data.plot.pie(
    y = '인지도 (%)',
    labels = data['캐릭터'],
    autopct="%1.1f%%",   # 비율을 보여주는 형식 결정 (소수점 첫째자리 까지 표시)
    figsize = (6,6),   
    legend = False,  # 범례
    title = '캐릭터 별 인지도'
).get_figure()
st.pyplot(fig)
