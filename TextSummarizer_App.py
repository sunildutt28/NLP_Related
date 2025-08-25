import streamlit as st
from transformers import pipeline

# Title
st.title("📝 Text Summarizer App")
st.write("Summarize long text into concise highlights using Hugging Face Transformers.")

# Load model once
@st.cache_resource
def load_model():
    return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer = load_model()

# User input
text = st.text_area("Paste your text here:", height=200)

# Summarize button
if st.button("Summarize"):
    if text.strip():
        if len(text.split()) < 40:
            st.warning("⚠️ Please enter a longer text (at least 40 words) for better summarization.")
        else:
            with st.spinner("Summarizing..."):
                summary = summarizer(
                    text,
                    max_length=130,   # maximum length of summary
                    min_length=30,    # minimum length of summary
                    do_sample=False   # deterministic output
                )
                st.subheader("📌 Summary")
                st.success(summary[0]['summary_text'])
    else:
        st.warning("Please enter some text to summarize.")
