import re
import string

def remove_punctuation(s):
    """See: http://stackoverflow.com/a/266162
    """
    exclude = set(string.punctuation)
    return ''.join(ch for ch in s if ch not in exclude)

def tokenize(text):
    text = remove_punctuation(text)
    text = text.lower()
    return re.split("\W+", text)

def count_words(words):
    wc = {}
    for word in words:
        wc[word] = wc.get(word, 0.0) + 1.0
    return wc

s = "Hello my name, is Greg. My favorite food is pizza."
count_words(tokenize(s))
{'favorite': 1.0, 'food': 1.0, 'greg': 1.0, 'hello': 1.0, 'is': 2.0, 'my': 2.0, 'name': 1.0, 'pizza': 1.0}

from sh import find

# setup some structures to store our data
vocab = {}
word_counts = {
    "vivek": {},
    "vikki": {}
}
priors = {
    "vivek": 0.,
    "vikki": 0.
}
docs = []
for f in find("sample-data"):
    f = f.strip()
    if not f.endswith(".txt"):
        # skip non .txt files
        continue
    elif "cryptid" in f:
        category = "vivek"
    else:
        category = "vikki"
    docs.append((category, f))
    # ok time to start counting stuff...
    priors[category] += 1
    text = open(f).read()
    words = tokenize(text)
    counts = count_words(words)
    for word, count in list(counts.items()):
        # if we haven't seen a word yet, let's add it to our dictionaries with a count of 0
        if word not in vocab:
            vocab[word] = 0.0  # use 0.0 here so Python does "correct" math
        if word not in word_counts[category]:
            word_counts[category][word] = 0.0
        vocab[word] += count
        word_counts[category][word] += count


#new_doc = open("examples/Allosaurus.txt").read()
#new_doc = open("examples/Python.txt").read()
new_doc = open("examples/vikki.txt").read()
words = tokenize(new_doc)
counts = count_words(words)

import math

prior_vikki = (priors["vikki"] / sum(priors.values()))
prior_vivek = (priors["vivek"] / sum(priors.values()))

log_prob_vivek = 0.0
log_prob_vikki = 0.0
for w, cnt in list(counts.items()):
    # skip words that we haven't seen before, or words less than 3 letters long
    if w not in vocab or len(w) <= 3:
        continue

    p_word = vocab[w] / sum(vocab.values())
    p_w_given_vikki = word_counts["vikki"].get(w, 0.0) / sum(word_counts["vikki"].values())
    p_w_given_vivek = word_counts["vivek"].get(w, 0.0) / sum(word_counts["vivek"].values())

    if p_w_given_vikki > 0:
        log_prob_vikki += math.log(cnt * p_w_given_vikki / p_word)
    if p_w_given_vivek > 0:
        log_prob_vivek += math.log(cnt * p_w_given_vivek / p_word)

print("Score(vikki)  :", math.exp(log_prob_vikki + math.log(prior_vikki)))
print("Score(vivek):", math.exp(log_prob_vivek + math.log(prior_vivek)))
