import streamlit as st
import random 
#게임 결과 내는 함수. guessNum는 사람 추측값 0(앞면) 뒷면 (1)
def playGame (guessNum):
  comNum = random.randint(0,1)
  if comNum ==guessNum:
    st.write('적중!!')
else:
  st.write('아쉽네요.틀렸습니다.')
st.title("동전던지기 게임")
st.divider()

st.image('')


st.header('동전 던지기 게임에 오신 것을 환영합니다.')
st.subheader('앞면일까요? 뒷면일까요?')

if st.button('앞면'):
  st.text('앞면일것 같음')
 
if st.button('뒷면'):
  st.text('뒷면일것 같음')

if st.button('앞면'):
  playGame (0)


if st.button('뒷면'):
  playGame (1)
