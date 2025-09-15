import streamlit as st
from transformers import pipeline

# Title
st.title("😊 Sentiment Analysis App")
st.write("Classify text as Positive, Negative, or Neutral using Hugging Face Transformers.")

# Load model once
@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment") #for +ve or -ve = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

analyzer = load_model()

# User input
text = st.text_area("Enter text to analyze sentiment:", height=150)

# Analyze button
if st.button("Analyze Sentiment"):
    if text.strip():
        with st.spinner("Analyzing..."):
            result = analyzer(text)[0]
            label = result['label']
            score = round(result['score'], 3)

            st.subheader("📌 Sentiment Result")
            #st.write(f"**Label:** {label}") # to find the label
            st.write(f"**Confidence:** {score}")
            
            # Add emoji indicator
            if label == "LABEL_2":
                st.success("😀 Positive Sentiment")
            elif label == "LABEL_0":
                st.error("😞 Negative Sentiment")
            else:
                st.info("😐 Neutral Sentiment !")
    else:
        st.warning("Please enter some text to analyze.")
