import sys
from textblob.classifiers import NaiveBayesClassifier

def training_from_file():
	with open('train.json', 'r') as fp:
		global cl
		cl = NaiveBayesClassifier(fp, format="json")

def analize(sent):
	result = cl.classify(sent)
	percent = int(cl.prob_classify(sent).prob(result)*100)
	print "%s%% %s - '%s'" % (percent, result, sent)

if len(sys.argv) > 1:
	training_from_file()
	analize(sys.argv[1])
else:
	print "ERROR missing argv!"
	print "usage: python sentiment.py <sentence>"
