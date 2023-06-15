import spacy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from rake_nltk import Rake

class TextAnalyzer:
    def __init__(self, corpus):
        self.corpus = corpus
        self.nlp = spacy.load('en_core_web_lg')
        self.analyzer = SentimentIntensityAnalyzer()
        self.keyphrase_extractor = Rake()

    def analyze_sentiments(self):
        doc = self.nlp(self.corpus)
        sentiments = []
        for sentence in doc.sents:
            sentiment = self.analyzer.polarity_scores(sentence.text)
            sentiments.append(sentiment)
        return sentiments

    def extract_keyphrases(self):
        doc = self.nlp(self.corpus)
        keyphrases = []
        for sentence in doc.sents:
            self.keyphrase_extractor.extract_keywords_from_text(sentence.text)
            phrases = self.keyphrase_extractor.get_ranked_phrases()
            keyphrases.append(phrases)
        return keyphrases
