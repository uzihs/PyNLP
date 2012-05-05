import nltk
import pprint

print "****** gutenberg"
from nltk.corpus import gutenberg
print gutenberg.fileids()
print "raw: ", len(gutenberg.raw())
print "words: ", len(gutenberg.words())
print "sents: ", len(gutenberg.sents())

print "****** webtext"
from nltk.corpus import webtext
print len(webtext.raw('firefox.txt'))

print "****** nps_chat"
from nltk.corpus import nps_chat
print nps_chat.fileids()
cr=nps_chat.posts('10-19-20s_706posts.xml')
print cr

print "****** brown"
from nltk.corpus import brown
nt=brown.words(categories='news')
print nt

from nltk.corpus import reuters
from nltk.corpus import inaugural

print [w for w in nltk.corpus.udhr.fileids() if 'heb' in w.lower()]
 
print nltk.corpus.brown.readme()
print nltk.corpus.brown.words()[1:10]

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(nltk.corpus.brown.words()[1:10])

