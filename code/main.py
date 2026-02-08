import sounddevice as sd
import numpy as np 
import  soundfile as sf
import datetime as dt   


sd.default.samplerate = 48000
sd.default.blocksize = 1024
sd.default.channels=1

rec_list = []
def audio_callback(indata, frames, time, status):
    if status :
        print(status)
    rec_list.append(indata.copy())

def playingsound(arr, sampling_rate = sd.default.samplerate):
     sd.play(arr, sampling_rate)
     sd.wait()

with sd.InputStream(
    callback=audio_callback
):
    input("press enter to stop\n")


full_audio = np.concatenate(rec_list, axis=0)
playingsound(full_audio)
time = dt.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
sf.write(f"recording/{time}.wav", full_audio, sd.default.samplerate)