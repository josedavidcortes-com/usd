with open('donQuixote.txt','r') as myFile:
  text = myFile.read()

import nltk
nltk.download('all')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
lemmatizer = WordNetLemmatizer()

import string

stop_words  = set(stopwords.words('english'))
word_tokens = word_tokenize(text)
#word_tokens = list(map(filter(lambda token: token not in string.punctuation,word_tokens)))
word_tokens = list(filter(lambda token: token not in string.punctuation,word_tokens))
list = []

for word in word_tokens:
  if word not in stop_words:
    list.append(word)




def get_magic(word):
      
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)


for word in word_tokens:
    print(lemmatizer.lemmatize(word,get_magic(word)))

#print(word_tokens)
