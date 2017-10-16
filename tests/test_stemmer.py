# -*- coding: utf-8 -*-

from lltk.stemmer import Stemmer


def test_stemmer():
    """
    Notes:
        Stemmer class should be tested as blackbox since it may contain several
        different implementations (dictionary lookup and stem generation).
    """
    stemmer = Stemmer()

    assert stemmer.stem('Jonas') == 'Jon'
    assert stemmer.stem('laikrodžiai') == 'laikrod'
    assert stemmer.stem('sekretorės') == 'sekretor'
    assert stemmer.stem('klaidelės') == 'klaid'
    assert stemmer.stem('triukšmauti') == 'triukšm'
