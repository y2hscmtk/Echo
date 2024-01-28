from playsound import playsound
from gtts import gTTS

file_name = 'sample.mp3'  # 저장할 파일 이름

# 한글 문장
text = "안녕하세요. 만나서 반갑습니다."
tts_ko = gTTS(text=text, lang='ko')   # 문자 = 변수, 언어 = 한글 (한글로 저장)
tts_ko.save(file_name)  # file_name을 이름으로 mp3파일 저장
playsound(file_name)  # 저장한 mp3파일을 실행