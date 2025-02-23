from flask import Flask, render_template, request, jsonify
import os
from transformers import pipeline
import whisper

os.environ["PATH"] += os.pathsep + "C:\\Users\\HP\\scoop\\apps\\ffmpeg\\current\\bin"
app = Flask(__name__, static_folder='static', template_folder='templates')

whisper_model = whisper.load_model("base")
sentiment_pipeline = pipeline("sentiment-analysis")

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/upload', methods=['POST'])
def upload_audio():
    if 'audio' not in request.files:
        return jsonify({"message": "No file uploaded"}), 400

    audio_file = request.files['audio']
    save_path = os.path.join("uploads", "recording.wav")  # Save as fixed filename

    audio_file.save(save_path)
    print(f"File saved at: {save_path}")  # ✅ Debugging

    # Transcribe audio
    transcription = whisper_model.transcribe(save_path)["text"]
    print(f"Transcription: {transcription}")  # ✅ Debugging

    # Sentiment Analysis
    sentiment_result = sentiment_pipeline(transcription)
    sentiment_score = { "positive": 0, "neutral": 0, "negative": 0 }

    if sentiment_result:
        label = sentiment_result[0]["label"].lower()
        score = round(sentiment_result[0]["score"] * 100)
        sentiment_score[label] = score

    return jsonify({
        "transcription": transcription,
        "sentiment": sentiment_score
    })




if __name__ == '__main__':
    app.run(debug=True)
