# VoiceVibe
**VoiceVibe**: A web app that converts speech to text and analyzes emotions using AI. Upload audio or speak via mic to get text and sentiment results (positive, negative, neutral). Built with Flask, showcasing speech processing and emotion detection.

## Usage

To run this web application locally, follow these steps:

1. Clone this repository to your local machine.
2. Set up a virtual environment:
    ```
    python -m venv venv
    ```
3. Activate the virtual environment:
    - On Windows:
        ```
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```
        source venv/bin/activate
        ```
4. Install the required dependencies using pip:

    ```
    pip install -r requirements.txt
    ```

6. Run the Flask application:

    ```
    flask --app app  run --debug
    ```

7. Open your web browser and navigate to `http://localhost:5000` to access the application.

## Project Versions

**Version 1: Pre-trained Models**

In the initial version of the project, I will utilize pre-trained models for speech-to-text conversion and sentiment analysis:

- **Speech-to-Text**: Using [OpenAI's Whisper model](https://github.com/openai/whisper) for accurate and efficient transcription of audio files. 
- **Sentiment Analysis**: Leveraging [transformers](https://github.com/huggingface/transformers) for sentiment analysis, which is well-suited for detecting emotions in text.
- **Deployment**: The results will be displayed using Flask for a simple and efficient web interface.

**Version 2: Custom-trained Models**

In the second version, I plan to implement custom-trained models:

- **Speech-to-Text**: Training a custom model tailored to specific audio datasets.
- **Sentiment Analysis**: Developing a custom sentiment analysis model using machine learning techniques.
- **Deployment**: Switching from Flask to [Streamlit](https://streamlit.io/) for a more interactive and user-friendly interface.

<!-- Note
Problem:
Issue with ffmpeg when trying to run ML_test/sentiment_analysis.py.

Solution:
Run ```scoop install ffmpeg``` to install ffmpeg. 

-->
