from llm import ask # gpt.py에서 ask 함수 import
import time
import os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

# 음성 인식(STT)
def stt(recognizer, audio):  
    try:
        text = recognizer.recognize_google(audio, language='ko')
        print("[사용자] " + text)
        tts(text)
    except sr.UnknownValueError:
        print("인식 실패")
    except sr.RequestError as e: 
        print("요청 실패 : {0}".format(e))
    pass

def tts(user_input):
    # gpt 응답을 답변으로 받아오기
    answer_text = ask(user_input)
    speak(answer_text) # 말하기

# 말하기 (TTS)
def speak(text):  
    print('[에코] ' + text)
    file_name = 'voice.mp3'
    tts = gTTS(text=text, lang='ko') # 사용언어는 한글로
    tts.save(file_name)  # file_name으로 해당 mp3파일 저장
    playsound(file_name)  # 저장한 mp3파일을 읽어줌
    if os.path.exists(file_name):  # file_name 파일이 존재한다면
        os.remove(file_name)  # 실행 이후 mp3 파일 제거

r = sr.Recognizer()
m = sr.Microphone()

# background로 동작, m(마이크)를 통해 듣다가 stt함수 호출
stop_listening = r.listen_in_background(m, stt) 

# 프로그램 종료 방지
while True:
    time.sleep(0.1)
