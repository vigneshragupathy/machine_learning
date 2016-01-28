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
    return re.split("\W+", text)

def count_words(words):
    wc = {}
    for word in words:
        wc[word] = wc.get(word, 0.0) + 1.0
    return wc

#s = "Hello my name, is Greg. My favorite food is pizza."
#count_words(tokenize(s))

from sh import find

# setup some structures to store our data
vocab = {}
word_counts = {
    "http": {},
    "https": {}
}
priors = {
    "http": 0.,
    "https": 0.
}
docs = []
for f in find("sample-data"):
    f = f.strip()
    if not f.endswith(".txt"):
        # skip non .txt files
        continue
    elif "http" in f:
        category = "http"
    else:
        category = "https"
    docs.append((category, f))
    # ok time to start counting stuff...
    priors[category] += 1
    text = open(f).read()
    words = tokenize(text)
    #print words
    #print words
    counts = count_words(words)
    #print counts
    for word, count in list(counts.items()):
        # if we haven't seen a word yet, let's add it to our dictionaries with a count of 0
        if word not in vocab:
            vocab[word] = 0.0  # use 0.0 here so Python does "correct" math
        if word not in word_counts[category]:
            word_counts[category][word] = 0.0
        vocab[word] += count
        word_counts[category][word] += count
        #print vocab[word]
        #print word_counts[category][word]

new_doc = open("examples/dummy_3.txt").read()
words = tokenize(new_doc)
print words
counts = count_words(words)
print counts

import math

prior_http = (priors["http"] / sum(priors.values()))
prior_https = (priors["https"] / sum(priors.values()))
print prior_http
print prior_https

log_prob_http = 0.0
log_prob_https = 0.0
for w, cnt in list(counts.items()):
    # skip words that we haven't seen before, or words less than 3 letters long
    if w not in vocab or len(w) <= 1:
        continue

    p_word = vocab[w] / sum(vocab.values())
    p_w_given_http = word_counts["http"].get(w, 0.0) / sum(word_counts["http"].values())
    p_w_given_https = word_counts["https"].get(w, 0.0) / sum(word_counts["https"].values())

    if p_w_given_http > 0:
        log_prob_http += math.log(cnt * p_w_given_http / p_word)
    if p_w_given_https > 0:
        log_prob_https += math.log(cnt * p_w_given_https / p_word)

#print("Score(http)  :", math.exp(log_prob_http + math.log(prior_http)))
#print("Score(https):", math.exp(log_prob_https + math.log(prior_https)))

score_http = math.exp(log_prob_http + math.log(prior_http))
score_https = math.exp(log_prob_https + math.log(prior_https))
print "Score for http is %s"%(score_http)
print "Score for https is %s"%(score_https)


if score_http > score_https:
    print "The file is classified as http"
else:
    print "The file is classified as https"