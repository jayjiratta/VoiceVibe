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

## Phase 1: Baseline Model Deployment
**Objective:** simple prototype using pre-trained models without fine-tuning.

### Technologies:
- **web:** Flask
- **Models:**
  - **Speech-to-Text (STT):** [Whisper by OpenAI](https://openai.com/research/whisper)
  - **Sentiment Analysis:** [Transformer models from Hugging Face](https://huggingface.co/models)
- **Frontend:** Flask templates and basic HTML/CSS

## Phase 2: Custom Model Implementation
**Objective:** using a smaller pre-trained STT model for fine-tuning and a custom-trained Sentiment Analysis model.

### Technologies:
- **web:** [Streamlit](https://streamlit.io/)
- **Models:**
  - **STT:** Pretrained STT model
  - **Sentiment Analysis:** Custom-trained transformer model

<!-- Note
Problem:
Issue with ffmpeg when trying to run ML_test/sentiment_analysis.py.

Solution:
Run ```scoop install ffmpeg``` to install ffmpeg. 

-->
