#http://www.nltk.org/getting-started
#sudo python -m nltk.downloader -d /usr/share/nltk_data all

#recursive descent parser (top down_ demo:
nltk.app.rdparser()

#shift reduce parser (bottom up; very simple implementation without backtracking - doesnt' always succeed):
nltk.app.srparser()

#chart parser:
nltk.app.chartparser    ()

nltk.parse.chart.demo()
#this has all the following options:
#    1: Top-down chart parser
#    2: Bottom-up chart parser
#    3: Bottom-up left-corner chart parser
#    4: Left-corner chart parser with bottom-up filter
#    5: Stepping chart parser (alternating top-down & bottom-up)
#    6: All parsers

#http://nltk.googlecode.com/svn/trunk/doc/api/nltk.parse.earleychart.EarleyChartParser-class.html



#parse trees:
nltk.app.tree() #doestn' work



grammar1 = nltk.data.load('file:mygrammar.cfg')
#or
grammar1 = nltk.parse_cfg("""
  S -> NP VP
  VP -> V NP | V NP PP
  PP -> P NP
  V -> "saw" | "ate" | "walked"
  NP -> "John" | "Mary" | "Bob" | Det N | Det N PP
  Det -> "a" | "an" | "the" | "my"
  N -> "man" | "dog" | "cat" | "telescope" | "park"
  P -> "in" | "on" | "by" | "with"
  """)

sent = "Mary saw Bob".split()
rd_parser = nltk.RecursiveDescentParser(grammar1) #trace=1,2,3
for tree in rd_parser.nbest_parse(sent):
    print tree

sr_parser=nltk.ShiftReduceParser(grammar1)  #trace=1,2,3
print sr_parser.parse(sent)

chart=nltk.ChartParser(grammar1)
print chart.parse(sent)

chart=nltk.EarleyChartParser(grammar1)
print chart.parse(sent)

from nltk.corpus import treebank
print treebank.parsed_sents('wsj_0001.mrg')[0]
treebank.parsed_sents('wsj_0001.mrg')[0].draw()


#large_grammars:
#[uzi-mbp: ~/_LinguisticsData/grammars/large_grammars/]$ ls
#total 8072
#drwxr-xr-x   8 Uzi  staff      272 May  5 00:19 ./
#drwxr-xr-x  12 Uzi  staff      408 May  5 00:19 ../
#-rw-r--r--   1 Uzi  staff  1103405 May  5 00:19 alvey.fcfg
#-rw-r--r--   1 Uzi  staff    16467 May  5 00:19 alvey_sentences.txt
#-rw-r--r--   1 Uzi  staff   197405 May  5 00:19 atis.cfg
#-rw-r--r--   1 Uzi  staff     6953 May  5 00:19 atis_sentences.txt
#-rw-r--r--   1 Uzi  staff  2781333 May  5 00:19 commandtalk.cfg
#-rw-r--r--   1 Uzi  staff    10169 May  5 00:19 commandtalk_sentences.txt


#PCFG:

grammar = nltk.parse_pcfg("""
    S    -> NP VP              [1.0]
    VP   -> TV NP              [0.4]
    VP   -> IV                 [0.3]
    VP   -> DatV NP NP         [0.3]
    TV   -> 'saw'              [1.0]
    IV   -> 'ate'              [1.0]
    DatV -> 'gave'             [1.0]
    NP   -> 'telescopes'       [0.8]
    NP   -> 'Jack'             [0.2]
    """)
viterbi_parser = nltk.ViterbiParser(grammar)
print viterbi_parser.parse(['Jack', 'saw', 'telescopes'])

nltk.parse.viterbi.demo()

#Grammars?
#  http://pargram.b.uib.no/
#  http://www.delph-in.net/matrix/
#  http://www.cis.upenn.edu/~xtag/