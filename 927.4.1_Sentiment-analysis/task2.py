from textblob import TextBlob

# ----- Part 1: Original sample text (from the assignment) -----
sample_text = "I absolutely love this product! The quality is excellent and it arrived on time."

# Create a TextBlob object
blob = TextBlob(sample_text)

# Perform sentiment analysis
sentiment = blob.sentiment

# Print the original text and sentiment analysis results
print("Original Text:", sample_text)
print("Sentiment Analysis Result:")
print("Polarity:", sentiment.polarity)  # Range from -1 (negative) to 1 (positive)
print("Subjectivity:", sentiment.subjectivity)  # Range from 0 (objective) to 1 (subjective)

print()  # Prints an empty line to separate the two results

# ----- Part 2: Extra example with a negative review -----
sample_text_2 = "This product is terrible and it arrived late."

blob_2 = TextBlob(sample_text_2)
sentiment_2 = blob_2.sentiment

print("Original Text:", sample_text_2)
print("Sentiment Analysis Result:")
print("Polarity:", sentiment_2.polarity)
print("Subjectivity:", sentiment_2.subjectivity)