# Echo

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
> Before starting the program, you must create a Secret.json file and input your OpenAI ChatGPT API Key.
```
{
    "OPENAI_API_KEY" = "YOUR_API_KEY"
}
```
You can run the program by executing main.py.
