import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

nltk.download("vader_lexicon")
sia = SentimentIntensityAnalyzer()

df = pd.read_csv("cleaned_sentiment140.csv")

# Check for NaN values and handle them
# Option 1: Drop rows with NaN in 'cleaned_text'
# df = df.dropna(subset=["cleaned_text"])

# Option 2: Fill NaN values with an empty string
df["cleaned_text"] = df["cleaned_text"].fillna("")

def get_sentiment(text):
    if isinstance(text, str):
        score = sia.polarity_scores(text)
        if score["compound"] >= 0.05:
            return "Positive"
        elif score["compound"] <= -0.05:
            return "Negative"
        else:
            return "Neutral"
    else:
        return "Neutral"  
    
df["predicted_sentiment"] = df["cleaned_text"].apply(get_sentiment)

df.to_csv("sentiment_results.csv", index=False)
print("Sentiment analysis complete! Results saved as 'sentiment_results.csv'.")