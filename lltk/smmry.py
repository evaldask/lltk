# -*- coding: utf-8 -*-

"""
This algorithm is based on: http://smmry.com/
Summarizes text and returns most 'popular' sentences and words in given text
"""
import re
from collections import Counter
from lltk.stemmer import Stemmer
from lltk.sentencesplitter import SentenceSplitter


class Smmry(object):
    """
    Notes:
        Class to summarize given text. Returns most popular sentences and words

    Attributes:
        __stemmer: Stemmer object to tokenize words in given text
        __splitter: SentenceSplitter object to split given text into sentences

    """

    def __init__(self):
        self.__stemmer = Stemmer()
        self.__splitter = SentenceSplitter()

    def summarize(self, text, top_sentences=5, top_words=5):
        """
        Notes:
            Picks sentences that have most common words in text and returns top
            sentences and most common words
        Args:
            text: string element that contain paragraph or large chuck of text
            top_sentences: number of top sentences to return
            top_words: number of top words to return

        Returns:
            common_sentences: array of tuples that contains sentences
                (in order) and score for that sentence
            common_words: array of tuples that contain word (stemmed) and
                number of how many times it has been repeated in text
        """

        text = text.replace(u'“', '"').replace(
            u'„', '"').replace(u'–', '-').replace('\n', '')
        cleaned = re.sub(r'[?|$|.|!|-|,|"|:|;]', r'', text).lower()
        splitted = cleaned.split(' ')
        stemmed = []
        for word in splitted:
            stemmed.append(self.__stemmer.stem(word))

        # remove insignificant elements such as:
        # dots, commas, words that are two or single letters and etc.
        stemmed = filter(lambda x: len(x) > 2, stemmed)
        tokens_counter = Counter(stemmed)

        sentences = self.__splitter.split(text)
        sentences_counter = Counter()
        for idx, sentence in enumerate(sentences):
            cleaned_sentence = re.sub(
                r'[?|$|.|!|-|,|"|:|;]', r'', sentence).lower()
            splitted_sentence = cleaned_sentence.split(' ')
            total = 0
            for word in splitted_sentence:
                total += tokens_counter[self.__stemmer.stem(word)]
            sentences_counter[idx] = total

        top_items = sentences_counter.most_common(top_sentences)
        in_order = sorted(top_items, key=lambda x: x[0])

        common_sentences = []
        for item in in_order:
            common_sentences.append((sentences[item[0]], item[1]))

        common_words = tokens_counter.most_common(top_words)

        return common_sentences, common_words
