# -*- coding: utf-8 -*-

"""
Unit tests for testing SentenceSplitter class
"""


from lltk import Stemmer


def test_stemmer():

    """
    This test is to check how if stemmer works properly. Tests should be
    abstract because they should be able to validate different implementations
    for stemmer (generative and reading from dictionary).
    """
    stemmer = Stemmer()

    assert stemmer.stem('Jonukas') == 'Jon'
    assert stemmer.stem('sekretorės') == 'sekretor'
    assert stemmer.stem('puškėti') == 'pušk'
    assert stemmer.stem('puškuočioti') == 'pušk'
    assert stemmer.stem('judesiu') == 'jud'
    assert stemmer.stem('pažodžiauti') == 'pažod'
    assert stemmer.stem('Jonas') == 'Jon'
    assert stemmer.stem('mergaite') == 'merg'
    assert stemmer.stem('bernel') == 'bern'
