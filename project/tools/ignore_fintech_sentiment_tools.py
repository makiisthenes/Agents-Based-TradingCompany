# Michael Peres 16/02/2024
# Using FinBERT to analyze sentiment of text. https://huggingface.co/ProsusAI/finbert/
# This tool lalows the agent to analyze specific snippets of text and determine the sentiment of the text.
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os, requests, json
import torch
from transformers import AutoTokenizer, pipeline, AutoModelForSequenceClassification
# AutoModelForCausalLM, AutoModelForSeq2SeqLM

# We are not going to run the model on the HuggingFace hub, but instead we are going to run it locally.
# Load the environmental variables.
load_dotenv()

# Load the model and tokenizer
FINBERT_SENTIMENT_MODEL = "ProsusAI/finbert"

tokenizer = AutoTokenizer.from_pretrained(FINBERT_SENTIMENT_MODEL)
model = AutoModelForSequenceClassification.from_pretrained(FINBERT_SENTIMENT_MODEL)  # We are classifying based on sequential data (text). Make sense.




input_text = "Stocks rallied and the British pound gained."

# Tokenize the input text
tokens = tokenizer(input_text, return_tensors="pt")
# Run the model on the input text
with torch.no_grad():
    # Make sure to use the correct model output attribute depending on the task (e.g., 'logits' for classification)
    outputs = model(**tokens)

logits = outputs.logits

# Optionally, apply a softmax to get probabilities
probs = torch.nn.functional.softmax(logits, dim=-1)

# Get the predicted class (index with the highest probability)
SENTIMENT_CLASSES = ["positive", "neutral", "negative"]
predicted_class = torch.argmax(probs, dim=-1).item()
print("Output of model", probs, SENTIMENT_CLASSES[predicted_class])  # positive, neutral, negative.