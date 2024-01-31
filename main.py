from llm import ask
import time
import os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

# STT
def stt(recognizer, audio):
    try:
        # Set the language based on the user's choice
        text = recognizer.recognize_google(audio, language=lang)
        print("[USER] " + text)
        ai_speak(text)
    except sr.UnknownValueError:
        print("Recognition failed")
    except sr.RequestError as e:
        print("Request failed: {0}".format(e))
    pass

def ai_speak(user_input):
    # Get GPT's response in the selected language
    answer_text = ask(user_input, lang)
    speak(answer_text)

# TTS
def speak(text):
    print('[Echo] ' + text)
    file_name = 'voice.mp3'
    tts = gTTS(text=text, lang=lang)
    tts.save(file_name)
    playsound(file_name)
    # Remove 'voice.mp3' file after execution
    if os.path.exists(file_name):
        os.remove(file_name)

r = sr.Recognizer()
m = sr.Microphone()

# Ask the user to choose a language
while True:
    lang = input("Choose your language (kr/eng): ")
    if lang.lower() in ['kr', 'eng']:
        break
    else:
        print("Invalid input. Please enter 'kr' or 'eng'.")

# Background operation, call stt function when hearing through microphone
stop_listening = r.listen_in_background(m, stt)

# Prevent program from exiting
while True:
    time.sleep(0.1)
