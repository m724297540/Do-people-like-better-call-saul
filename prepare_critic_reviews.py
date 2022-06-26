import pandas as pd
import numpy as np
import nltk
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('wordnet')
# nltk.download('omw-1.4')
import string
import fasttext
import contractions
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer

pd.options.mode.chained_assignment = None
pd.set_option('display.max_colwidth', 100)

# importing data
df = pd.read_csv('Better_Call_Saul_critic_reviews.csv')

#check for missing values
for col in df.columns:
    print(col, df[col].isnull().sum())

#expanding contractions
df['review_quote'] = df['review_quote'].apply(lambda x: [contractions.fix(word) for word in x.split()])
df['review_quote'] = [' '.join(map(str, row)) for row in df['review_quote']]

# only keep reviews that are written in English

#1. English detection
pretrained_model = "C:/Users/cheng/Downloads/lid.176.bin" 
model = fasttext.load_model(pretrained_model)
langs = []
for row in df['review_quote']:
    lang = str(model.predict(row)[0])
    langs .append(lang[-5:-3])
df['language'] = langs

#2. Only keep English reviews
df = df[df['language'] == 'en']

# tokenization
df['review_quote'] = df['review_quote'].apply(word_tokenize)

# covert to lower case
df['review_quote'] = df['review_quote'].apply(lambda x : [word.lower() for word in x])

# remove punctuations
pun = string.punctuation
df['review_quote'] = df['review_quote'].apply(lambda x : [word for word in x if word not in pun])

# remove stopwords
stop_words = set(stopwords.words('english'))
df['review_quote'] = df['review_quote'].apply(lambda x : [word for word in x if word not in stop_words])

# lemmatization
df['pos_tag'] = df['review_quote'].apply(nltk.tag.pos_tag)
def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN
df['wordnet_pos'] = df['pos_tag'].apply(lambda x: [(word, get_wordnet_pos(pos_tag)) for (word, pos_tag) in x])
wnl = WordNetLemmatizer()
df['review_quote_processed'] = df['wordnet_pos'].apply(lambda x: [wnl.lemmatize(word, pos_tag) for (word, pos_tag) in x])
df['review_quote_processed'] = df['review_quote_processed'].apply(lambda x: ' '.join(x))

# save into a csv file
df.to_csv('BCS_processed_critic_reviews.csv')
print('finished!')