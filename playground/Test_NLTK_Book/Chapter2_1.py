from nltk.corpus import gutenberg
print gutenberg.fileids()
print "raw: ", len(gutenberg.raw())
print "words: ", len(gutenberg.words())
print "sents: ", len(gutenberg.sents())

from nltk.corpus import webtext
print len(webtext.raw('firefox.txt'))

from nltk.corpus import nps_chat
nps_chat.fileids()
cr=nps_chat.posts('10-19-20s_706posts.xml')

from nltk.corpus import brown
nt=brown.words(categories='news')

from nltk.corpus import reuters
from nltk.corpus import inaugural

 [w for w in nltk.corpus.udhr.fileids() if 'heb' in w.lower()]
 
nltk.corpus.brown.readme()
nltk.corpus.brown.words()[1:10]

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(nltk.corpus.brown.words()[1:10])

