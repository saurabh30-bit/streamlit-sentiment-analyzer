def clean_text(text):
    import re
    text = re.sub(r'http\S+', '', text)
    return text.strip()
