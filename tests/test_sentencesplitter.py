# -*- coding: utf-8 -*-

from lltk.sentencesplitter import SentenceSplitter


def test_splitting():
    """
    Notes:
        This unit test evaluates how good sentences are splitted. Test contains
        4 different scenarios:
        - simple sentence
        - sentence with one abbreviation
        - sentence with multiple abbreviations
        - sentence with qoute

        All these sentences should be splitted correctly.
    """
    splitter = SentenceSplitter()
    sentences = [
        'Labas vakaras.',
        'Čia yra dr. Jono Basanavičiaus rašto darbai.',
        '''Šiaulių apsk. Radviliškio raj. gyventojai nesiekia 100 tūkst.
        gyventojų skaičiaus.''',
        '''Kaip sakė a.a. A. Čepauskas: \"Ne piniguose laimėje, o jų perkamojoje
         galioje.\"'''
    ]
    assert splitter.split(' '.join(sentences)) == sentences
