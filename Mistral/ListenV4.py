from RealtimeSTT import AudioToTextRecorder
recorder = AudioToTextRecorder(spinner=False, model="tiny.en", language="en")
if __name__ == '__main__':

    print("Recording...")

    a=recorder.text()
    print(a)

    print("done")
    """recorder.stop()"""
    recorder.shutdown()

