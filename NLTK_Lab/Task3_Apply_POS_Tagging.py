import nltk

# Downloading NLTK resources needed for tokenizing and POS tagging
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

# Sample business document
business_document = """
The recent feedback from Acme Corp highlighted issues with the new model of the Omega widget.
Customers from New York and San Francisco have reported delays in shipping.
The CEO of Acme Corp, Jane Doe, mentioned plans to address these concerns by Q3.
"""

# Tokenizing the document
tokens = nltk.word_tokenize(business_document)

# Applying POS tagging
pos_tags = nltk.pos_tag(tokens)

# Printing words and their POS tags
print("Words and POS Tags:")
for word, tag in pos_tags:
    print(f"{word}: {tag}")