import nltk, re, pprint

raw = """'When I'M a Duchess,' she said to herself, (not in a very hopeful tone
though), 'I won't have any pepper in my kitchen AT ALL. Soup does very
well without--Maybe it's always pepper that makes people hot-tempered,'..."""

raw.split()

re.split(r'\W+', raw)

print re.findall(r"\w+(?:[-']\w+)*|'|[-.(]+|\S\w*", raw)


 	
text = 'That U.S.A. poster-print costs $12.40...'
pattern = r'''(?x)    # set flag to allow verbose regexps
     ([A-Z]\.)+        # abbreviations, e.g. U.S.A.
   | \w+(-\w+)*        # words with optional internal hyphens
   | \$?\d+(\.\d+)?%?  # currency and percentages, e.g. $12.40, 82%
   | \.\.\.            # ellipsis
   | [][.,;"'?():-_`]  # these are separate tokens
 '''
nltk.regexp_tokenize(text, pattern)
