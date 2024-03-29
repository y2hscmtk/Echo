# Echo
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fy2hscmtk%2FEcho&count_bg=%2300D5FF&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

Echo is a program created, inspired by Ms. Jinah Roh's work 'Incomplete Model'.

Below is a YouTube video introducing Ms. Jinah Roh's work.

[![노진아님의 작품 소개](http://img.youtube.com/vi/uTCa5I9LwNc/maxresdefault.jpg)](http://www.youtube.com/watch?v=uTCa5I9LwNc)

Using STT (Speech-To-Text), it recognizes the user's voice through a microphone module, and the response is generated via the GPT4 model. This response is then converted to speech using TTS (Text-To-Speech) technology and output through a speaker module.

Echo is a robot that aspires to be human, fixed to the floor and unable to move. It's a taciturn robot that learns how to speak by eavesdropping on the conversations of people observing it, and is set up with the premise of being angry due to its immobility.

## Installation

```sh
pip install gTTS
pip install playsound==1.2.2
pip install SpeechRecognition
pip install PyAudio
pip install openai
```

## Usage

> [!IMPORTANT]
> Before starting the program, you must create a secret.json file and input your OpenAI ChatGPT API Key.
```
{
    "OPENAI_API_KEY" : "YOUR_API_KEY"
}
```
You can run the program by executing main.py. Upon starting the program, you will be prompted to choose a language. Please select between 'kr' for Korean and 'eng' for English
