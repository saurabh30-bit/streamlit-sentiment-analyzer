import matplotlib
matplotlib.use('Agg')

def get_sentiment_color(polarity):
    if polarity > 0.1:
        return '#22c55e'
    elif polarity < -0.1:
        return '#ef4444'
    return '#eab308'

def format_confidence(subjectivity):
    return f'{(1 - subjectivity) * 100:.1f}%'
