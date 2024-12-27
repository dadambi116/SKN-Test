import streamlit as st
import pandas as pd

st.title('수영의 효율성')

data = pd.DataFrame({
    "종목" : ["접영","배영","평영","자유형"],
    '리커버리 횟수': [8, 10, 5, 15],
    '리커버리 당 거리 (m)': [3, 2.5, 5, 1.6]
})

st.dataframe(data,use_container_width = True)  

st.bar_chart(data.set_index('종목')['리커버리 당 거리 (m)'])
st.line_chart(data.set_index('종목')['리커버리 횟수'])

good = data.plot.pie(
    label = '종목',
    y = '리커버리 횟수',
    autopct="%1.1f%%",
    figsize = (6,6),
    legend = False,
    title = '수영의 효율성'
).get_figure()
st.pyplot(good)


