import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("english")

text = "Pete ate a large cake Sam has a bigger mouth cooked"
output = ""

# Tokenize the text, i.e break it into lines
# tokenized = tokenizer.tokenize(text)

# tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
# sentences = tokenizer.tokenize(text)
# print sentences
# Get the list of words from the entire text
words = word_tokenize(text)
print(stemmer.stem("bigger"))
print words
# print(stemmer.stem(words))


# replace this dict with input file
dict = {'Pete':'cake','ate':'large','cooked':'talked'}
print dict

# manipulate each word
for i in range(0,len(words)):
    # replacing with dict elemnts
    for key in dict:
        if words[i] == key:
            words[i] = dict[key]

# stemming
    # words[i] = stemmer.stem(words[i])

# adding synonyms, with their relative similarity number

    # synonyms SET of words[i]
    synonyms = wordnet.synsets(words[i])

    # synonym of first elemnt of synonyms SET, used for comparision as this fist element is word itself,
    if synonyms:
        w1 = wordnet.synset(synonyms[0].name())

    # action on each synonyms
    for syn in synonyms:

            # w2 stores synonym of syn
            w2 = wordnet.synset(syn.name())


            # comparision of w1's synonyms with w1
            if w2 and w1:

                compare = w1.wup_similarity(w2)
                if compare > 0.75:
                    words[i] += "|" + syn.lemmas()[0].name() + ","
                    compare = '{0:.4f}'.format(compare)
                    words[i] += compare
                    print compare

    print words[i]

# print words
