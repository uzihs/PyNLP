from nltk.book import *

print "concordance:"
text1.concordance("good", lines=300)
text1.concordance("large", lines=300)
print "==================================================="
print "similar:"
text1.similar("good")
print "==================================================="
print "common_contexts:"
text1.common_contexts(["good", "large"])
text1.dispersion_plot(["good", "large"])
print "==================================================="
print "generate:"
text1.generate()
