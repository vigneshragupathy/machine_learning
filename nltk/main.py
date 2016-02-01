import subprocess
def traffic_features(packet_details):
	packet_details = packet_details.strip()
	#t[-1] = t[-1].strip()
	LIST_1 = packet_details.split("\t")[-1:]
	#LIST_2 = LIST_1.split(",")[-1]
	LIST_out = (", ".join(LIST_1))
	LIST_2 = LIST_out.split(",")[-1]
	#return {'traffic_port': LIST_out}
	return {'traffic_port': LIST_2}
	#print packet_details[-1]
	#return packet_details[-1]
	#output1 = subprocess.call(["echo",packet_details,"|","awk","{'print $NF'}"])
	#return  packet_details[-1]
	#return output1

	#return {'last_letter': word[-1]}
	#print {'last_letter': word[-1]}
#print gender_features("word")

#from nltk.corpus import names
#http_file = open('vikki_http.txt')
http_file = open('test.txt')
#https_file = open('vikki_https.txt')
https_file = open('test_1.txt')
labeled_traffic = ([(traffic, 'http') for traffic in iter(http_file)] + [(traffic, 'https') for traffic in iter(https_file)])

import random
random.shuffle(labeled_traffic)
#print labeled_traffic
#traffic_features("")

import nltk
#for (n, traffic) in labeled_traffic:
	#print "n is %s and traffic is %s"%(n,traffic)
featuresets = [(traffic_features(n), traffic) for (n, traffic) in labeled_traffic]
#print featuresets
train_set, test_set = featuresets[200:], featuresets[:200]
#print train_set
classifier = nltk.NaiveBayesClassifier.train(train_set)

sample_packet = "192.168.184.131 74.125.68.99    1       54      40      49586,80"
result = classifier.classify(traffic_features(sample_packet))
print "The packet type is %s"%(result)
print(nltk.classify.accuracy(classifier, test_set))
classifier.show_most_informative_features(5)

