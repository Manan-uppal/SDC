import assemblyai as aai

# aai.settings.api_key = "bf34c4cf41a64aea8782324a682120d0"
config = aai.TranscriptionConfig(speech_models=["universal-3-pro", "universal-2"], language_detection=True)


def convertor(location):
    
    transcript = aai.Transcriber(config=config).transcribe(location)
    if transcript.status == "error":
        raise RuntimeError(f"Transcription failed: {transcript.error}")
    return(transcript.text)


# print(convertor(r"recording/test.wav"))