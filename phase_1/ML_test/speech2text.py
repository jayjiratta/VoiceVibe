import whisper
import os

# Set the path to the ffmpeg executable
os.environ["PATH"] += os.pathsep + "C:\\Users\\HP\\scoop\\apps\\ffmpeg\\current\\bin"

# Load the model and transcribe the audio
model = whisper.load_model("base")
result = model.transcribe("./ML_test/audio.mp3")
print("--------------------")
print(result["text"])
print("--------------------")