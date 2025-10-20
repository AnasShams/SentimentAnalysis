from flask import Flask, render_template, request, jsonify
from textblob import TextBlob
import logging

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze-text', methods=['POST'])
def analyze_text():
    try:
        data = request.get_json()
        if not data or 'text' not in data:
            return jsonify({'error': 'No text provided'}), 400
        
        text = data['text'].strip()
        if not text:
            return jsonify({'error': 'Please enter text to analyze'}), 400
        
        # Use TextBlob instead of NLTK
        analysis = TextBlob(text)
        polarity = analysis.sentiment.polarity

        if polarity >= 0.05:
            sentiment = "Positive 😀"
        elif polarity <= -0.05:
            sentiment = "Negative 😡"
        else:
            sentiment = "Neutral 😐"

        return jsonify({
            'success': True,
            'sentiment': sentiment,
            'polarity': polarity,
            'text_preview': text[:100] + '...' if len(text) > 100 else text
        })

    except Exception as e:
        logger.error(f"Error analyzing text: {str(e)}")
        return jsonify({'error': f'Analysis error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)