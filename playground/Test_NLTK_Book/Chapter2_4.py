import nltk

nltk.corpus.stopwords.words('english')
print  len (nltk.corpus.words.words())

entries = nltk.corpus.cmudict.entries()
print entries[100] #phonetics of "abdication"
print nltk.corpus.cmudict.dict()["abdication"]


from nltk.corpus import swadesh
print swadesh.fileids()
print swadesh.words("en")
fr2en=swadesh.entries(["fr", "en"])
translate=dict(fr2en)
print translate["chien"]

from nltk.corpus import wordnet as wn
wn.synsets('boy')
print wn.synset('son.n.02').lemma_names
print wn.synset('son.n.02').definition
print wn.synset('boy.n.02').examples
print wn.synset('son.n.02').lemmas
print wn.lemma('son.n.02.Son')
print wn.lemma('son.n.02.Son').synset
print wn.lemma('son.n.02.Son').name
print wn.lemmas('boy')
print wn.synset('dish.n.01').hyponyms()
print [lemma.name for synset in wn.synset('dish.n.01').hyponyms() for lemma in synset.lemmas]

print wn.synset('boy.n.01').hypernyms()
#print wn.synset('boy.n.01').hypernyms_paths()

#nltk.app.wordnet()

print wn.synset('tree.n.01').part_meronyms()
print wn.synset('tree.n.01').substance_meronyms()
print wn.synset('tree.n.01').member_holonyms()

print wn.synset('walk.v.01').entailments()
print wn.lemma('supply.n.02.supply').antonyms()

dir(wn.synset('harmony.n.02'))


print wn.synset('whale.n.02').min_depth()
print wn.synset('whale.n.02').path_similarity(wn.synset('baleen_whale.n.01'))

print wn.all_synsets('n')
print len(list(wn.all_synsets('v')))
