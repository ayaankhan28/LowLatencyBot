

import soundfile as sf
import sounddevice as sd
def play_here():
    notification_sound_path = "C:\\Mydrive\\python.vs\\Gemini\\Vision\\noti.mp3"
    auddata, samra = sf.read(notification_sound_path)
    sd.play(auddata, samra)
    sd.wait()

play_here()