def main() -> None:
    print("Hello from nltk-01!")

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download("vader_lexicon", quiet=True)


def main():
    analyzer = SentimentIntensityAnalyzer()

    texts = [
        "I love this course, it's amazing!",
        "This is the worst lab ever.",
        "The class starts at 9am.",
    ]

    for text in texts:
        sentiment_score = analyzer.polarity_scores(text)
        print(text)
        print(sentiment_score)

        compound = sentiment_score["compound"]
        if compound >= 0.05:
            print("Sentiment: Positive\n")
        elif compound <= -0.05:
            print("Sentiment: Negative\n")
        else:
            print("Sentiment: Neutral\n")
if __name__ == "__main__":
    main()