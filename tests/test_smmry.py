# -*- coding: utf-8 -*-

"""
Unit tests for testing SentenceSplitter class
"""


from lltk import Smmry


def test_smmry():

    """
    This test is to check how if smmry algorithm performs.
    """
    smmry = Smmry()
    text = [
        '''Čia yra ilgas ilgas ilgas tekstas.''',
        '''Žodis ilgas kartojasi tekste ilgai.'''
    ]
    sentences, words = smmry.summarize(' '.join(text), 1, 1)
    assert sentences == [(text[0], 17)]
    assert words == [('ilg', 5)]
