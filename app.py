from flask import Flask, render_template, request, jsonify
import os
import whisper
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__, static_folder='static', template_folder='templates')
# UPLOAD_FOLDER = 'uploads'
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load Whisper model
# model = whisper.load_model("base")
# # Load Sentiment Analyzer
# analyzer = SentimentIntensityAnalyzer()

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/upload', methods=['POST'])
# def upload_audio():
#     if 'audio' not in request.files:
#         return jsonify({'error': 'No file uploaded'}), 400
    
#     file = request.files['audio']
#     filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#     file.save(filepath)
    
#     # Transcribe audio
#     result = model.transcribe(filepath)
#     text = result['text']
    
#     # Sentiment Analysis
#     sentiment = analyzer.polarity_scores(text)
#     sentiment_label = "Positive" if sentiment['compound'] > 0.05 else "Negative" if sentiment['compound'] < -0.05 else "Neutral"
    
#     return jsonify({'text': text, 'sentiment': sentiment_label})

if __name__ == '__main__':
    app.run(debug=True)
