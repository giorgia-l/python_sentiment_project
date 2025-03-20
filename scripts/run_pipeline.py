import os
import sys
sys.path.append(os.path.abspath('..'))  # Adds the parent directory to sys.path

import logging
from src import config
from src.load_data import load_data #sto richiamando un altro codice python, apriamolo wow:
from src.preprocess import preprocess_data #chiama pure preprocess
from src.make_model import train_model
# from src.evaluation import evaluate_model
# from src.save_results import save_predictions
# Perchè abbiamo messo il pipelyne che richiama altri codici? per evitare di mettere troppo codice e
# farlo girare. divido a livello logico le cose che fanno diverse cose 

# Set up logging
logging.basicConfig(filename='../log/pipeline.log', level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("Starting Sentiment Analysis Pipeline...")

    # Step 1: Load data from Excel and store it in SQLite
    logging.info("Loading raw data...")
    load_data()

    # Step 2: Preprocess text data
    logging.info("Preprocessing data...")
    preprocess_data()

    # Step 3: Train sentiment analysis model
    logging.info("Training the model...")
    train_model()

if __name__ == "__main__":
    main()