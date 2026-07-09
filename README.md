# 💬 Real-Time Sentiment Analyzer

A modern, interactive web application built with Python and Streamlit that performs real-time sentiment analysis on text using Natural Language Processing (NLP).

## 🚀 Features
- **Real-Time Analysis**: Instantly calculates the sentiment of user input.
- **Polarity Scoring**: Determines if the text is Positive, Negative, or Neutral (-1 to 1).
- **Subjectivity Scoring**: Determines if the text is objective (fact) or subjective (opinion) (0 to 1).
- **Key Phrase Extraction**: Automatically extracts the core noun phrases from the input text.
- **Beautiful UI**: Built with Streamlit for a clean, responsive frontend.

## 📦 Tech Stack
- **Python 3.9+**
- **Streamlit**: For the web interface
- **TextBlob**: For lexical sentiment analysis
- **Pandas**: For data handling

## 🛠️ Local Setup & Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/saurabh30-bit/streamlit-sentiment-analyzer.git
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Future Roadmap
- Integrate custom fine-tuned transformer models in the \models\ directory.

