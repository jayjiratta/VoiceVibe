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

5. Run the Flask application:

    ```
    flask --app app  run --debug
    ```

6. Open your web browser and navigate to `http://localhost:5000` to access the application.
