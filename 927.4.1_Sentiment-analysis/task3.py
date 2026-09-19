from textblob import TextBlob

# Sample customer feedback comments
feedback_comments = [
    "The service was fantastic and the staff was very helpful.",
    "I am unhappy with the product quality and delivery was delayed.",
    "The product is okay, but it could be improved.",
    "Amazing experience! I am very satisfied with my purchase."
]

# Function to analyze sentiment of each comment
def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

# Analyze and print sentiment for each feedback comment
for comment in feedback_comments:
    sentiment = analyze_sentiment(comment)
    print(f"Feedback: {comment}")
    print(f"Sentiment Polarity: {sentiment}")
    print("-----")