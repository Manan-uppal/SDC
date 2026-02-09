import whisper

model = whisper.load_model("base")  # or "small", "medium", "large"
result = model.transcribe("recordings/2026-02-09_01-54-29.wav")

print("Transcript:\n")
print(result["text"])
