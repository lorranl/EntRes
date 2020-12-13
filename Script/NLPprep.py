import os
import pandas as pd
import string
import re
import en_core_web_sm
nlp = en_core_web_sm.load()
import nltk
from spacy.lang.en.stop_words import STOP_WORDS
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


# Add custom stop words
STOP_WORDS.update({"ltd","llc","inc","group","limited"})


def nopunct(words):
    words = re.sub("\s[-!$%^&*()_+|~=`{}\[\]:\";'<>?,.\/]\s", " ", words)
    words = re.sub("[-!$%^&*()_+|~=`{}\[\]:\";'<>?,.\/]", "", words)
    return words

def stopwords(words):
    toks = word_tokenize(words)
    filtered = [w for w in toks if not w in STOP_WORDS]
    return ' '.join(filtered)


# load test files / paths
base = "D:\python\EntRes\Tests\\base.csv"
comp =
tgt =


file = pd.read_csv(base, header=None, dtype="string")
file['lower'] = file[0].str.lower()
file['nopunct'] = file['lower'].apply(nopunct)
file['tokens'] = file['nopunct'].apply(stopwords)

