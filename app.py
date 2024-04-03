import streamlit as st
from audio_recorder_streamlit import audio_recorder
import whisper
import soundfile as sf
import numpy as np
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
import io
import torch
import fleep


def getLLamaresponse(input_text):

    ### LLama2 model
    llm = CTransformers(
        model="models/llama-2-7b-chat.ggmlv3.q8_0.bin",
        model_type="llama",
        config={"max_new_tokens": 256, "temperature": 0.01},
    )

    ## Prompt Template

    template = """ Please fix grammer for `{input_text}` """

    prompt = PromptTemplate(input_variables=[""], template=template)

    ## Generate the ressponse from the LLama 2 model
    response = llm(prompt.format(input_text=input_text))
    return response


def recognize_audio(audio_data):
    if audio_data:
        with open(audio_data, "wb") as f:
            f.write(audio_data)


# try:


# model = whisper.load_model("base")

# Convert byte data to NumPy array

# result = model.transcribe(audio_data)

#     return  result["text"]
# except Exception as e:
#         return None, str(e)


st.set_page_config(
    page_title="Generate",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.header(" FixGram  🤖")

input_text = st.text_input("Enter the Sentence")

audio_bytes = audio_recorder()
if audio_bytes:
    with open(audio_bytes, "rb" ) as f:
            f.write(audio_bytes)

submit = st.button("Submit")

## Final response
# if submit:
#     st.write(recognize_audio(audio_bytes))
