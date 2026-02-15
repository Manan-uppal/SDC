import sounddevice as sd
import numpy as np 
import soundfile as sf
import datetime as dt   
import SPT_api as spai
import lmstudio as lms

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

def record():
    with sd.InputStream(
        callback=audio_callback
    ):
        input("press enter to stop\n")


def corrector(text):
    model = lms.llm("gemma-3-4b-it")
    response = model.respond(text)
    return response
    

while True:
    try :
        rec_list.clear()
        record()
        full_audio = np.concatenate(rec_list, axis=0)
        playingsound(full_audio) 
        ask = str(input("Enter y/n :: "))
        if ask.lower() == "y":
            sf.write(f"recording/test.wav", full_audio, sd.default.samplerate)
            break  
        else :
            continue
    except:
        continue




# time = dt.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")y'
# sf.write(f"recording/{time}.wav", full_audio, sd.default.samplerate) 



text = (spai.convertor(r"recording/test.wav"))
print(corrector(f'give me grammatically correct version of this "{text}" sentence , just give me correct version'))