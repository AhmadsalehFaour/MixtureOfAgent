import logging
import csv
import os
from datetime import datetime

def init_logger():
    log_path = "logs/moa_{}.log".format(datetime.now().date())
    logging.basicConfig(
        filename=log_path,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    return logging.getLogger()

def save_prompt(prompt):
    os.makedirs("logs", exist_ok=True)
    with open("logs/prompts.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().isoformat(), prompt])

def is_valid_response(text):
    return isinstance(text, str) and len(text.strip()) > 30 and any(c.isalpha() for c in text)
