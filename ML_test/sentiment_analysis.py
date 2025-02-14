from transformers import pipeline

sentiment_analyzer = pipeline("sentiment-analysis")

text = "I love this product! It's amazing."
result = sentiment_analyzer(text)
print("ผลการวิเคราะห์ความรู้สึก:", result)