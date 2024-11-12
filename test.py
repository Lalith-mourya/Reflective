import re
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download("stopwords")

# Load the trained model
filename = 'trained_model.sav'
model = pickle.load(open(filename, 'rb'))

# Load the vectorizer used for training
vectorizer = TfidfVectorizer()
vectorizer = pickle.load(open('vectorizer.sav', 'rb'))

# Initialize the Porter Stemmer
port_stem = PorterStemmer()

# Define preprocessing function
def preprocess_text(text):
    # Remove non-alphabet characters
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.lower()
    text = text.split()
    # Remove stopwords and apply stemming
    text = [port_stem.stem(word) for word in text if word not in stopwords.words('english')]
    return ' '.join(text)

# Get user input
user_input = input("Enter a sentence to analyze sentiment: ")

# Preprocess and vectorize the input text
processed_input = preprocess_text(user_input)
input_vector = vectorizer.transform([processed_input])

# Make a prediction
prediction = model.predict(input_vector)

# Print the result
if prediction[0] == "positive":
    print("The sentiment of the entered text is Positive.")
else:
    print("The sentiment of the entered text is Negative.")
