from transformers import pipeline
import torch
print(torch.__version__)
print(torch.cuda.is_available())

model = pipeline("summarization", model="facebook/bart-large-cnn")
response = model("Text to summarize goes here")
print(response)