import json
import os

HISTORY_FILE = 'analysis_history.json'

def save_analysis(text, polarity, subjectivity):
    history = load_history()
    history.append({'text': text[:100], 'polarity': polarity, 'subjectivity': subjectivity})
    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f)

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE) as f:
            return json.load(f)
    return []
