nltk.corpus.stopwords.words('english')
len (nltk.corpus.words.words())

entries = nltk.corpus.cmudict.entries()
entries[100] #phonetics of "abdication"
nltk.corpus.cmudict.dict()["abdication"]


from nltk.corpus import swadesh
swadesh.fileids()
swadesh.words("en")
fr2en=swadesh.entries(["fr", "en"])
translate=dict(fr2en)
translate["chien"]

from nltk.corpus import wordnet as wn
wn.synsets('boy')
wn.synset('son.n.02').lemma_names
wn.synset('son.n.02').definition
wn.synset('boy.n.02').examples
wn.synset('son.n.02').lemmas
wn.lemma('son.n.02.Son')
wn.lemma('son.n.02.Son').synset
wn.lemma('son.n.02.Son').name
wn.lemmas('boy')
wn.synset('dish.n.01').hyponyms()
[lemma.name for synset in wn.synset('dish.n.01').hyponyms() for lemma in synset.lemmas]

wn.synset('boy.n.01').hypernyms()
wn.synset('boy.n.01').hypernyms_paths()

nltk.app.wordnet()

wn.synset('tree.n.01').part_meronyms()
wn.synset('tree.n.01').substance_meronyms()
wn.synset('tree.n.01').member_holonyms()

wn.synset('walk.v.01').entailments()
wn.lemma('supply.n.02.supply').antonyms()

dir(wn.synset('harmony.n.02'))


wn.synset('whale.n.02').min_depth()
wn.synset('whale.n.02').path_similarity(wn.synset('baleen_whale.n.01'))

wn.all_synsets('n')
len(list(wn.all_synsets('v')))
