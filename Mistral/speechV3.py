import asyncio
import os
import time


"""# Initialize the text-to-speech engine
import pyttsx3
engine = pyttsx3.init()

# Set properties (optional)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)  # Select a voice
engine.setProperty('rate', 150)            # Speed of speech
engine.setProperty('volume', 1)            # Volume (0.0to 1.0)"""
names = [
    "en-IE-EmilyNeural",#11223
    "en-US-AvaNeural",#123

]
import edge_tts  # Assuming you have imported edge_tts properly
# edge-tts --text "Hello, world!" --write-media hello.mp3 --write-subtitles hello.vtt
def speak(text):
    a = time.time()
    command = f'edge-tts --text  "{text}" --voice en-US-AvaNeural --write-media hello.mp3 '
    os.system(command)
    b = time.time()
    print("latency",b-a)


async def speaknew(text):
    time1 = time.time()
    voice = "en-US-AvaNeural"
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save("hello.mp3")
    time2 = time.time()
    print("text to speech",time2-time1)



speak("Good morning! Hope you’re feeling refreshed and ready to take on the day. Anything exciting on your agenda?")