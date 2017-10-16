# -*- coding: utf-8 -*-

"""
Unit tests for testing SentenceSplitter class
"""


from lltk import SentenceSplitter


def test_sentencesplitter():
    """
    This test is to check how good sentence splitter is. It contains 4 tests:
    - simple sentence,
    - sentence that starts with abbreviation,
    - multiple abbreviations in sentence,
    - sentence with quote.
    """

    splitter = SentenceSplitter()

    sentences = [
        '''Labas vakaras.''',
        '''Dr. Jonas Basanavičius buvo signataras.''',
        '''Šiaulių apskr. Radvilišio raj. turi mažiau nei 100 tūkst.
        gyventojų.''',
        '''Kaip a.a. draugas A. Sipavičius sakė: \"Ne piniguose laimė, o jų
        perkamojoje galioje.\"'''
    ]

    assert splitter.split(' '.join(sentences)) == sentences
