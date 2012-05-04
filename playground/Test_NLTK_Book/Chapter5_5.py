import nltk
brown_tagged_sents=nltk.corpus.brown.tagged_sents(categories='news')
size = int(len(brown_tagged_sents) * 0.9)
train_sents=brown_tagged_sents[:size]
test_sents=brown_tagged_sents[size:]
unigram_tagger=nltk.UnigramTagger(train_sents)
unigram_tagger.evaluate(test_sents)

bigram_tagger = nltk.BigramTagger(train_sents)
bigram_tagger.evaluate(test_sents)

t0=nltk.DefaultTagger('NN')
t1=nltk.UnigramTagger(train_sents, backoff=t0)
t2=nltk.BigramTagger(train_sents, backoff=t1)
t2.evaluate(test_sents)

from cPickle import dump
output = open('t2.pkl', 'wb')
dump(t2, output, -1)
output.close()


test_tags = [tag for sent in brown.sents(categories='editorial')
                 for (word, tag) in t2.tag(sent)]
gold_tags = [tag for (word, tag) in brown.tagged_words(categories='editorial')]
print nltk.ConfusionMatrix(gold, test)


nltk.tag.brill.demo()

