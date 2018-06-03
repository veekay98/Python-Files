import nltk, re, pprint
locs = [('Omnicom', 'IN', 'New York'),
        ('DDB Needham', 'IN', 'New York'),
        ('Kaplan Thaler Group', 'IN', 'New York'),
       ('BBDO South', 'IN', 'Atlanta'),
        ('Georgia-Pacific', 'IN', 'Atlanta')]
query = [e1 for (e1, rel, e2) in locs if e2=='New York']
print(query)

def ie_preprocess(document):
	sentences=nltk.sent_tokenize(document)
	sentences=[nltk.word_tokenize(sent) for sent in sentences]
	sentences=[nltk.pos_tag(sent) for sent in sentences]

sentence = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"), 
 ("dog", "NN"), ("barked", "VBD"), ("at", "IN"),  ("the", "DT"), ("cat", "NN")]

grammar = "NP: {<DT>?<JJ>*<NN>}" 

cp = nltk.RegexpParser(grammar) 
result = cp.parse(sentence) 
print(result) 



grammar = r"""
  NP: {<DT|PP\$>?<JJ>*<NN>}   # chunk determiner/possessive, adjectives and noun
      {<NNP>+}                # chunk sequences of proper nouns
"""
cp = nltk.RegexpParser(grammar)
sentence = [("Rapunzel", "NNP"), ("let", "VBD"), ("down", "RP"), 
                 ("her", "PP$"), ("long", "JJ"), ("golden", "JJ"), ("hair", "NN")]

print(cp.parse(sentence)) 


#cp = nltk.RegexpParser('CHUNK: {<V.*> <TO> <V.*>}')
brown = nltk.corpus.brown
for sent in brown.tagged_sents():
	tree = cp.parse(sent)
        for subtree in tree.subtrees():
        	if subtree.label() == 'CHUNK': 
                	print(subtree)