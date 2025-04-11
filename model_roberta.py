from transformers import pipeline

# Load RoBERTa sentiment pipeline
def load_model():
    sentiment_pipeline = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")
    return sentiment_pipeline

def analyze_sentiment(text, model):
    result = model(text)
    return result[0]['label'], result[0]['score']
