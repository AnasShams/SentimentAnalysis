import json
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")
sia = SentimentIntensityAnalyzer()

def handler(request):
    try:
        # Expect text to analyze in JSON body
        body = request.get("body")
        if body:
            data = json.loads(body)
            text = data.get("text")
        else:
            # Or fallback to query parameter
            text = request.get("queryStringParameters", {}).get("text")

        if not text:
            return {
                "statusCode": 400,
                "headers": {"Content-Type": "application/json"},
                "body": json.dumps({"error": "No text provided"})
            }

        scores = sia.polarity_scores(text)
        sentiment = (
            "Positive 😀" if scores["compound"] >= 0.05 else
            "Negative 😡" if scores["compound"] <= -0.05 else
            "Neutral 😐"
        )

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({
                "text": text,
                "sentiment": sentiment,
                "scores": scores
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": str(e)})
        }
