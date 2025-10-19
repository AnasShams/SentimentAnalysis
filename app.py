import streamlit as st
import pandas as pd
import time
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")
sia = SentimentIntensityAnalyzer()

st.title("Social Media Sentiment Analyzer 🚀")
st.write("Analyze the sentiment of tweets, comments, or uploaded text files.")

user_input = st.text_area("Type a tweet or comment here...")

if st.button("Analyze Sentiment"):
    if user_input:
        sentiment_score = sia.polarity_scores(user_input)
        sentiment = (
            "Positive 😀" if sentiment_score["compound"] >= 0.05 else
            "Negative 😡" if sentiment_score["compound"] <= -0.05 else
            "Neutral 😐"
        )
        st.write(f"**Sentiment:** {sentiment}")
        st.write(f"Sentiment Scores: {sentiment_score}")
    else:
        st.warning("Please enter text to analyze.")

st.subheader("Upload a CSV file for bulk analysis")
uploaded_file = st.file_uploader("Upload CSV (text column required)", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    if "text" in df.columns:
        df = df.sample(n=100, random_state=42)  

        progress_bar = st.progress(0)
        total = len(df)

        sentiments = []
        for i, text in enumerate(df["text"]):
            score = sia.polarity_scores(str(text))["compound"]
            sentiment = "Positive 😀" if score >= 0.05 else "Negative 😡" if score <= -0.05 else "Neutral 😐"
            sentiments.append(sentiment)

            progress_bar.progress((i + 1) / total)
            time.sleep(0.001)

        df["Sentiment"] = sentiments
        st.write(df)
    else:
        st.error("CSV file must have a column named 'text'.")

st.write("Developed by Anas, Abhinav, Arnav, Saad 😊")