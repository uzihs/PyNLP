from __future__ import division
import nltk, re, pprint
from urllib import urlopen
url = "http://www.gutenberg.org/files/2554/2554.txt"
raw=urlopen(url).read()
print len(raw)

print raw.rfind("End of Project")
print raw.rfind("End of Project Gutenberg's Crime")
raw=raw[5334:1157737]

tokens=nltk.wordpunct_tokenize(raw)
text=nltk.Text(tokens)
print text.collocations()

words=[w.lower() for w in text]
vocab=sorted(set(words))
print vocab

url2="http://news.bbc.co.uk/1/hi/health/2284783.stm"
html=urlopen(url2).read()
print html
raw2=nltk.clean_html(html)
# raw2=raw2[3296:3900]
tokens2=nltk.word_tokenize(raw2)
print tokens2