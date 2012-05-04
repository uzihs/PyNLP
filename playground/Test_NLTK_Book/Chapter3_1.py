from __future__ import division
import nltk, re, pprint
from urllib import urlopen
url = "http://www.gutenberg.org/files/2554/2554.txt"
raw=urlopen(url).read()
len(raw)

raw.rfind("End of Project")
raw.rfind("End of Project Gutenberg's Crime")
raw=raw[5334:1157737]

tokens=nltk.wordpunct_tokenize(raw)
text=nltk.Text(tokens)
text.collocations()

words=[w.lower() for w in text]
vocab=sorted(set(words))


url2="http://news.bbc.co.uk/1/hi/health/2284783.stm"
html=urlopen(url2).read()
print html
raw2=nltk.clean_html(html)
# raw2=raw2[3296:3900]
tokens2=nltk.word_tokenize(raw2)
