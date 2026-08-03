import logging
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_analysis(text_length, polarity):
    logging.info(f"Analyzed text of length {text_length}, polarity: {polarity:.2f}")
