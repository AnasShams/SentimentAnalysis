# import pandas as pd
# import nltk
# from nltk.sentiment import SentimentIntensityAnalyzer

# nltk.download("vader_lexicon")
# sia = SentimentIntensityAnalyzer()

# df = pd.read_csv("cleaned_sentiment140.csv")
# df["cleaned_text"] = df["cleaned_text"].fillna("")

# def get_sentiment(text):
#     score = sia.polarity_scores(text)
#     if score["compound"] >= 0.05:
#         return "Positive"
#     elif score["compound"] <= -0.05:
#         return "Negative"
#     else:
#         return "Neutral"

# df["predicted_sentiment"] = df["cleaned_text"].apply(get_sentiment)
# df.to_csv("sentiment_results.csv", index=False)
# print("Sentiment analysis complete! Saved to sentiment_results.csv")
