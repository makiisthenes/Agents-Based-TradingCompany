from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
from langchain.llms import Ollama
from langchain.tools import tool
import json, os, requests, torch
from crewai import Agent, Task


class SentimentTools:
	@tool("Get sentiment analysis of content")
	def get_simple_sentiment_analysis(self, content: str):
		"""
			This tool allows the agent to analyze specific snippets of a text and determine the sentiment of the text.
			https://huggingface.co/ProsusAI/finbert/
		"""
		# Load the sentiment analysis pipeline
		sentiment_pipeline = pipeline(task="sentiment-analysis", model="ProsusAI/finbert")
		# Run sentiment analysis
		results = sentiment_pipeline(content)
		# Parse the results
		sentiment = results[0]['label']
		confidence = results[0]['score']
		result = {
			"sentiment": sentiment,
			"confidence": confidence
		}
		return result

	@tool("Get strong sentiment analysis of content")
	def get_strong_sentiment_analysis(self, text_prompt: str):
		"""
			This model has better understanding of language, and can be used to analyze the sentiment of the text.
			https://huggingface.co/LinguaCustodia/fin-pythia-1.4b
		"""
		SENTIMENT_MODEL = "LinguaCustodia/fin-pythia-1.4b"
		# Explicitly set the CUDA device
		device = "cuda"
		tokenizer = AutoTokenizer.from_pretrained(SENTIMENT_MODEL)
		model = AutoModelForCausalLM.from_pretrained(SENTIMENT_MODEL).to(
			device)  # We are classifying based on sequential data (text). Make sense.
		# text_prompt = ("IKEA reported record-breaking profits for the quarter, exceeding analyst expectations and driving their stock price to new highs.")
		prompt = (
			f"### Instruction: Analyze the sentiment of this statement extracted from a financial news article. Provide "
			f"your answer as either strongly negative, negative, positive, strongly positive, or neutral. \n"
			f"### Text: {text_prompt} \n### Answer:")
		target_classes = ["positive", "negative", "neutral", 'strongly positive', 'strongly negative']
		target_class_ids = tokenizer.convert_tokens_to_ids(target_classes)
		inputs = tokenizer(prompt, return_tensors="pt", add_special_tokens=False).to(device)
		outputs = model(inputs.input_ids)
		top_output = outputs.logits[0][-1][target_class_ids].argmax(dim=0)
		# print("Understanding the output of the model.")
		# print(outputs.logits[0][-1])
		#
		# detokenized_output = tokenizer.decode(outputs)
		# print(detokenized_output)
		return target_classes[top_output]

