import nltk


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
#viterbi_parser = nltk.ViterbiParser(grammar)
#print viterbi_parser.parse(['Jack', 'saw', 'telescopes'])

chart=nltk.EarleyChartParser(grammar)
print chart.parse(sent)


