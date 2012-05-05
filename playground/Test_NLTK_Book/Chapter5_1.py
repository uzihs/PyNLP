import nltk

#text = nltk.work_tokenize("How are you doing, Sir?")
#print nltk.pos_tag(text)

print nltk.help.upenn_tagset('RB')
print nltk.help.upenn_tagset('NN.*')
print nltk.help.upenn_tagset('.*')

# below 2 meaning to refuse
text = nltk.word_tokenize("They refuse to permit us to obtain the refuse permit")
print nltk.pos_tag(text)


text = nltk.Text(word.lower() for word in nltk.corpus.brown.words())
print text.similar('woman')
print text.similar('the')

tagged_token = nltk.tag.str2tuple('fly/NN')
print tagged_token

sent = '''
 The/AT grand/JJ jury/NN commented/VBD on/IN a/AT number/NN of/IN
 other/AP topics/NNS ,/, AMONG/IN them/PPO the/AT Atlanta/NP and/CC
 Fulton/NP-tl County/NN-tl purchasing/VBG departments/NNS which/WDT it/PPS
 said/VBD ``/`` ARE/BER well/QL operated/VBN and/CC follow/VB generally/RB
 accepted/VBN practices/NNS which/WDT inure/VB to/IN the/AT best/JJT
 interest/NN of/IN both/ABX governments/NNS ''/'' ./.
 '''
print [nltk.tag.str2tuple(t) for t in sent.split()]

print nltk.corpus.brown.tagged_words()[1:30]
print nltk.corpus.brown.tagged_words(simplify_tags=True)[1:30]


from nltk.corpus import brown
brown_news_tagged = brown.tagged_words(categories='news', simplify_tags=True)
tag_fd = nltk.FreqDist(tag for (word, tag) in brown_news_tagged)
print tag_fd.keys()

#try "the ADJ man" in Brown Simplified
nltk.app.concordance()


wsj = nltk.corpus.treebank.tagged_words(simplify_tags=True)
word_tag_fd = nltk.FreqDist(wsj)
print word_tag_fd
print [word + "/" + tag for (word, tag) in word_tag_fd if tag.startswith('V')]


cfd1 = nltk.ConditionalFreqDist(wsj)
print cfd1['cut'].keys()


cfd2 = nltk.ConditionalFreqDist((tag, word) for (word, tag) in wsj)
print cfd2['VN'].keys()

                                       
