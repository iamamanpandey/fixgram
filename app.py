import streamlit as st
import whisper
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
from audiorecorder import audiorecorder


@st.cache_resource
def load_llama_model():
    try:
        llm = CTransformers(
            model="models/llama-2-7b-chat.ggmlv3.q8_0.bin",
            model_type="llama",
            config={"max_new_tokens": 256, "temperature": 0.01},
        )
        return llm
    except Exception as e:
        return None, str(e)


@st.cache_resource
def load_whisper_model():
    try:
        return whisper.load_model("base.en")
    except Exception as e:
        return None, str(e)


def getLLammaResponse(input_text):
    ## Prompt Template

    template = """ Please fix grammar for `{input_text}` """

    prompt = PromptTemplate(input_variables=[""], template=template)
    llm = load_llama_model()

    ## Generate the response from the LLama 2 model
    response = llm(prompt.format(input_text=input_text))
    return response


st.set_page_config(
    page_title="Generate",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.header("FixGram  🤖")

input_text = st.text_input("Enter the Sentence")

audio = audiorecorder("Click to record", "Click to stop recording")
if len(audio) > 0:
    st.audio(audio.export().read())
    audio.export("audio.wav", format="wav")


col1, col2 = st.columns(2)

with col1:
    submit = st.button("Submit")
with col2:
    transcribeAudio = st.button("Transcribe Audio")


if transcribeAudio:
    if audio is not None:
        model = load_whisper_model()
        result2 = model.transcribe("audio.wav")
        st.write(result2["text"])
    if len(result2["text"]) > 0:
        st.markdown(getLLammaResponse(result2["text"]))


# Final response
if submit:
    st.write(getLLammaResponse(input_text))


# if st.button("Transcribe Audio"):
#     if audio_file is not None:
#         st.success("Audio file uploaded")
#         result = model.transcribe(audio_file.name)
#         st.success("Transcribe Successful")
#         st.text(result["text"])
#         st.text("Correct Answer:")
#         st.markdown(getLLammaResponse(result["text"]))
#     else:
#         st.sidebar.error("No audio file uploaded")
