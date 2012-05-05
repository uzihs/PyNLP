#http://www.python.org/dev/peps/pep-0008/
#http://www.python.org/dev/peps/pep-0257/
import nltk

words = ['I', 'turned', 'off', 'the', 'spectroroute']
words[2], words[3], words[4] = words[3], words[4], words[2]
print words


words = ['I', 'turned', 'off', 'the', 'spectroroute']
tags = ['noun', 'verb', 'prep', 'det', 'noun']
print zip(words, tags)
print list(enumerate(words))


text = nltk.corpus.nps_chat.words()
cut = int(0.9 * len(text))
training_data, test_data = text[:cut], text[cut:]
print text == training_data + test_data   #validate
print len(training_data) / len(test_data) #validate


words = 'I turned off the spectroroute'.split()
wordlens = [(len(word), word) for word in words]
print wordlens.sort()
print ' '.join(w for (_, w) in wordlens)


#print max(w.lower() for w in nltk.word_tokenize(text))


sent = ['Take', 'care', 'of', 'the', 'sense', ',', 'and', 'the',
        'sounds', 'will', 'take', 'care', 'of', 'themselves', '.']
def extract_property(prop):
    return [prop(word) for word in sent]
print extract_property(len)

print extract_property(lambda w: w[-1])

print sorted(sent, lambda x, y: cmp(len(y), len(x)))



def search2(substring, words):
    for word in words:
        if substring in word:
            yield word
print "search2:"
for item in search2('zz', nltk.corpus.brown.words()):
    print item
    
def permutations(seq):
    if len(seq) <= 1:
        yield seq
    else:
        for perm in permutations(seq[1:]):
            for i in range(len(perm)+1):
                 yield perm[:i] + seq[0:1] + perm[i:]

def is_content_word(word):
    return word.lower() not in ['a', 'of', 'the', 'and', 'will', ',', '.']
sent = ['Take', 'care', 'of', 'the', 'sense', ',', 'and', 'the',
        'sounds', 'will', 'take', 'care', 'of', 'themselves', '.']
print filter(is_content_word, sent)

print [w for w in sent if is_content_word(w)]


print map(lambda w: len(filter(lambda c: c.lower() in "aeiou", w)), sent)

print [len([c for c in w if c.lower() in "aeiou"]) for w in sent]


import pdb
#import mymodule
#pdb.run('mymodule.myfunction()')


 	
from timeit import Timer
vocab_size = 100000
setup_list = "import random; vocab = range(%d)" % vocab_size 
setup_set = "import random; vocab = set(range(%d))" % vocab_size 
statement = "random.randint(0, %d) in vocab" % vocab_size * 2 
print Timer(statement, setup_list).timeit(1000)
print Timer(statement, setup_set).timeit(1000)



#example for docstring
 	
def accuracy(reference, test):
    """
    Calculate the fraction of test items that equal the corresponding reference items.

    Given a list of reference values and a corresponding list of test values,
    return the fraction of corresponding values that are equal.
    In particular, return the fraction of indexes
    {0<i<=len(test)} such that C{test[i] == reference[i]}.
 	
    >>> accuracy(['ADJ', 'N', 'V', 'N'], ['N', 'N', 'V', 'ADJ'])
    0.5

@param reference: An ordered list of reference values.
@type reference: C{list}
@param test: A list of values to compare against the corresponding
    reference values.
@type test: C{list}
@rtype: C{float}
@raise ValueError: If C{reference} and C{length} do not have the
    same length.
"""

    if len(reference) != len(test):
        raise ValueError("Lists must have the same length.")
    num_correct = 0
    for x, y in izip(reference, test):
        if x == y:
            num_correct += 1
    return float(num_correct) / len(reference)

