import nltk
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer


snowball_stemmer = SnowballStemmer("english")
print(snowball_stemmer.stem('French'))

wordnet_lemmatizer = WordNetLemmatizer()
print(wordnet_lemmatizer.lemmatize('french'))
