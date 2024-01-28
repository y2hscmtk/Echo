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

def tts(input_text):  # 어떤 대답을 할것인지 정의
    answer_text = ''
    if '안녕' in input_text:
        answer_text = "안녕. 반가워"
    elif '뭐 하고 있' in input_text: # '지금 뭐 하고 있어?', '뭐 하고 있니?', 등
        answer_text = "지금 대화 중이잖아, 당신이랑"
    elif '잘 있어' in input_text:
        answer_text = "다음에 보자"
        stop_listening(wait_for_stop=False)  # 더이상 듣지 않음
    elif '에코' in input_text:
        answer_text = "왜 불러"
    else:
        answer_text = "무슨 말 하는건지 모르겠어"
    speak(answer_text)

# 소리내어 읽기 (TTS)
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