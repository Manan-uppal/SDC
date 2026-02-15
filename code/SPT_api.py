import assemblyai as aai


config = aai.TranscriptionConfig(speech_models=["universal-3-pro", "universal-2"], language_detection=True)


def convertor(location):
    
    transcript = aai.Transcriber(config=config).transcribe(location)
    if transcript.status == "error":
        raise RuntimeError(f"Transcription failed: {transcript.error}")
    return(transcript.text)


# print(convertor(r"recording/test.wav"))git 