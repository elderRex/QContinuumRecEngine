import nltk
from nltk.corpus import brown
from nltk.tag import RegexpTagger,UnigramTagger,BigramTagger,TrigramTagger

class nlp_tagger:

    def __init__(self):
        self.patterns = [
            (r'^@\w+', 'NNP'),
            (r'^\d+$', 'CD'),
            (r'.*ing$', 'VBG'),
            (r'.*ment$', 'NN'),
            (r'.*ful$', 'JJ'),
            (r'.*', 'NN')
        ]
        self.target = ['NOUN','ADJ','VERB','ADV']

    def train(self):

        self.re_tagger = nltk.RegexpTagger(self.patterns)
        self.bi_tagger = BigramTagger(brown.tagged_words(), backoff=self.re_tagger)
        self.tri_tagger = TrigramTagger(brown.tagged_words(), backoff=self.bi_tagger)