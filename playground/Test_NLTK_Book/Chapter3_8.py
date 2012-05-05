from __future__ import division
import nltk, re, pprint

print len(nltk.corpus.brown.words()) / len(nltk.corpus.brown.sents())


sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
text = nltk.corpus.gutenberg.raw('chesterton-thursday.txt')
sents = sent_tokenizer.tokenize(text)
pprint.pprint(sents[171:181])
