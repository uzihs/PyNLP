from __future__ import division
import nltk, re, pprint

wsj=sorted(set(nltk.corpus.treebank.words()))
fd=nltk.FreqDist(vs for word in wsj
                    for vs in re.findall(r'[aeiou]{2,}', word))
print fd.items()



regexp=r'^[AEIOUaeiou]+|[AEIOUaeiou]+$|[^AEIOUaeiou]'
def compress(word):
    pieces=re.findall(regexp, word)
    return ''.join(pieces)
english_uhdr = nltk.corpus.udhr.words('English-Latin1')
print nltk.tokenwrap(compress(w) for w in english_uhdr[:75])


cv_word_pairs=[(cv,w) for w in nltk.corpus.toolbox.words('rotokas.dic')
                      for cv in re.findall(r'[ptksvr][aeiou]', w)]
cv_index=nltk.Index(cv_word_pairs)
print cv_index['su']


print re.findall(r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processes')


from nltk.corpus import gutenberg
moby=nltk.Text (gutenberg.words('melville-moby_dick.txt'))
print moby.findall(r"<a>(<.*>)<man>")

chat = nltk.Text (nltk.corpus.nps_chat.words())
print chat.findall(r"<l.*>{3,}")

nltk.re_show(r'a', 'banana')

nltk.app.nemo()

from nltk.corpus import brown
hobbies_learned = nltk.Text(brown.words(categories=['hobbies', 'learned']))
print hobbies_learned.findall(r"<\w*> <and> <other> <\w*s>")
print hobbies_learned.findall(r"<as> <\w*> <as> <\w*s>")



