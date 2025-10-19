import pandas as pd
import re
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")
stop_words = set(stopwords.words("english"))

df = pd.read_csv("sentiment140.csv", encoding="latin1", usecols=[0, 5], names=["sentiment", "text"])

df["sentiment"] = df["sentiment"].map({0: "negative", 4: "positive"})

def clean_text(text):
    text = text.lower()  
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)
    text = re.sub(r"@\w+|\#\w+", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = " ".join(word for word in text.split() if word not in stop_words)
    return text

df["cleaned_text"] = df["text"].apply(clean_text)

df.to_csv("cleaned_sentiment140.csv", index=False)

print("Data preprocessing complete! Saved as 'cleaned_sentiment140.csv'.")
