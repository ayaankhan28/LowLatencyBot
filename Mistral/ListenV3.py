
from faster_whisper import WhisperModel
import pyaudio
import wave
import audioop
import time
model = WhisperModel('tiny', device="cuda", compute_type="float16")
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5  # Adjust as needed
WAVE_OUTPUT_FILENAME = "output.wav"
THRESHOLD_ENERGY = 2000  # Adjust as needed
THRESHOLD_TIME = 2  # Adjust as needed
audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
frames = []
start_time = time.time()

silence_detected= False
def listn():
    print("Listening...")
    global silence_detected, start_time
    while True:

        data = stream.read(CHUNK)
        frames.append(data)
        # Calculate energy of the current chunk
        energy = audioop.rms(data, 2)
        # Check if energy is below the threshold
        if energy < THRESHOLD_ENERGY:
            # If silence is detected and silence duration exceeds the threshold, stop recording
            if silence_detected and time.time() - start_time > THRESHOLD_TIME:
                break
            silence_detected = True
        else:
            silence_detected = False
            start_time = time.time()



    # Stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded audio to a file
    with wave.open(WAVE_OUTPUT_FILENAME, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))





    segments,jvjv= model.transcribe(WAVE_OUTPUT_FILENAME)
    text = ""

    for segment in segments:
        print("...")
        text = text + segment.text




    return text


print(listn())

