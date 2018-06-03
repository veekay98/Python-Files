#This is used to access webpages and open urls
import urllib.request
response = urllib.request.urlopen('http://php.net/')
html = response.read()

import nltk
from nltk.corpus import stopwords

from bs4 import BeautifulSoup
soup = BeautifulSoup(html,"html5lib")
text = soup.get_text(strip=True)

from nltk.tokenize import sent_tokenize,word_tokenize
tokens = word_tokenize(text)

clean_tokens = tokens[:]
sr = stopwords.words('english')

for token in tokens:
	if token in stopwords.words('english'):

        	clean_tokens.remove(token)

freq = nltk.FreqDist(clean_tokens)

for key,val in freq.items():

    print (str(key) + ':' + str(val))






mytext = "Hello Adam, how are you? I hope everything is going well. Today is a good day, see you dude."

print(sent_tokenize(mytext))

print(word_tokenize(mytext))

from nltk.corpus import wordnet

syn = wordnet.synsets("love")

print(syn[0].definition())

print(syn[0].examples())




synonyms = []

for syn in wordnet.synsets('awesome'):

    for lemma in syn.lemmas():

        synonyms.append(lemma.name())

print(synonyms)


from nltk.corpus import wordnet

antonyms = []

for syn in wordnet.synsets("small"):

    for l in syn.lemmas():

        if l.antonyms():

            antonyms.append(l.antonyms()[0].name())

print(antonyms)

from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
print(stemmer.stem('working'))

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize('increases'))
print(lemmatizer.lemmatize('playing', pos="v"))



print(lemmatizer.lemmatize('playing', pos="v"))#verb

print(lemmatizer.lemmatize('playing', pos="n"))#noun

print(lemmatizer.lemmatize('playing', pos="a"))#adjective

print(lemmatizer.lemmatize('playing', pos="r"))#adverb





print(stemmer.stem('stones'))

print(stemmer.stem('speaking'))

print(stemmer.stem('bedroom'))

print(stemmer.stem('jokes'))

print(stemmer.stem('lisa'))

print(stemmer.stem('purple'))

print('----------------------')

print(lemmatizer.lemmatize('stones'))

print(lemmatizer.lemmatize('speaking'))

print(lemmatizer.lemmatize('bedroom'))

print(lemmatizer.lemmatize('jokes'))

print(lemmatizer.lemmatize('lisa'))

print(lemmatizer.lemmatize('purple'))


locs = [('Omnicom', 'IN', 'New York'),
        ('DDB Needham', 'IN', 'New York'),
        ('Kaplan Thaler Group', 'IN', 'New York'),
       ('BBDO South', 'IN', 'Atlanta'),
        ('Georgia-Pacific', 'IN', 'Atlanta')]
query = [e1 for (e1, rel, e2) in locs if e2=='New York']
print(query)