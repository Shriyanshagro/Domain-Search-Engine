from __future__ import print_function
import nltk
from nltk.stem.snowball import SnowballStemmer



stemmer = SnowballStemmer("english")

print(stemmer.stem("running"))
