Sentiment Analysis Web App

A simple web application built with Streamlit and NLTK (VADER Sentiment Analyzer) that performs sentiment analysis on user-provided text.

🚀 Features

User-friendly interface built with Streamlit

Analyzes text sentiment as Positive, Negative, Neutral, or Compound Score

Real-time results with visual indicators

Lightweight and fast

🛠️ Tech Stack

Frontend / UI: Streamlit

Backend / Processing: Python

NLP: NLTK VADER Sentiment Analyzer

📂 Project Structure
3day-mini-project/
│── app.py                 # Main Streamlit app
│── requirements.txt       # Dependencies
│── README.md              # Project documentation
└── (nltk_data)            # NLTK resources (auto-downloaded)

⚙️ Installation & Setup
1. Clone the repository
git clone https://github.com/your-username/SentimentAnalysis.git
cd SentimentAnalysis

2. Create Virtual Environment (optional but recommended)
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On Mac/Linux

3. Install Dependencies
pip install -r requirements.txt

4. Run the App
streamlit run app.py

📊 Example Output

Input:

I really love this project!


Output:

Positive Sentiment 😊
Compound Score: 0.72

📝 Requirements

Python 3.8+

Streamlit

NLTK

Install manually if needed:

pip install streamlit nltk


Also download the VADER lexicon (if not already present):

import nltk
nltk.download('vader_lexicon')

🤝 Contributing

Feel free to fork this repository, open issues, and submit pull requests to enhance the project.