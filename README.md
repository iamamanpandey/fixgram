# FixGram 🤖 - Speech-to-Text Grammar Correction

A Streamlit application that combines Whisper AI for speech-to-text conversion and Llama 2 for grammar correction. Users can either type text directly or record audio, which will be transcribed and then grammatically corrected.

## Features

- Speech-to-text conversion using OpenAI's Whisper
- Grammar correction using Llama 2
- Real-time audio recording capability
- User-friendly interface built with Streamlit
- Support for both text input and audio input

## Prerequisites

Before running this application, make sure you have the following:

- Python 3.8 or higher
- Required models:
  - Llama 2 model file (`llama-2-7b-chat.ggmlv3.q8_0.bin`) in the `models` directory
  - Whisper base English model (will be downloaded automatically on first run)

## Installation

1. Clone the repository:
```bash
git clone [your-repository-url]
cd [repository-name]
```

2. Install the required packages:
```bash
pip install streamlit whisper langchain ctransformers audiorecorder
```

3. Download the Llama 2 model:
   - Download `llama-2-7b-chat.ggmlv3.q8_0.bin`
   - Place it in the `models` directory of your project

## Usage

1. Run the Streamlit application:
```bash
streamlit run app.py
```

2. Use the application:
   - Type text directly into the input field and click "Submit" for grammar correction
   - OR
   - Click "Click to record" to record audio
   - Click "Click to stop recording" when finished
   - Click "Transcribe Audio" to convert speech to text and correct grammar

## Project Structure

```
project/
│
├── app.py              # Main application file
├── models/            # Directory for model files
│   └── llama-2-7b-chat.ggmlv3.q8_0.bin
│
└── README.md          # Project documentation
```

## Key Components

- `load_llama_model()`: Initializes the Llama 2 model for grammar correction
- `load_whisper_model()`: Loads the Whisper model for speech-to-text conversion
- `getLLammaResponse()`: Processes text through the Llama 2 model for grammar correction

## Cache Implementation

The application uses Streamlit's caching mechanism (`@st.cache_resource`) to optimize performance:
- Model loading is cached to prevent repeated loading
- Both Whisper and Llama models are loaded only once per session

## Error Handling

The application includes error handling for:
- Model loading failures
- Audio processing issues
- Text input validation

