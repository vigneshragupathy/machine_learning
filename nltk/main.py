def gender_features(word):
	return {'last_letter': word[-1]}
	#print {'last_letter': word[-1]}
#print gender_features("word")

from nltk.corpus import names
labeled_names = ([(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in names.words('female.txt')])
#print labeled_names
import random
random.shuffle(labeled_names)

import nltk
featuresets = [(gender_features(n), gender) for (n, gender) in labeled_names]
train_set, test_set = featuresets[500:], featuresets[:500]
classifier = nltk.NaiveBayesClassifier.train(train_set)

print classifier.classify(gender_features('rachel'))
print(nltk.classify.accuracy(classifier, test_set))
classifier.show_most_informative_features(5)

