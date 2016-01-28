import re
import string

def remove_punctuation(s):
    """See: http://stackoverflow.com/a/266162
    """
    exclude = set(string.punctuation)
    return ''.join(ch for ch in s if ch not in exclude)

def tokenize(text):
    #text = remove_punctuation(text)
    text = text.lower()
    #return text
    return re.split("\W+", text)

def count_words(words):
    wc = {}
    for word in words:
        wc[word] = wc.get(word, 0.0) + 1.0
    return wc

s = "32824,80 100"
print count_words(tokenize(s))