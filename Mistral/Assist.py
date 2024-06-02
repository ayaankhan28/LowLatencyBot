import re
import time
import speechV3
import soundfile as sf
import sounddevice as sd
import pyttsx3
from groq import Groq
from faster_whisper import WhisperModel
import pyaudio
import wave
import audioop
import os
import asyncio
def play_here():
    notification_sound_path = "C:\\Mydrive\\python.vs\\Gemini\\Vision\\noti.mp3"
    auddata, samra = sf.read(notification_sound_path)
    sd.play(auddata, samra)
    sd.wait()
play_here()


apiKey = "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"
client = Groq(api_key=apiKey)
import keyboard
model = WhisperModel('tiny', device="cuda", compute_type="float16")
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
THRESHOLD_ENERGY = 2000
THRESHOLD_TIME = 2
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"
audio = pyaudio.PyAudio()

#build a project where I can control car racing games using the hand gestures,
#but there was a lot of latency. Can you can you tell me what could have gone wrong?
messages = [
            {
                "role": "system",
                "content": "you are my personal assisstant,give me response under 30 words."
            },

        ]

def remove_emojis(text):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               "]+", flags=re.UNICODE)
    # Replace emojis with an empty string
    return emoji_pattern.sub(r'', text)
def speak_async():
    auddata, samra = sf.read("hello.mp3")
    sd.play(auddata, samra)
    sd.wait()
    sd.stop()
    os.remove("hello.mp3")

def listen():

    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    frames = []
    start_time = time.time()
    silence_detected = False

    while True:
        data = stream.read(CHUNK)
        frames.append(data)
        energy = audioop.rms(data, 2)

        if energy < THRESHOLD_ENERGY:
            if silence_detected and time.time() - start_time > THRESHOLD_TIME:
                break
            silence_detected = True
        else:
            silence_detected = False
            start_time = time.time()


    time1 = time.time()
    stream.stop_stream()
    stream.close()

    # Save the recorded audio to a file
    with wave.open(WAVE_OUTPUT_FILENAME, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

    # Transcribe the audio
    segments, jvjv = model.transcribe(WAVE_OUTPUT_FILENAME)
    transcription = ""

    for segment in segments:
        transcription += segment.text
    time2 = time.time()
    print("transcribing time: " , (time2-time1))

    return transcription

def process_audio(transcription):
    time1 = time.time()
    if transcription == "exit":
        sd.stop()
    mes = {
                "role": "user",
                "content": f"{transcription}",
            }
    messages.append(mes)

    resource = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=messages,
        temperature=0.5,

    )
    text = resource.choices[0].message.content
    mes = {
        "role": "assistant",
        "content": f"{text}",
    }
    messages.append(mes)

    print(text)
    time2 = time.time()
    print("Groq Response " , (time2-time1))





    print(len(text))

    #print("GPT time time: " , (time2-time1))
    #LowLatencyTTS
    #speechV3.speakFast(text)
    #NaturalSoundingTTS
    asyncio.run(speechV3.speaknew(text))
    speak_async()

if __name__ == "__main__":
    #recorder = AudioToTextRecorder(spinner=False, model="tiny.en", language="en")
    while True:
        #print("Listening...")
        if keyboard.is_pressed('shift+x'):
            play_here()

            transcription = listen()
            transcription = remove_emojis(transcription)
            print(transcription)



            #print("transcription:", transcription,":")
            #print(len(transcription))
            if "exit" in transcription.lower():
                #print("pass1")
                break
            if len(transcription) ==4:
                #print("pass2")
                pass
            else:


                process_audio(transcription)
