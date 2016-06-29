from nltk.tokenize import word_tokenize

# Load a text file if required
text = "Pete ate a large cake. Sam has a big mouth."
output = ""

# Tokenize the text, i.e break it into lines
# tokenized = tokenizer.tokenize(text)

# Get the list of words from the entire text
words = word_tokenize(text)

print words

dict = {'Pete':'cake','ate':'large'}

for i in range(0,len(words)):
    for key in dict:
        if words[i] == key:
            words[i] = dict[key]

print words
