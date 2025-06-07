import spacy

# Load English model
nlp = spacy.load("en_core_web_sm")

# Input text
text = "He felt anger. She angers quickly. They were angry all day."

# Process the text
doc = nlp(text)

# Tokenization and Lemmatization
lemmas = [token.lemma_ for token in doc if token.is_alpha]

print("Lemmatized Tokens:", lemmas)
