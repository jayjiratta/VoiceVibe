from transformers import pipeline

sentiment_analyzer = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

text = "I feel normal with product!"
result = sentiment_analyzer(text)
print(result)