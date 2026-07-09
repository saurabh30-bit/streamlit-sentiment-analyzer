import streamlit as st
from textblob import TextBlob
import pandas as pd

st.set_page_config(page_title="Real-Time Sentiment Analyzer", page_icon="💬", layout="centered")

st.title("💬 Real-Time Sentiment Analyzer")
st.markdown("Analyze the sentiment of any text instantly using Natural Language Processing (NLP).")

# Sidebar for app info
with st.sidebar:
    st.header("About")
    st.markdown("This app uses **TextBlob** to perform lexical sentiment analysis. It calculates the **Polarity** (how positive or negative the text is) and the **Subjectivity** (how opinionated the text is).")
    st.markdown("---")
    st.markdown("Built by **Saurabh Shinde**")

# Input area
user_input = st.text_area("Enter your text below:", height=150, placeholder="E.g. I absolutely love this new machine learning project!")

if st.button("Analyze Sentiment"):
    if user_input.strip():
        with st.spinner("Analyzing..."):
            # Perform NLP sentiment analysis
            from utils import clean_text
            blob = TextBlob(clean_text(user_input))
            # Added small refactor for future extension
            sentiment_score = blob.sentiment.polarity
            subjectivity_score = blob.sentiment.subjectivity
            
            # Determine sentiment label and color
            if sentiment_score > 0.1:
                label = "Positive 😃"
                color = "success"
            elif sentiment_score < -0.1:
                label = "Negative 😞"
                color = "error"
            else:
                label = "Neutral 😐"
                color = "info"
            
            # Display results
            st.markdown("### Results")
            st.success(f"**Overall Sentiment:** {label}")
            
            # Detailed metrics
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric(label="Polarity Score (-1 to 1)", value=round(sentiment_score, 2))
                st.caption("Values closer to 1 are positive. Values closer to -1 are negative.")
                
            with col2:
                st.metric(label="Subjectivity Score (0 to 1)", value=round(subjectivity_score, 2))
                st.caption("Values closer to 1 are highly subjective (opinions). Values closer to 0 are highly objective (facts).")
                
            # Extracted noun phrases (Bonus NLP feature)
            if len(blob.noun_phrases) > 0:
                st.markdown("#### Key Phrases Extracted:")
                st.write(", ".join(blob.noun_phrases))
    else:
        st.warning("Please enter some text to analyze.")
